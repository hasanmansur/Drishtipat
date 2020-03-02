import cv2 as cv
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

img = cv.imread("./ST2MainHall4/ST2MainHall4001.jpg")

imgDiffX = cv.Sobel(img, cv.CV_32F, 1, 0)
imgDiffY = cv.Sobel(img, cv.CV_32F, 0, 1)

imgDiffXY = cv.multiply(imgDiffX, imgDiffY)
imgDiffXX = cv.multiply(imgDiffX, imgDiffX)
imgDiffYY = cv.multiply(imgDiffY, imgDiffY)

a = imgDiffXX[:,:,0] + imgDiffXX[:,:,1] + imgDiffXX[:,:,2]
b = imgDiffXY[:,:,0] + imgDiffXY[:,:,1] + imgDiffXY[:,:,2]
c = imgDiffYY[:,:,0] + imgDiffYY[:,:,1] + imgDiffYY[:,:,2]

b_square = b * b
ac = a * c
a_plus_c = a + c
a_plus_c_square = a_plus_c * a_plus_c
lambda1 = ((a_plus_c + np.sqrt(a_plus_c_square - 4 * (b_square - ac))))/2
lambda2 = ((a_plus_c - np.sqrt(a_plus_c_square - 4 * (b_square - ac))))/2

print("lambda1",lambda1)
#print("lambda2",lambda2)

a_minus_lambda1 = a - lambda1
b_neg = b * (-1)
x = b_neg / a_minus_lambda1
#print(x.shape)

bgr_angle_degree = (np.arctan2(1, x) * 180 / np.pi) + 360
bgr_angle_final = np.rint((bgr_angle_degree % 360)/10)
bgr_angle_final[np.isnan(bgr_angle_final)] = 0
#print(bgr_angle_final)







'''
J11 = imgDiffXX
J22 = imgDiffYY
J12 = imgDiffXY
#print(J12.shape)
# GST components calculations (stop)
# eigenvalue calculation (start)
# lambda1 = J11 + J22 + sqrt((J11-J22)^2 + 4*J12^2)
# lambda2 = J11 + J22 - sqrt((J11-J22)^2 + 4*J12^2)
tmp1 = J11 + J22
tmp2 = J11 - J22
tmp2 = cv.multiply(tmp2, tmp2)
tmp3 = cv.multiply(J12, J12)
tmp4 = np.sqrt(tmp2 + 4.0 * tmp3)
lambda1 = tmp1 + tmp4    # biggest eigenvalue
lambda2 = tmp1 - tmp4    # smallest eigenvalue
print(lambda2.shape)
# eigenvalue calculation (stop)
# Coherency calculation (start)
# Coherency = (lambda1 - lambda2)/(lambda1 + lambda2)) - measure of anisotropism
# Coherency is anisotropy degree (consistency of local orientation)
imgCoherencyOut = cv.divide(lambda1 - lambda2, lambda1 + lambda2)
# Coherency calculation (stop)
# orientation angle calculation (start)
# tan(2*Alpha) = 2*J12/(J22 - J11)
# Alpha = 0.5 atan2(2*J12/(J22 - J11))
imgOrientationOut = cv.phase(J22 - J11, 2.0 * J12, angleInDegrees = True)
imgOrientationOut = 0.5 * imgOrientationOut
# orientation angle calculation (stop)
'''
