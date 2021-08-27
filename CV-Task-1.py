import cv2

img_path = "resources/red.jpg"                 # saving image path
img = cv2.imread(img_path)                      # reading the image in img variable
img = cv2.resize(img, (600,300))               # resizing the image in img variable

b, g, r = cv2.split(img)                        # splitting the colored image into red, green and blue channels
cv2.imshow("Red Channel", r)                    # displaying red channel
cv2.imshow("Green Channel", g)                  # displaying green channel
cv2.imshow("Blue Channel", b)                   # displaying blue channel

img_merge = cv2.merge([b, g, r])                # merging the red, green and blue channels into a colored image
cv2.imshow("Merged Image", img_merge)                  # displaying the colored image

img_swapped = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # swapping red and blue color
cv2.imshow("Swapped Image", img_swapped)        # displaying the colored image

cv2.waitKey(0)                                  # adding wait of 10 seconds
cv2.destroyAllWindows()                         # closing all the opened windows
