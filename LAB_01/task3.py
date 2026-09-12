import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("sample.jpg").convert("RGB")

img = np.array(image)

red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", img.shape)

print(
    f"Red Channel 2D Shape : {red.shape} | "
    f"Mean Intensity: {red.mean():.2f}"
)

print(
    f"Green Channel 2D Shape: {green.shape} | "
    f"Mean Intensity: {green.mean():.2f}"
)

print(
    f"Blue Channel 2D Shape : {blue.shape} | "
    f"Mean Intensity: {blue.mean():.2f}"
)

plt.figure(figsize=(12, 7))

plt.subplot(2, 3, 1)
plt.imshow(red_only)
plt.title("Red-Only")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(green_only)
plt.title("Green-Only")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blue_only)
plt.title("Blue-Only")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(red, cmap="gray")
plt.title("Red Intensity")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(green, cmap="gray")
plt.title("Green Intensity")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(blue, cmap="gray")
plt.title("Blue Intensity")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered")