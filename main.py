import cv2
import numpy as np
from PIL import Image
import scipy

def greyscale(img):
   greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # New grayscale image = ( (0.3 * R) + (0.59 * G) + (0.11 * B) ).
   return greyscale

def bright(img, beta_value ):
   img_bright = cv2.convertScaleAbs(img, beta=beta_value)
   return img_bright

def sharpen(img):
   kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
   img_sharpen = cv2.filter2D(img, -1, kernel)
   return img_sharpen

def invert(img):
   inv = cv2.bitwise_not(img)
   return inv

def filter(img):
   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   img = np.asarray(img)

   cols,rows=683,384
   matrix = [[1,1,1],[1,1,1],[1,1,1]]
   filtered = [[0] * cols for i in range(rows)]
   for x in range(rows):
       for y in range(cols):
           if (x > 0 and x < rows-1) and (y>0 and y<cols-1):
               filtered[x][y]= (((matrix[0][0]*img[x-1][y-1])+(matrix[0][1]*img[x-1][y])+(matrix[0][2]*img[x-1][y+1])+(matrix[1][0]*img[x][y-1])+(matrix[1][1]*img[x][y])+(matrix[1][2]*img[x][y+1])+(matrix[2][0]*img[x+1][y-1])+(matrix[2][1]*img[x+1][y])+(matrix[2][2]*img[x+1][y+1])))/9
   new_image = Image.fromarray(np.uint8(filtered))

   pil_image = new_image.convert('RGB')
   open_cv_image = np.array(pil_image)
   open_cv_image = open_cv_image[:, :, ::-1].copy()

   return open_cv_image

def grayscale(img):
   b, g, r = cv2.split(img)

   b_array = np.asarray(b)
   g_array = np.asarray(g)
   r_array = np.asarray(r)

   cols, rows = 683, 384
   filtered = [[0] * cols for i in range(rows)]
   for x in range(rows):
       for y in range(cols):
           if (x > 0 and x < rows - 1) and (y>0 and y<cols-1):
               filtered[x][y] = (0.299*b_array[x][y]+0.587*g_array[x][y]+0.114*r_array[x][y])
   new_image = Image.fromarray(np.uint8(filtered))

   pil_image = new_image.convert('RGB')
   open_cv_image = np.array(pil_image)
   open_cv_image = open_cv_image[:, :, ::-1].copy()
   return open_cv_image


def filter_gray(img,filter=0):
   img = np.asarray(img)
   if filter > 0:
       img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   cols,rows=683,384
   if filter == -1:
       matrix = [[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]]
   if filter==0:
       matrix = [[1,1,1],[1,1,1],[1,1,1]]
   if filter==1:
       matrix = [[1,0,-1],[2,0,2],[1,0,-1]]
   if filter==2:
       matrix = [[1,2,1],[0,0,0],[-1,-2,-1]]
   if filter == 3:
       matrix = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
   filtered = [[0] * cols for i in range(rows)]
   for x in range(rows):
       for y in range(cols):
           if (x > 0 and x < rows-1) and (y>0 and y<cols-1):
               filtered[x][y]= (((matrix[0][0]*img[x-1][y-1])+(matrix[0][1]*img[x-1][y])+(matrix[0][2]*img[x-1][y+1])+(matrix[1][0]*img[x][y-1])+(matrix[1][1]*img[x][y])+(matrix[1][2]*img[x][y+1])+(matrix[2][0]*img[x+1][y-1])+(matrix[2][1]*img[x+1][y])+(matrix[2][2]*img[x+1][y+1])))/9
   new_image = Image.fromarray(np.uint8(filtered))

   pil_image = new_image.convert('RGB')
   open_cv_image = np.array(pil_image)
   open_cv_image = open_cv_image[:, :, ::-1].copy()

   open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
   return open_cv_image


def filter_averaging(img,f=0):
   b, g, r = cv2.split(img)

   b = filter_gray(b,f)
   g = filter_gray(g,f)
   r = filter_gray(r,f)
   new_image = cv2.merge([b, g, r])
   return new_image #open_cv_image #

def filter_edge_detect(img,type):

   new_image = filter_gray(filter_averaging(img),type)

   return new_image #open_cv_image #



#mode = cv2.waitKey(10000)
mode = input("Select Mode: ")

if mode == 'image':
   file_name='Filtered'
   flag =0


   while True:
       frame = cv2.imread('cube.jpg')
#        frame = cv2.imread('math.jpg')
       frame = cv2.resize(frame, (683, 384))

       cv2.imshow( 'Original', frame)
       q = cv2.waitKey(0)

       if q == ord('f'):
           if flag != 1:
               flag = 1
           else:
               flag = 0
       elif q == ord('g'):
           if flag != 2:
               flag = 2
           else:
               flag = 0
       elif q == ord('m'):
           if flag != 3:
               flag = 3
           else:
               flag = 0
       elif q == ord('l'):
           if flag != 4:
               flag = 4
           else:
               flag = 0
       elif q == ord('s'):
           if flag != 5:
               flag = 5
           else:
               flag = 0
       elif q == ord('i'):
           if flag != 6:
               flag = 6
           else:
               flag = 0
       elif q == ord('a'):
           if flag != 7:
               flag = 7
           else:
               flag = 0
       elif q == ord('h'):
           if flag != 8:
               flag = 8
           else:
               flag = 0
       elif q == ord('v'):
           if flag != 9:
               flag = 9
           else:
               flag = 0
       elif q == ord('k'):
           if flag != 10:
               flag = 10
           else:
               flag = 0
       else:
           flag=0

       if flag == 1:
           frame = filter(frame)
       elif flag == 2:
           frame = greyscale(frame)
       elif flag == 3:
           frame = bright(frame,80)
       elif flag == 4:
           frame = bright(frame,-50)
       elif flag == 5:
           frame = sharpen(frame) #filter_averaging(frame,-1)#
       elif flag == 6:
           frame = invert(frame)
       elif flag == 7:
           frame = filter_averaging(frame)
       elif flag == 8:
           frame = filter_edge_detect(frame, 1)
       elif flag == 9:
           frame = filter_edge_detect(frame, 2)
       elif flag == 10:
           frame = filter_edge_detect(frame, 3)

       cv2.imshow( file_name, frame)
elif mode == 'video':
   image = cv2.VideoCapture(0)
   file_name = 'Live video'
   flag = 0

   while True:
       ret, frame = image.read()
       frame = cv2.resize(frame, (683, 384))
       cv2.imshow('Original', frame)
       q = cv2.waitKey(1)

       if q == ord('g'):
           if flag != 2:
               flag = 2
           else:
               flag = 0
       elif q == ord('m'):
           if flag != 3:
               flag = 3
           else:
               flag = 0
       elif q == ord('l'):
           if flag != 4:
               flag = 4
           else:
               flag = 0
       elif q == ord('s'):
           if flag != 5:
               flag = 5
           else:
               flag = 0
       elif q == ord('i'):
           if flag != 6:
               flag = 6
           else:
               flag = 0

       if flag == 1:
           frame = filter(frame)
       elif flag == 2:
           frame = greyscale(frame)
       elif flag == 3:
           frame = bright(frame, 80)
       elif flag == 4:
           frame = bright(frame, -50)
       elif flag == 5:
           frame = sharpen(frame)
       elif flag == 6:
           frame = invert(frame)

       cv2.imshow(file_name, frame)
       #cv2.destroyAllWindows()

cv2.destroyAllWindows()
