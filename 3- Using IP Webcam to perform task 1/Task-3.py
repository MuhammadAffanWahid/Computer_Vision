from urllib.request import urlopen
import cv2
import numpy as np
url='http://172.16.20.202:8080/shot.jpg'

#url='http://192.168.1.4:8080/shot.jpg'

i=0
while True:
    imgResp = urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('Image',cv2.resize(img,(600,300)))             # displaying live video
    q=cv2.waitKey(1)                                          # 1 milli second wait
    if(q==ord('c')):                                          # if 'c' is pressed
        cv2.imwrite('./img_'+str(i)+'.jpg',img)               # save the image

        img = cv2.resize(img, (600, 300))    # resizing the image
        b, g, r = cv2.split(img)             # splitting the colored image into its channels
        cv2.imshow("Red Channel", r)         # displaying red channel
        cv2.imshow("Green Channel", g)       # displaying green channel
        cv2.imshow("Blue Channel", b)        # displaying blue channel

        img_swapped = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # swapping red and blue color
        cv2.imshow("Swapped Image", img_swapped)            # displaying the colored image

        i=i+1                        # increment i for naming next image
    if q==ord('q'):                  # if 'q' is pressed
        break                        # quit program

cv2.destroyAllWindows()              # closing all opened windows

