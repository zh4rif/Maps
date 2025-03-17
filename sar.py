import tkinter as tk
from tkinter import filedialog
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_shapefile():
    file_path = filedialog.askopenfilename(filetypes=[("Shapefiles", "*.shp")])
    if not file_path:
        return
    
    global gdf
    gdf = gpd.read_file(file_path)
    plot_shapefile()

def plot_shapefile():
    ax.clear()
    gdf.plot(column='displacement', cmap='jet', legend=True, ax=ax)
    ax.set_title("InSAR Displacement Data")
    canvas.draw()

# Create main window
root = tk.Tk()
root.title("InSAR Data Viewer")
root.geometry("800x600")

# Create a frame for buttons
frame = tk.Frame(root)
frame.pack(pady=10)

load_button = tk.Button(frame, text="Load Shapefile", command=load_shapefile)
load_button.pack()

# Create Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()