import cv2
from PIL import Image

source = './source/3.jpg'
image = Image.open(source)
resized_image = image.resize((450, 450))

color_image = cv2.imread(resized_image)

# cv2.imshow("3", color_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

cartoon_image1, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
cv2.imshow('pencil', cartoon_image2)
cv2.waitKey()
cv2.destroyAllWindows()