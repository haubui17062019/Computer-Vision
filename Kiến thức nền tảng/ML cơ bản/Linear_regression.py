#giải quyết bài toán có đầu ra là giá trị thực
#ví dụ: dự đoán giá nhà, dự đoán giá cổ phiếu, dự đoán tuổi,...

from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# regr = linear_model.LinearRegression(fit_intercept=False)
# regr.fit(Xbar, y)
# a = regr.coef_
# w0 = a[0][0]
# w1 = a[0][1]
#hàm tính
# y = w0 + w1*x0

# 1. training: tìm đường thẳng (model) gần các điểm nhất
# import numpy as np
# from sklearn.linear_model import LinearRegression
# x = [2104, 1416, 1534, 852]
# y = [460, 232, 315, 178]
# x = np.asarray(x)
# y = np.asarray(y)
# model = LinearRegression()
# model.fit(x.reshape(-1,1), y.reshape(-1,1))
# w, b = model.coef_[0][0], model.intercept_[0]
# sol_sklean = np.array([b,w])
# print(sol_sklean)

# def estimate_coef(x, y):
#   # number of observations/points
#   n = np.size(x)
#   # mean of x and y vector
#   m_x, m_y = np.mean(x), np.mean(y)
#   # calculating cross-deviation and deviation about x
#   SS_xy = np.sum(y * x) - n * m_y * m_x
#   SS_xx = np.sum(x * x) - n * m_x * m_x
#   print(np.sum(y * x))
#   # calculating regression coefficients
#   b_1 = SS_xy / SS_xx
#   b_0 = m_y - b_1 * m_x
#   return (b_0, b_1)

#######################
# import numpy as np
# x = np.array([[2104, 1416, 1534, 852]]).T
# # weight (kg)
# y = np.array([[460, 232, 315, 178]]).T
# print(x, y)
# one = np.ones((x.shape[0], 1))
# Xbar = np.concatenate((one, x), axis = 1)
# A = np.dot(Xbar.T, Xbar)
# b = np.dot(Xbar.T, y)
# w = np.dot(np.linalg.pinv(A), b)
# print(w)

####################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

x = [2104, 1416, 1534, 852]
y = [460, 232, 315, 178]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
print(mymodel)
plt.scatter(x, y)
print(myfunc(50), myfunc(40), myfunc(1000))
plt.plot(x, mymodel)
plt.show()
x = np.asarray(x) # thành ma trận
print(x)
xmean = np.mean(x, None) #trung bình
print(xmean)

