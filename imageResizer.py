import glob
import sys
import os
import cv2
read_images=glob.glob("*.jpg")

for i in read_images:
    width = 416
    height = 416
    dim = (width, height)
    img = cv2.imread(i, cv2.IMREAD_UNCHANGED)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(200)
    os.remove(i)
    cv2.imwrite(i,resized)