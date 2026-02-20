import svgwrite
import math

def create_logo(filename):
    dwg = svgwrite.Drawing(filename, profile='full', size=('200px', '200px'))
    center_x, center_y = 100, 100
    radius = 80
    num_wedges = 12
    
    # Nightingale Rose Diagram / Radial Bar Chart
    # Use different lengths for wedges to simulate data
    lengths = [0.4, 0.6, 0.8, 0.5, 0.9, 0.7, 0.3, 0.6, 0.8, 0.5, 0.9, 0.4]
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF', '#FFFF99', 
              '#FF6666', '#3399FF', '#66FF66', '#FFB366', '#B366FF', '#FFFF66']
    
    angle_step = 360 / num_wedges
    
    for i in range(num_wedges):
        start_angle = i * angle_step
        end_angle = (i + 1) * angle_step
        
        # Calculate coordinates for wedge (simplified as path)
        # Convert degrees to radians for math functions
        start_rad = math.radians(start_angle - 90) # -90 to start at top
        end_rad = math.radians(end_angle - 90)
        
        r = radius * lengths[i]
        
        x1 = center_x + r * math.cos(start_rad)
        y1 = center_y + r * math.sin(start_rad)
        x2 = center_x + r * math.cos(end_rad)
        y2 = center_y + r * math.sin(end_rad)
        
        # Path command for a wedge
        # M center_x,center_y L x1,y1 A r,r 0 0,1 x2,y2 Z
        path_d = f"M {center_x},{center_y} L {x1},{y1} A {r},{r} 0 0,1 {x2},{y2} Z"
        
        dwg.add(dwg.path(d=path_d, fill=colors[i], opacity=0.8, stroke="white", stroke_width=2))

    # Add Initials SW
    # dwg.add(dwg.text('SW', insert=(center_x, center_y), fill='black', 
    #                  font_size='40px', font_family='Arial', font_weight='bold', 
    #                  text_anchor='middle', dominant_baseline='middle'))
    
    # Place initials in the center with a white background circle for readability
    dwg.add(dwg.circle(center=(center_x, center_y), r=25, fill='white', opacity=0.9))
    dwg.add(dwg.text('SW', insert=(center_x, center_y + 5), fill='#333', 
                     font_size='24px', font_family='sans-serif', font_weight='bold', 
                     text_anchor='middle', dominant_baseline='middle'))

    dwg.save()

if __name__ == '__main__':
    create_logo('Nightingale_digiter_project/assets/logo.svg')
