import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
image = Image.open("sample.jpg").convert("RGB")
img = np.array(image)

# Downsampling factor
N = 8

# Original dimensions and memory
original_shape = img.shape
original_memory = img.nbytes

# 1. Downsample using NumPy striding
downsampled = img[::N, ::N, :]

# 2. Re-expand using np.repeat()
expanded = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N,
    axis=1
)

# Make sure expanded image has the same dimensions as original
expanded = expanded[:img.shape[0], :img.shape[1], :]

# 3. Calculate reductions

# Reduction per spatial axis
height_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
width_reduction = (1 - downsampled.shape[1] / img.shape[1]) * 100

# Memory reduction
memory_savings = (
    1 - downsampled.nbytes / original_memory
) * 100

# Print results
print("--- DOWNSAMPLING ANALYSIS (N = 8) ---")

print(
    f"Original Shape     : {original_shape} | "
    f"Memory: {original_memory:,} bytes"
)

print(
    f"Downsampled Shape   : {downsampled.shape} | "
    f"Memory: {downsampled.nbytes:,} bytes"
)

print(
    f"Re-expanded Shape   : {expanded.shape} | "
    f"Visual: Blocky Pixelation"
)

print(
    f"Dimension Reduction : {height_reduction:.2f}% "
    f"reduction per axis"
)

print(
    f"Memory Savings      : {memory_savings:.2f}% data reduction"
)

# Display original and pixelated images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(expanded)
plt.title("Pixelated Image (N=8)")
plt.axis("off")

plt.tight_layout()
plt.show()