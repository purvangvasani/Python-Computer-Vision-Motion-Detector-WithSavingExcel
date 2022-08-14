import cv2
from PIL import Image

img = cv2.imread('download.jpeg', 0)


# img_resize = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
# cv2.imshow('Galaxy', img_resize)
# cv2.imwrite("galaxy_resize.jpg", img_resize)
# cv2.waitKey(3000)

scale_percent_1 = 500
width_1 = int(img.shape[1] * scale_percent_1 / 100)
height_1 = int(img.shape[0] * scale_percent_1 / 100)
dim_1 = (width_1, height_1)
scale_1 = cv2.resize(img, dim_1, interpolation = cv2.INTER_AREA)

# cv2.imshow("Scaled output image", scale_1)
cv2.imwrite("download_scaleUp.jpg", scale_1)
image_file = Image.open("download_scaleUp.jpg")
image_file.save("download_new.jpg", quality=95)
cv2.waitKey(3000)

# img_scale_up = cv2.resize(img, (0, 0), fx=2.5, fy=2.5)
# cv2.imshow('download', img_scale_up)
# cv2.imwrite("download_scaleUp.jpg", img_scale_up)
# cv2.waitKey(3000)

cv2.destroyAllWindows()