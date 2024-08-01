import cv2

#  Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# COPY THE PATH OF YOU IMAGE HERE
# PLEASE REPLACE THIS PATH WITH PATH OF AN IMAGE IN YOUR OWN DEVICE
img = cv2.imread("C:\\Users\\Pratyush Kala\\OneDrive\\Desktop\\jravis.jpg")

# Convert image to grayscale
graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
face = face_cascade.detectMultiScale(graysc, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Drawing rectangles around the detected faces
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# result
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
