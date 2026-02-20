import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import Image
import json

class NightingaleAdvancedDigitizer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Nightingale Data Station")
        
        self.master_data = {} 
        self.current_group_name = "April 1854"
        self.coords = {"Origin": None, "Red": None, "Blue": None, "Black": None}
        
        self.history = [] 
        
        self.mode = "DIGITIZE"  
        self.img = Image.open(image_path)
        
        self.setup_ui()
        self.setup_canvas()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        self.left_panel = ttk.Frame(self.root, padding="10")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.btn_mode = ttk.Button(self.left_panel, text="Mode: Digitize (Crosshair)", command=self.toggle_mode)
        self.btn_mode.pack(fill=tk.X, pady=5)

        self.btn_undo = ttk.Button(self.left_panel, text="Undo (Ctrl+Z)", command=self.undo)
        self.btn_undo.pack(fill=tk.X, pady=5)

        self.lbl_mouse = ttk.Label(self.left_panel, text="Mouse: (0, 0)", font=('Courier', 10))
        self.lbl_mouse.pack(pady=10)

        self.status_labels = {}
        for cat in ["Origin", "Red", "Blue", "Black"]:
            lbl = ttk.Label(self.left_panel, text=f"{cat}: None")
            lbl.pack(anchor=tk.W)
            self.status_labels[cat] = lbl

        ttk.Button(self.left_panel, text="Save Group", command=self.save_to_dict).pack(pady=20)

    def setup_canvas(self):
        plt.rcParams['keymap.yscale'] = []
        plt.rcParams['keymap.xscale'] = []
        
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        self.ax.imshow(self.img)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.toolbar.pack_forget() 

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.canvas.mpl_connect('key_press_event', self.on_key)
        
        self.root.bind("<Control-z>", lambda event: self.undo())
        self.canvas.get_tk_widget().focus_set()

    def toggle_mode(self):
        if self.mode == "DIGITIZE":
            self.mode = "NAVIGATE"
            self.toolbar.pan() 
            self.btn_mode.config(text="Mode: Navigate (Pan/Zoom)")
        else:
            self.mode = "DIGITIZE"
            self.toolbar.pan() 
            self.btn_mode.config(text="Mode: Digitize (Crosshair)")
        self.canvas.get_tk_widget().focus_set()

    def on_move(self, event):
        if event.xdata and event.ydata:
            self.lbl_mouse.config(text=f"Mouse: ({int(event.xdata)}, {int(event.ydata)})")

    def on_key(self, event):
        if self.mode != "DIGITIZE": return
        
        key_map = {'r': 'Red', 'b': 'Blue', 'k': 'Black', 'o': 'Origin'}
        if event.key in key_map:
            cat = key_map[event.key]
            if event.xdata is not None:
                self.coords[cat] = [int(event.xdata), int(event.ydata)]
                self.status_labels[cat].config(text=f"{cat}: {self.coords[cat]}", font=('Arial', 9, 'bold'))
                
                color = 'red' if event.key=='r' else 'blue' if event.key=='b' else 'black' if event.key=='k' else 'orange'
                marker = 'x' if cat!='Origin' else 'o'
                
                line, = self.ax.plot(event.xdata, event.ydata, marker=marker, color=color)
                self.history.append((cat, line))
                self.canvas.draw()

    def on_click(self, event):
        self.canvas.get_tk_widget().focus_set()
        if event.xdata is None or event.ydata is None: return
        
        if self.mode == "DIGITIZE" and event.button == 1:
            cat = "Origin"
            self.coords[cat] = [int(event.xdata), int(event.ydata)]
            self.status_labels[cat].config(text=f"{cat}: {self.coords[cat]}", font=('Arial', 9, 'bold'))
            
            line, = self.ax.plot(event.xdata, event.ydata, 'yo', markersize=8)
            self.history.append((cat, line))
            self.canvas.draw()

    def undo(self):
        if not self.history:
            return
        
        cat, line = self.history.pop()
        
        line.remove()
        self.coords[cat] = None
        self.status_labels[cat].config(text=f"{cat}: None", font=('Arial', 9))
        
        self.canvas.draw()
        # print(f"Undone: {cat}")

    def save_to_dict(self):
        if not self.coords["Origin"]:
            messagebox.showwarning("Error", "Please set Origin first!")
            return
        
        group_id = f"Group_{len(self.master_data) + 1}"
        self.master_data[group_id] = {k: v for k, v in self.coords.items()}
        
        print(f"\n--- Group {group_id} Saved ---")
        
        for key in ["Red", "Blue", "Black"]:
            self.coords[key] = None
            self.status_labels[key].config(text=f"{key}: None", font=('Arial', 9))
        
        self.history.clear() 
        
        messagebox.showinfo("Success", f"Data saved to {group_id}.")
        self.canvas.get_tk_widget().focus_set()

    def export_to_json(self):
        if not self.master_data: return
        with open("digitized_data.json", "w") as f:
            json.dump(self.master_data, f, indent=4)

    def on_closing(self):
        if self.master_data:
            if messagebox.askyesno("Quit", "Export data to JSON?"):
                self.export_to_json()
        plt.close('all') 
        self.root.quit() 
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NightingaleAdvancedDigitizer(root, "Nightingale-mortality.jpg")
    root.mainloop()