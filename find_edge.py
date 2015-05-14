# import the necessary packages
from pyimagesearch import imutils
from skimage import exposure
import numpy as np
import argparse
import cv2


# construct the arugment parser and parse the arugments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
args = vars(ap.parse_args())

# load the query image, compute the ration of the old height
# to the new height, clone it, and resize it
image = cv2.imread(args["query"])
#ratio = image.shape[0] / 300.0
#orig = image.copy()
#image = imutils.resize(image, height = 300)

# convert the image to greyscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#gray = cv2.bilateralFilter(gray, 11, 17, 17)

blur = cv2.GaussianBlur(gray, (5,5), 0)
gray = blur
edged = cv2.Canny(gray, 15, 15, apertureSize = 3)

#lines = cv2.HoughLines(edged, 1, np.pi/180, 200)

#for (rho, theta) in lines[:1]:
#	a = np.cos(theta)
#	b = np.sin(theta)
#	x0 = a*rho
#	y0 = b*rho
#	x1 = int(x0 + 1000*(-b))
#	y1 = int(y0 + 1000*(a))
#	x2 = int(x0 - 1000*(-b))
#	y2 = int(y0 - 1000*(a))
#
#	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("edged", edged)
cv2.waitKey(0)
