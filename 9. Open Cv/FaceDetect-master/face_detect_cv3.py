import cv2
import sys
# Get user supplied values
imagePath = "9. Open Cv/FaceDetect-master/curso.png"
cascPath = "9. Open Cv/FaceDetect-master/haarcascade_frontalface_default.xml"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
print("Found {0} faces!".format(len(faces)))
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, 'Face', (x,y-10), 2, 0.7,(255,0,0),2,cv2.LINE_AA)
cv2.imshow("Faces found", image)
key=cv2.waitKey(0)

