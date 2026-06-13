import tifffile as tiff
import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt

# Load 3D image
volume = tiff.imread("sample.tif")

print("Volume shape:", volume.shape)

# Create PyVista ImageData
grid = pv.ImageData()

# PyVista expects dimensions in x,y,z order
grid.dimensions = (
    volume.shape[2],
    volume.shape[1],
    volume.shape[0]
)

# Add voxel values
grid.point_data["Intensity"] = volume.flatten(order="F")

# Create plotter
plotter = pv.Plotter()

# Volume rendering
plotter.add_volume(
    grid,
    cmap="gray",
    opacity="sigmoid"
)

plotter.add_axes()
plotter.show_grid()

plotter.show()
#visualizing a single slice
volume = tiff.imread("sample.tif")

middle_slice = volume.shape[0] // 2

plt.imshow(volume[middle_slice], cmap='gray')
plt.title(f"Slice {middle_slice}")
plt.colorbar()
plt.show()