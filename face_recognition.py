import cv2

face_patterns = cv2.CascadeClassifier('/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

sample_image = cv2.imread('/home/qbj/文档/3.face/face.jpg')

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('/home/qbj/文档/3.face/face.png', sample_image);