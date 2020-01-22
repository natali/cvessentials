# import stuff
import cv2
import numpy as nm

# imread = image read, specifiy the path

img = cv2.imread("assets/mommy.jpg")
img2 = cv2.imread("assets/mommy.jpg", flags=0)

# convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img)
print(img2)
# print (row, column, channel) of image
print(img.shape)


# imshow = image show
cv2.imshow("Original", img)

# wait for key event
cv2.waitKey(0)