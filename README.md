Grid Image Processing Tool with AI Analysis
This tool captures your computer's entire screen, divides it into a grid of smaller regions, and uses Ollama's Llama 3.2-Vision model to analyze and describe the content of each grid square. The goal is to create a dataset of labeled grid squares, which can be used for UI automation, training AI models, or understanding screen layouts programmatically.

Key Features
Screen Capture:

Captures a full-screen snapshot of the current display.
Supports any resolution or aspect ratio.
Grid Division:

Divides the screen into a grid of N x N squares (default: 10x10).
Each square is saved as an individual image file for further processing.
AI-Powered Analysis:

Passes each grid image to Llama 3.2-Vision, a powerful vision-based AI model, to generate a description of the content.
Supports use cases such as detecting UI components, icons, or screen layouts.
Dataset Generation:

Saves metadata for each grid square in a JSON file, including:
Grid position (row, column).
Bounding box coordinates.
AI-generated description of the content.
Error Handling:

Handles errors gracefully during the AI analysis stage.
Logs and skips problematic grid squares to ensure uninterrupted processing.
How It Works
1. Grid Division
The screen is divided into a grid, where each cell is defined by:

Its row and column index in the grid.
The bounding box coordinates (x1, y1, x2, y2) that represent the region of the screen corresponding to the grid cell.
2. Saving Grid Images
Each grid cell is cropped from the screen and saved as a PNG image in a folder named grid_images.

3. AI Description
The cropped grid image is passed to Llama 3.2-Vision for analysis. The model generates a text description of the image's content, which is stored in a JSON file for later use.

Output Files
Grid Images:

Each grid square is saved as an image file named grid_<row>_<col>.png, where <row> and <col> are the grid indices.
Example: grid_0_0.png represents the grid square in the first row and first column.
Grid Reference Image:

A full-screen image (grid_reference.png) with a red grid overlay for visualization.
JSON Metadata:

A JSON file (grid_descriptions.json) containing:
Grid position (row, col).
Bounding box coordinates (x1, y1, x2, y2).
AI-generated description of the grid content.
