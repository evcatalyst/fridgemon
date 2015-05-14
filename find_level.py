# import the necessary packages
from pyimagesearch import imutils
from skimage import exposure
import numpy as np
import argparse
import cv2
import math
from matplotlib import pyplot as plt


# construct the arugment parser and parse the arugments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
args = vars(ap.parse_args())

# load the query image, compute the ration of the old height
# to the new height, clone it, and resize it
image = cv2.imread(args["query"], 0)

### rotating and image using python and opencv
## grab the dimensions of the image and calculate the center
## of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

## rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("rotated", rotated)
#cv2.waitKey(0)


#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#cl1 = clahe.apply(img)

#cv2.imshow("output",cl1)
#cv2.waitKey(0)




gray = rotated
edged = cv2.Canny(gray, 10, 12)

lines = cv2.HoughLinesP(edged, 1, math.pi/1, 20, None, 2, 480);


dot1 = (lines[0][0][0], lines[0][0][1])
dot2 = (lines[0][0][2], lines[0][0][3])
cv2.line(rotated, dot1, dot2, (255,0,0), 3)
#cv2.imshow("output", rotated)

#cv2.imshow("lines", edged)
cv2.imwrite("fileout.jpg", edged)


length = lines[0][0][1] - lines[0][0][3]
print (length)
#cv2.waitKey(0)
