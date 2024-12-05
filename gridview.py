import os
from PIL import ImageGrab, Image, ImageDraw
import ollama

# Constants
OUTPUT_DIR = "grid_images"
GRID_SIZE = 10  # Adjust to change the number of grid squares (e.g., 10x10)

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Capture the entire screen
screen = ImageGrab.grab()
screen_width, screen_height = screen.size

# Calculate grid dimensions
grid_width = screen_width // GRID_SIZE
grid_height = screen_height // GRID_SIZE

# Draw the grid on the screen
grid_image = screen.copy()
draw = ImageDraw.Draw(grid_image)
for x in range(0, screen_width, grid_width):
    draw.line((x, 0, x, screen_height), fill="red", width=1)
for y in range(0, screen_height, grid_height):
    draw.line((0, y, screen_width, y), fill="red", width=1)

# Save the grid reference image
grid_image.save(os.path.join(OUTPUT_DIR, "grid_reference.png"))

# Save each grid square as a separate image
print("Saving grid squares and analyzing with Llama 3.2-Vision...")
descriptions = []  # To store descriptions of each grid

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        # Calculate bounding box for each grid square
        left = j * grid_width
        top = i * grid_height
        right = left + grid_width
        bottom = top + grid_height

        # Crop the grid square
        cropped = screen.crop((left, top, right, bottom))

        # Save the cropped image
        filename = f"grid_{i}_{j}.png"
        image_path = os.path.join(OUTPUT_DIR, filename)
        cropped.save(image_path)

        # Analyze the image with Ollama's Llama 3.2-Vision
        try:
            response = ollama.chat(
                model="llama3.2-vision:11b",
                messages=[
                    {
                        "role": "user",
                        "content": "Describe this image?",
                        "images": [image_path],
                    }
                ],
            )
            # Extract and store the description
            cleaned_text = response['message']['content'].strip()
            descriptions.append({
                "grid_position": {"row": i + 1, "col": j + 1},
                "bounding_box": {"x1": left, "y1": top, "x2": right, "y2": bottom},
                "description": cleaned_text
            })
            print(f"Grid ({i + 1}, {j + 1}): {cleaned_text}")
        except Exception as e:
            print(f"Error analyzing grid ({i + 1}, {j + 1}): {e}")
            descriptions.append({
                "grid_position": {"row": i + 1, "col": j + 1},
                "bounding_box": {"x1": left, "y1": top, "x2": right, "y2": bottom},
                "description": "Error: Unable to analyze"
            })

# Save descriptions to a JSON file
import json
with open(os.path.join(OUTPUT_DIR, "grid_descriptions.json"), "w") as json_file:
    json.dump(descriptions, json_file, indent=4)

print(f"All grid descriptions saved in '{os.path.join(OUTPUT_DIR, 'grid_descriptions.json')}'")
