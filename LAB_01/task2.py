import numpy as np

image = np.zeros((300, 400, 3), dtype=np.uint8)

image[0:150, 0:200] = [255, 0, 0]
image[0:150, 200:400] = [0, 255, 0]
image[150:300, 0:200] = [0, 0, 255]
image[150:300, 200:400] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", image.shape)
print("Data Type             :", image.dtype)
print("Total Elements        :", f"{image.size:,}", "values")
print("Memory Footprint      :", f"{image.nbytes:,}", "bytes", f"({image.nbytes / 1024:.2f})", "KB")

