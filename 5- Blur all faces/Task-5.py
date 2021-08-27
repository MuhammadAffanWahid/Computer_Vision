import cv2
import numpy as np
from PIL import Image

def pixelate(img,a,b,w,h):
    img = np.asarray(img)                   # convert image into an array

    face = img                              # copying the img in face
    for x in range(b, b + h):
        for y in range(a, a + w):
            face[x][y] = img[b+(int((x-(b))/10)*10)][a+(int((y-a)/10)*10)]    # convert 10 pixel into 1 pixels

    face = Image.fromarray(np.uint8(face))  # converting array back into a gray image
    pil_image = face.convert('RGB')
    face = np.array(pil_image)
    face = face[:, :, ::-1].copy()
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    return face

def blur(img,x,y,w,h):
    b, g, r = cv2.split(img)                # split image into its channels

    b = pixelate(b, x, y, w, h)             # pixelate each channel
    g = pixelate(g, x, y, w, h)
    r = pixelate(r, x, y, w, h)
    new_image = cv2.merge([b, g, r])        # merge pixelated channels in to a bgr pixelated image

    return new_image  # open_cv_image #     # return the pixelated image

faces = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture( 0)

while True:
    _,img = cap.read()                      # capture frame from webcam
    img = cv2.resize(img, (600,300))        # resize the frame

    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert bgr image to gray image
    detections = faces.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=3) # detect all the faces in the frame
    cv2.imshow('original',img)              # display the captured frame

    for(x,y,w,h) in detections:             # take each face detected in the frame
        img = blur(img,x,y,w,h)             # and make it blur

    cv2.imshow("output",img)                # show the image after making faces blur

    if cv2.waitKey(1) == ord('q'):          # exit if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()                     # destroy all the opened windows
