import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read image as grayscale
img = cv2.imread('imagee.jpeg', cv2.IMREAD_GRAYSCALE)

# Checking dimensions
print("Image shape:", img.shape)

# Display of image
plt.figure(figsize=(6,6))
plt.imshow(img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

