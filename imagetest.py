#improt the necessary packages
import cv2


#load the image and show it
#image = cv2.imread("milk_01.jpg")
image = cv2.imread("IMG_115.TIFF")

### loading and displaying an image
## open image - when type "0" close image
cv2.imshow("original", image)
cv2.waitKey(0)

### getting the dimensions of the image
## output the shape of the image - columns, rows, channels
#print image.shape


### resizing an image using python and opencv
## we need to keep in mind aspect ratio so the image does
## not look skewed or distorted -- therefore, we calculate
## the ratio of the new image to the old image

#r = 100.00 / image.shape[1]
#dim = (100, int(image.shape[0] * r))

## perform the actual resizing of the image and show it
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("resized", resized)
#cv2.waitKey(0)


### rotating and image using python and opencv
## grab the dimensions of the image and calculate the center
## of the image
#(h, w) = image.shape[:2]
#center = (w / 2, h / 2)

## rotate the image by 180 degrees
#M = cv2.getRotationMatrix2D(center, 180, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("rotated", rotated)
#cv2.waitKey(0)

### saving an image to disk using python and opencv
#cv2.imwrite("thumbnail.png", rotated)

