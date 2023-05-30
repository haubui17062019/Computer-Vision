from calendar import c
from queue import Empty
from turtle import width
import cv2
import numpy as np

'''
#đọc 
img = cv2.imread("12.jpg")
#kích thước ma trận 5x5, số nguyên không dấu 8 bit
kernel = np.ones((5, 5), np.uint8)
#màu xám
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#làm mờ
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
#vẽ bằng đường
imgCanny = cv2.Canny(img, 150, 200)
#giãn nở hình ảnh
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#xói mòn
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#hiện thị ảnh
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Cannon Image", imgCanny)
cv2.imshow("Dialtaion Image", imgDialation)
cv2.imshow("Eroded  Image", imgEroded)
#độ trễ, thời gian hiển thị
cv2.waitKey(0)


####################
#mở webcam 
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100) #độ sáng
while True:
    #lưu tất cả ảnh trong biến img, 
    success, img = cap.read()
    cv2.imshow("Video", img)
    #dừng lại
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

######################################
#tọa độ trong ảnh, thay đổi kích thước ảnh
img = cv2.imread("12.jpg")
#đặt kích cỡ cho ảnh
imgResize = cv2.resize(img, (400, 500))
#in ra kích thước
print(img.shape)
#in ra 1 phần của ảnh
imgCropped = img[0: 200, 200:500]
cv2.imshow("Image", img)
cv2.imshow("imgResize", imgResize)
img = cv2.imread("12.jpg")
cv2.waitKey(0)

#################
#SHAPE VÀ TEXT
#tạo 1 ảnh đen
img = np.zeros((512, 512, 3), np.uint8)
print(img)
#tô màu = xanh
#img[200:300, 100:300] = 255, 0,0
#vẽ đường
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 1)
#vẽ hình chữ nhật
cv2.rectangle(img,(0,0),(250,350), (0,0,255), 3, cv2.FILLED)
#vẽ đường tròn
cv2.circle(img, (200, 200), 30, (0,0,255), 1)
#thêm chữ (kích cỡ chữ)
cv2.putText(img, "Opencv ", (300, 300), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image", img)
cv2.waitKey(0)

#############
#CẮT MỘT PHẦN CỦA ẢNH
img = cv2.imread("12.jpg")
width, height = 250, 350
#khai báo 4 điểm để cắt
pts1 =np.float32([[0,219],[287,188],[154,482],[352,440]])
pts2 =np.float32([[0,0],[width, 0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)


##############
#GHÉP ẢNH VÀO 1 TẤM
img = cv2.imread("12.jpg")
#ghép ngang
imghor = np.hstack((img, img))
#ghép dọc
imgVer = np.vstack((img, img))
cv2.imshow("Hor", imghor)
cv2.waitKey(0)


########
#Đè màu
def empty(a):
    pass
path = '12.jpg'
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 240)
cv2.createTrackbar("Hue min", "trackbars", 0, 179, empty)
cv2.createTrackbar("Hue max", "trackbars", 179, 179, empty)
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "trackbars")
    print(h_min, h_max)
    lower = np.array(h_min)
    upder = np.array(h_max)
    mask = cv2.inRange(imgHSV, lower, upder)
    cv2.imshow("original", img)
    cv2.imshow("hsv", imgHSV)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
'''

##########
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('hau.jpg')
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0,0),2)





cv2.imshow("original", img)
cv2.waitKey(0)
