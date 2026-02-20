# Nightingale Rose Project
# Florence Nightingale's Rose Diagram — A Replication
![Logo](assets/logo.svg)

## The Story
This is the Nightingale Rose diagram from 19th century that shows a polar plot with unequal sector radii. Nightingale initially used it to demonstrate that the death rate of soldiers in the crimean war due to poor sanitation was far higher than the direct combat death rate, thus successfully persuading the government to improve medical and sanitation conditions. 

## How the Data Was Collected
This application is a data digitization tool designed to extract coordinates from the "Nightingale-mortality.jpg" image. It provides a graphical user interface (GUI) built with library tkinter and matplotlib to allow users to interactively mark specific data points (Origin, Red, Blue, Black) on the image.
The tool allows user to:
- Mark an **Origin** point using the mouse.
- Mark **Red**, **Blue**, and **Black** data points using keyboard shortcuts.
- The program records the pixel coordinates (x, y) of each point on the image. 
- Navigate (pan/zoom) the image.
- Save grouped data points into a nested dictionary structure.
- Export the collected data to a JSON file (`digitized_data.json`) upon exit.

## The Math and Visualization
1. from coordinates to radius (r) 
using the euclidean distance formula, the distance from the classification marker (xi, yi) to the center point (x0, y0) is calculated from the coordinates to the radius (r). this distance is the pixel radius r of the sector. 
<img width="828" height="191" alt="Screenshot From 2026-02-19 19-51-09" src="https://github.com/user-attachments/assets/5aedaf88-6c7e-4b83-a72a-856f384bb9b4" />

2. the direct proportionality between area and value 
nightingale's core design principle is that the area 'a' of the sector is directly proportional to the number of deaths. at a fixed angle (e.g., 30∘ or π/6 radians per month), the formula for calculating the sector area is: 
<img width="426" height="189" alt="Screenshot From 2026-02-19 19-53-31" src="https://github.com/user-attachments/assets/a3ff3547-f656-47a0-b18c-12cbb5ab84a3" />
since θ is a constant for all sectors, therefore: a∝r²

This means that if we want to compare mortality rates over two months, we are comparing the square of the radius. this is precisely where nightingale's brilliance lies—she knew that human vision perceives area more strongly than length. 

## The Visualization

<img width="194" height="148" alt="image" src="https://github.com/user-attachments/assets/24016509-bf59-4f93-a1f2-b9aea6480c4a" />

## Key Insights

## Technical Details

- Language: Python  
- Libraries:
    - `tkinter` (usually comes with Python)
    - `matplotlib`
    - `Pillow` (PIL)
    - `numpy`
- Files:
     GUI_digitizer.py            README.md             requirements.txt
    'Implementatioin Plan'       assets
     Nightingale-mortality.jpg   digitized_data.json
        

## How to Run

1. Clone this repository.  
2. Create and activate a virtual environment (optional).  
3. Install requirements (if you have a `requirements.txt`).  
4. Run the plotting script:  
   `python3 GUI_digitizer.py`  

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

## What I Learned

Through this project, I gained a deeper understanding of how to bridge the gap between historical static model and modern digital analysis by building a custom coordinate extraction tool. When ensuring that the mathematical translation from pixel Euclidean distance to polar area remained historically accurate.

## References
- Nightingale’s Original Diagrams - The Florence Nightingale image
