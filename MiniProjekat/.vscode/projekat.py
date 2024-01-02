import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tqdm.notebook

he_image = cv2.imread("HE.tif", cv2.IMREAD_GRAYSCALE)
le_image = cv2.imread("LE.tif", cv2.IMREAD_GRAYSCALE)

# Primena Sobel filtera
sobel_he = cv2.Sobel(he_image, cv2.CV_64F, 1, 1, ksize=5)
sobel_le = cv2.Sobel(le_image, cv2.CV_64F, 1, 1, ksize=5)

# Pronalaženje kontura
contours_he, _ = cv2.findContours(np.uint8(sobel_he), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_le, _ = cv2.findContours(np.uint8(sobel_le), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
graylevel=np.arrange(255)
# Poređenje kontura i označavanje stranih tela
for contour_he in contours_he:
    for contour_le in contours_le:
        # Poređenje kontura, na primer, po veličini
        if cv2.contourArea(contour_he) - cv2.contourArea(contour_le) > threshold:
            # Crtanje pravougaonika oko detektovanog stranog tela
            x, y, w, h = cv2.boundingRect(contour_le)
            cv2.rectangle(le_image, (x, y), (x + w, y + h), 0, -1)  # Označavanje crnom bojom




# Prikaz rezultata

plt.subplot(1, 2, 1), plt.imshow(he_image, cmap='gray'), plt.title('HE Image')
plt.subplot(1, 2, 2), plt.imshow(le_image, cmap='gray'), plt.title('LE Image with Detected Foreign Objects')
plt.show()