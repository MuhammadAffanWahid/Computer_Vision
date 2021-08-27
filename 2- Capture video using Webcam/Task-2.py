import cv2                                      # importing cv2 library
vid = cv2.VideoCapture(0)                       # making a video capture object
while (True):                                   # running an infinite loop
    ret, frame = vid.read()                     # reading frames from the object
    cv2.imshow('frame', frame)                  # displaying the frames captured
    if cv2.waitKey(1) & 0xFF == ord('e'):       # if 'e' is pressed break the
        break                                   # infinite loop
vid.release()                                   # unlocking the video capture object
cv2.destroyAllWindows()                         # closing all the opened windows
