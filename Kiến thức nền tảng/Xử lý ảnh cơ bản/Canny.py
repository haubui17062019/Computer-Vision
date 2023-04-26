import cv2

img1 = cv2.imread('anh1.jpg')
img = cv2.medianBlur(img1, 3)
edges = cv2.Canny(img, 100, 200)
cv2.imshow('img_org', img)
cv2.imshow('edges', edges)
cv2.waitKey(0)