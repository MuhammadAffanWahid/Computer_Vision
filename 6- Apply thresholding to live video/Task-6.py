import cv2
import numpy as np
from PIL import Image

def threshold_channel(image):
    h, w = 300, 600
    image = np.asarray(image)
    face = image  # copying the img in face
    n = 40

    for x in range(h):
        for y in range(w):
            if image[x][y] < n:
                face[x][y] = 0
            else:
                face[x][y] = 255

    face = Image.fromarray(np.uint8(face))  # converting array back into a gray image
    pil_image = face.convert('RGB')
    face = np.array(pil_image)
    face = face[:, :, ::-1].copy()
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    return face


def threshold(img):
    new_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new_image = threshold_channel(new_image)  # apply thresholding on each channel
    return new_image  # open_cv_image #     # return the pixelated image


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()  # capture frame from webcam
    img = cv2.resize(img, (600, 300))  # resize the frame

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert bgr image to gray image
    cv2.imshow('original', img)  # display the captured frame
    img = threshold(img)

    cv2.imshow("output", img)  # show the image after making faces blur

    if cv2.waitKey(1) == ord('q'):  # exit if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows
cv2.waitKey(0)
