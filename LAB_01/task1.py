import math

hr_resolution = int(input("Enter horizontal resolution (pixels): "));
vr_resolution = int(input("Enter vertical resolution (pixels): "));
physical_diagonal_size = float(input("Enter physical diagonal size (inches): "))
total_pixel_count = hr_resolution * vr_resolution;
DPI = math.sqrt(hr_resolution ** 2 + vr_resolution ** 2) / physical_diagonal_size

def get_ratio(a,b):
    divisor = math.gcd(a,b)

    simplified_a = a // divisor
    simplified_b = b // divisor

    return f"{simplified_a}:{simplified_b}"


print("--- DISPLAY METRICS ANALYSIS ---");
print(f"Total Pixel Count : {total_pixel_count} pixels");
print("Aspect Ratio : ", get_ratio(hr_resolution, vr_resolution))
print(f"Calculated DPI : {round(DPI, 2)} DPI")
if DPI < 100:
    print("Density Category : Low Density (Standard Monitor)")
elif DPI <= 200:
    print("Density Category : Medium Density (HD Display)")
else:
    print("Density Category : High Density (Retina / Mobile)")


    