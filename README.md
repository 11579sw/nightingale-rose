# Nightingale Advanced Digitizer

## Description
This application is a data digitization tool designed to extract coordinates from the "Nightingale-mortality.jpg" image. It provides a graphical user interface (GUI) built with `tkinter` and `matplotlib` to allow users to interactively mark specific data points (Origin, Red, Blue, Black) on the image.

The tool allows you to:
- Mark an **Origin** point using the mouse.
- Mark **Red**, **Blue**, and **Black** data points using keyboard shortcuts.
- Navigate (pan/zoom) the image.
- Save grouped data points into a nested dictionary structure.
- Export the collected data to a JSON file (`digitized_data.json`) upon exit.

## Prerequisites
Ensure you have Python installed along with the following libraries:

- `tkinter` (usually comes with Python)
- `matplotlib`
- `Pillow` (PIL)
- `numpy`

## Installation
1.  Clone the repository or download the source code.
2.  Install the required dependencies:
    ```bash
    pip install matplotlib pillow numpy
    ```
3.  Ensure the image file `Nightingale-mortality.jpg` is present in the same directory as the script.

## Usage

1.  Run the application:
    ```bash
    python realapp.py
    ```

2.  **Controls**:
    - **Mode Switching**: Click the button at the top left to toggle between "Digitize (Crosshair)" and "Navigate (Pan/Zoom)" modes.
    - **Digitize Mode**:
        - **Left Click**: Set the **Origin** point (displayed as a yellow dot).
        - **'r' Key**: Set the **Red** point at the current mouse position.
        - **'b' Key**: Set the **Blue** point at the current mouse position.
        - **'k' Key**: Set the **Black** point at the current mouse position.
    - **Navigate Mode**:
        - **Zoom In**: Hold down the right mouse button and drag to the upper right. You will see a rectangle; release the button to zoom in on the image to that area.
        - **Zoom Out**: Hold down the right mouse button and drag to the lower left. The image will shrink.
        - **Pan**: Hold down the left mouse button and drag to move the image and view different areas.
    - **Save Group**: Click the "Save Group (To Nested Dict)" button to save the current set of points (Origin, Red, Blue, Black) as a group. 
        This resets the Red, Blue, and Black points but keeps the Origin for the next group.
    - **Undo**: Click the "Undo (Ctrl+Z)" button to undo the last action.

3.  **Exiting and Saving**:
    - When you close the window, you will be prompted to save the data.
    - If you choose "Yes", the data will be exported to `digitized_data.json`.

## Output
The data is saved in `digitized_data.json` with the following structure:

```json
{
    "Group_1": {
        "Origin": [x, y],
        "Red": [x, y],
        "Blue": [x, y],
        "Black": [x, y]
    },
    "Group_2": {
        ...
    }
}
```
# Nightingale Rose Project
