import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# using grayscale images to better performance and detecting
img = cv2.imread('news.jpg')
# use cvtColor to convert img into grayscale
gs_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gs_img,
                                      scaleFactor=1.1,
                                      minNeighbors=10)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

print(type(faces))
print(faces)

resize = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
