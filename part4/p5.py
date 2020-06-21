import numpy as np
import cv2 as cv
import glob
from matplotlib import pyplot as plt

def calculate_chamfer_dst(image):
    neighbor_pixel_dis = 1
    chamfer_dst = image.astype("float")
    # initialization
    chamfer_dst[chamfer_dst==0]=float("inf")
    chamfer_dst[chamfer_dst==255]=0
    #print("chamfer_dst after init", chamfer_dst)

    # forward pass
    for i in range(0, chamfer_dst.shape[0]):
        for j in range(0, chamfer_dst.shape[1]):
            pixel_center = chamfer_dst[i, j]

            f0 = float("inf") if(j - 1 < 0) else chamfer_dst[i, j - 1]
            f0_dis = neighbor_pixel_dis + f0

            f1 = float("inf") if(i - 1 < 0 or j - 1 < 0) else chamfer_dst[i - 1, j - 1]
            f1_dis = neighbor_pixel_dis + f1

            f2 = float("inf") if(i - 1 < 0) else chamfer_dst[i - 1, j]
            f2_dis = neighbor_pixel_dis + f2

            f3 = float("inf") if(i - 1 < 0 or j + 1 > chamfer_dst.shape[1] - 1) else chamfer_dst[i - 1, j + 1]
            f3_dis = neighbor_pixel_dis + f3

            chamfer_dst[i, j] = min(pixel_center, f0_dis, f1_dis, f2_dis, f3_dis)

    #print("chamfer_dst after forward pass", chamfer_dst)

    # backward pass
    for m in range(chamfer_dst.shape[0] - 1, -1, -1):
        for n in range(chamfer_dst.shape[1] - 1, -1, -1):
            pixel_center = chamfer_dst[m, n]

            b0 = float("inf") if(n + 1 > chamfer_dst.shape[1] - 1) else chamfer_dst[m, n + 1]
            b0_dis = neighbor_pixel_dis + b0

            b1 = float("inf") if(m + 1 > chamfer_dst.shape[0] - 1 or n + 1 > chamfer_dst.shape[1] - 1) else chamfer_dst[m + 1, n + 1]
            b1_dis = neighbor_pixel_dis + b1

            b2 = float("inf") if(m + 1 > chamfer_dst.shape[0] - 1) else chamfer_dst[m + 1, n]
            b2_dis = neighbor_pixel_dis + b2

            b3 = float("inf") if(m + 1 > chamfer_dst.shape[0] - 1 or n - 1 < 0) else chamfer_dst[m + 1, n - 1]
            b3_dis = neighbor_pixel_dis+ b3

            chamfer_dst[m, n] = min(pixel_center, b0_dis, b1_dis, b2_dis, b3_dis)

    #print("chamfer_dst after backward pass", chamfer_dst)
    return chamfer_dst

def calculate_match_score_bk(chamfer_dst, template):
    match_score = np.sum(template[template==255] * chamfer_dst[chamfer_dst==0])
    return match_score

def calculate_match_score(chamfer_dst, template):
    result = np.where(template == 255)
    match_score = np.sum(chamfer_dst[result[0], result[1]])
    return match_score

def plot(plt, matrix, title):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, 126, 8))
    ax.set_yticks(np.arange(0, 126, 8))
    plt.setp(ax.get_xticklabels(), rotation=90, rotation_mode="anchor")
    ax.set_title(title)
    plt.imshow(matrix)
    plt.colorbar()
    plt.show()

# # real image
# im = cv.imread('1.png')
# canny = cv.Canny(im,100,200)
# chamfer_dst = calculate_chamfer_dst(canny)
# match_score = calculate_match_score(chamfer_dst, canny)
# print(match_score)


# test image
# test_edge_image = np.zeros((8,8)).astype("uint8")
# test_edge_image[2,0] = 255
# test_edge_image[4,4] = 255
# test_edge_image[5,4] = 255
# test_edge_image[6,4] = 255
# test_edge_image[6,5] = 255
# test_edge_image[6,6] = 255
# test_edge_image[5,7] = 255
# test_edge_image[7,7] = 255
#
# chamfer_dst = calculate_chamfer_dst(test_edge_image)
# match_score = calculate_match_score(chamfer_dst, test_edge_image)
# print(match_score)

files = [file for file in glob.glob("GaitImages/" + "*")]
files.sort()
#print(len(files))

im_list = []
chamfer_dst_list = []
print("computing chamfer distance matrix....")
for file in files:
    print(file)
    im = cv.imread(file)
    canny = cv.Canny(im,100,200)
    im_list.append(canny)
    chamfer_dst = calculate_chamfer_dst(canny)
    chamfer_dst_list.append(chamfer_dst)

#print(len(im_list), len(chamfer_dst_list))

print("computing match scores....")
match_score_list_1 = []
match_score_list_2 = []
for i in range(len(im_list)):
    for j in range(len(im_list)):
        match_score_list_2.append(calculate_match_score(chamfer_dst_list[i],im_list[j]))
    #print(match_score_list_2)
    match_score_list_1.append(match_score_list_2)
    match_score_list_2 = []
match_scores = np.array(match_score_list_1)
plot(plt, match_scores, "chamfer match scores")
