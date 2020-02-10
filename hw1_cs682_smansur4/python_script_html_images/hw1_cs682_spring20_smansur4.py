import argparse
import cv2
import numpy as np
import copy

# parsing the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", required = True, help = "path to the image")
args = vars(ap.parse_args())
destination_dir = "./"

#------------------------prob2: BGR and GRAYSCALE-------------------------------
# BGR
image_path = args["i"]
image = cv2.imread(image_path)
#cv2.imshow("BGR", image)
#cv2.waitKey(0)

# BGR to GRAYSCALE
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("GRAY", gray)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "gray.jpeg", gray)

#------------------------prob3: transformations----------------------------------
(image_width, image_height) = (image.shape[1], image.shape[0])

#translation
x_shift = 100
y_shift = 50
transformation_matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
shifted = cv2.warpAffine(image, transformation_matrix, (image_width, image_height))
#cv2.imshow("Shifted Right & Down", shifted)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "translated_right_down.jpeg", shifted)

#rotation
center = (image_width // 2, image_height // 2)
angle = 270
scale = 1.0
transformation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(image, transformation_matrix, (image_width, image_height))
#cv2.imshow("270 Rotated", rotated)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "rotated_270.jpeg", rotated)

#flipping/reflection
flipped = cv2.flip(gray, 0)
#cv2.imshow("Vertical Flip", flipped)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "vertical_flipped.jpeg", flipped)

#resizing/scaling
dim = (2 * image_width, 2 * image_height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
#cv2.imshow("Double Sized", resized)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "double_sized.jpeg", resized)

# horizontal shear
shear_M = np.float32([[1, 0.5, 0], [0, 1, 0]])
hor_sheared = cv2.warpAffine(gray,shear_M,(image_width, image_height))
#cv2.imshow("Horizontal Shear", hor_sheared)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "horizontal_sheared.jpeg", hor_sheared)

# blurring
blurred = cv2.blur(image,(10,10))
#cv2.imshow("Blurred", blurred)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "blurred.jpeg", blurred)

# color space change
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", hsv)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "hsv.jpeg", hsv)

#------------------------prob4: Gaussian Pyramid--------------------------------
images_list = []
image_Gi = cv2.imread(image_path)
while True:
    (image_width, image_height) = (image_Gi.shape[1], image_Gi.shape[0])
    #cv2.imshow("originial image", image_Gi)
    image_sample = copy.deepcopy(image_Gi)
    images_list.append(image_sample)
    #key = cv2.waitKey(0)
    #if key == 27:
        #break
    if image_width == 1 and image_height == 1:
        break
    else:
        image_Gi = cv2.pyrDown(image_Gi, dstsize=(image_width // 2, image_height // 2))
images_list.reverse()
total_height = 0
width_list = []
for image in images_list:
    total_height += image.shape[0]
    width_list.append(image.shape[1])
max_width = max(width_list)
print("total_height:", total_height)
print("max_width:", max_width)
composite_image = np.zeros(shape=(total_height, max_width, 3), dtype="uint8")
height_offset = 0
for image in images_list:
    composite_image[height_offset:height_offset+image.shape[0], :image.shape[1]] = image[:]
    height_offset = height_offset + image.shape[0]
#cv2.imshow("pyramid image", composite_image)
#cv2.waitKey(0)
cv2.imwrite(destination_dir + "pyramid.jpeg", composite_image)
