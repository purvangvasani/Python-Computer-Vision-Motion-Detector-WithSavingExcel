import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 1)
    img_resize = cv2.resize(img, (100, 100))
    cv2.imshow('New', img_resize)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    cv2.imwrite("resize_"+image, img_resize)