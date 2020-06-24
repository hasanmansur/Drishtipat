# S M HASAN MANSUR
# G01143027

import cv2 as cv
import numpy as np
from pandas import *
from matplotlib import pyplot as plt
import copy
import pprint

pp = pprint.PrettyPrinter(indent=2)

def print_row_9_1_11(message_board):
    for row in (8,9,10):
        print("row", row+1, ":", message_board[row])

# E_zcen calculation
def E_zcen(l_im, r_im, d_val, masseage_board):
    for i in range(21):
        l_im_i = i + 1 # left image starting row
        r_im_i = i + 1 # right image starting row
        for j in range(21):
            # -----------left image processing--------------------
            l_im_j = j + 1 # left image starting column
            b_window = l_im[l_im_i-1:l_im_i+2, l_im_j-1:l_im_j+2]
            b_window_mean = np.mean(b_window)
            b_x = np.sign(b_window - b_window_mean).astype("int").flatten()
            # -----------right image processing--------------------
            r_im_j = j + 7 - int(d_val) # right image starting column
            m_window = r_im[r_im_i-1:r_im_i+2, r_im_j-1:r_im_j+2]
            m_window_mean = np.mean(m_window)
            m_x = np.sign(m_window - m_window_mean).astype("int").flatten()
            # -----------calculating e_zcen------------------------
            e_zcen = np.count_nonzero(b_x - m_x)
            masseage_board[i, j] = e_zcen

# adjacency list creation (ideal and corner cases)
def create_adjacency_list(i,j):
    if(i == 0 and j == 0):
        #print("left top corner")
        return [(i,j+1),(i+1,j)]
    elif(i == 0 and j == 20):
        #print("right top corner")
        return [(i,j-1),(i+1,j)]
    elif(i == 20 and j == 0):
        #print("left bottom corner")
        return [(i,j+1), (i-1,j)]
    elif(i == 20 and j == 20):
        #print("right bottom corner")
        return [(i,j-1), (i-1,j)]
    elif(i == 0):
        #print("top row")
        return [(i,j-1), (i,j+1), (i+1,j)]
    elif(i == 20):
        #print("bottom row")
        return [(i,j-1), (i,j+1), (i-1,j)]
    elif(j == 0):
        #print("leftmost column")
        return [(i-1,j), (i,j+1), (i+1,j)]
    elif(j == 20):
        #print("rightmost column")
        return [(i-1,j), (i,j-1), (i+1,j)]
    else:
        #print("ideal pixels")
        return [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]

# E_smoothness term calculation
def calculate_e_smooth_h_d(h, d):
    return np.absolute(h-d)

# calculating neighbor's message at t1 time
def calculate_m_t1_p_q(i, j, adjacent_pixel, d_val):
    # print("origin_pixel: ", (i,j))
    # print("adjacent_pixel: ", adjacent_pixel)
    # print("d_val: ", d_val)

    p = adjacent_pixel
    L =  [0,1,2,3,4,5,6]
    cost_for_different_h_levels = []
    for h in L:
        e_data_p_h = 0
        e_smooth_h_d = 0
        if(h == 0):
            e_data_p_h = d_0[p[0],p[1]]
        elif(h == 1):
            e_data_p_h = d_1[p[0],p[1]]
        elif(h == 2):
            e_data_p_h = d_2[p[0],p[1]]
        elif(h == 3):
            e_data_p_h = d_3[p[0],p[1]]
        elif(h == 4):
            e_data_p_h = d_4[p[0],p[1]]
        elif(h == 5):
            e_data_p_h = d_5[p[0],p[1]]
        elif(h == 6):
            e_data_p_h = d_6[p[0],p[1]]

        e_smooth_h_d = calculate_e_smooth_h_d(h, d_val)
        adjacency_list_of_p = create_adjacency_list(p[0],p[1])
        adj_list_of_p_final = []
        for pos in range(len(adjacency_list_of_p)):
            if(adjacency_list_of_p[pos][0] != i or adjacency_list_of_p[pos][1] != j):
                adj_list_of_p_final.append(adjacency_list_of_p[pos])
        t0_total_cost_cost_from_neighbors = 0
        for neighbor in adj_list_of_p_final:
            if(h == 0):
                msg_from_neighbor = d_0[neighbor[0],neighbor[1]]
            elif(h == 1):
                msg_from_neighbor = d_1[neighbor[0],neighbor[1]]
            elif(h == 2):
                msg_from_neighbor = d_2[neighbor[0],neighbor[1]]
            elif(h == 3):
                msg_from_neighbor = d_3[neighbor[0],neighbor[1]]
            elif(h == 4):
                msg_from_neighbor = d_4[neighbor[0],neighbor[1]]
            elif(h == 5):
                msg_from_neighbor = d_5[neighbor[0],neighbor[1]]
            elif(h == 6):
                msg_from_neighbor = d_6[neighbor[0],neighbor[1]]
            t0_total_cost_cost_from_neighbors = t0_total_cost_cost_from_neighbors + msg_from_neighbor
        final_cost_for_h = e_data_p_h + e_smooth_h_d + t0_total_cost_cost_from_neighbors
        cost_for_different_h_levels.append(final_cost_for_h)
    return min(cost_for_different_h_levels)

# accumulating total cost at t1 time
def accumulate_cost_t1(message_board, d_val):
    for i in range(im_height):
        for j in range(im_width):
            # adjacency list creation
            adjacency_list_of_ij = create_adjacency_list(i,j)
            edata_q_d = 0
            if(d_val == 0):
                edata_q_d = d_0[i,j]
            elif(d_val == 1):
                edata_q_d = d_1[i,j]
            elif(d_val == 2):
                edata_q_d = d_2[i,j]
            elif(d_val == 3):
                edata_q_d = d_3[i,j]
            elif(d_val == 4):
                edata_q_d = d_4[i,j]
            elif(d_val == 5):
                edata_q_d = d_5[i,j]
            elif(d_val == 6):
                edata_q_d = d_6[i,j]
            sum_of_t1_adjacent_messages = 0
            for adjacent_pixel in adjacency_list_of_ij:
                t1_msg_from_adjacent_pixel = calculate_m_t1_p_q(i, j, adjacent_pixel, d_val)
                sum_of_t1_adjacent_messages = sum_of_t1_adjacent_messages + t1_msg_from_adjacent_pixel
            total_accumulated_cost_t1 = edata_q_d + sum_of_t1_adjacent_messages
            message_board[i,j] = total_accumulated_cost_t1

# calculating neighbor's message at t2 time
def calculate_m_t2_p_q(i, j, adjacent_pixel, d_val):
    # print("origin_pixel: ", (i,j))
    # print("adjacent_pixel: ", adjacent_pixel)
    # print("d_val: ", d_val)

    p = adjacent_pixel
    L =  [0,1,2,3,4,5,6]
    cost_for_different_h_levels = []
    for h in L:
        e_data_p_h = 0
        e_smooth_h_d = 0
        if(h == 0):
            e_data_p_h = d_0[p[0],p[1]]
        elif(h == 1):
            e_data_p_h = d_1[p[0],p[1]]
        elif(h == 2):
            e_data_p_h = d_2[p[0],p[1]]
        elif(h == 3):
            e_data_p_h = d_3[p[0],p[1]]
        elif(h == 4):
            e_data_p_h = d_4[p[0],p[1]]
        elif(h == 5):
            e_data_p_h = d_5[p[0],p[1]]
        elif(h == 6):
            e_data_p_h = d_6[p[0],p[1]]

        e_smooth_h_d = calculate_e_smooth_h_d(h, d_val)
        adjacency_list_of_p = create_adjacency_list(p[0],p[1])
        adj_list_of_p_final = []
        for pos in range(len(adjacency_list_of_p)):
            if(adjacency_list_of_p[pos][0] != i or adjacency_list_of_p[pos][1] != j):
                adj_list_of_p_final.append(adjacency_list_of_p[pos])
        t1_total_cost_cost_from_neighbors = 0
        for neighbor in adj_list_of_p_final:
            if(h == 0):
                msg_from_neighbor = d_0_t1[neighbor[0],neighbor[1]]
            elif(h == 1):
                msg_from_neighbor = d_1_t1[neighbor[0],neighbor[1]]
            elif(h == 2):
                msg_from_neighbor = d_2_t1[neighbor[0],neighbor[1]]
            elif(h == 3):
                msg_from_neighbor = d_3_t1[neighbor[0],neighbor[1]]
            elif(h == 4):
                msg_from_neighbor = d_4_t1[neighbor[0],neighbor[1]]
            elif(h == 5):
                msg_from_neighbor = d_5_t1[neighbor[0],neighbor[1]]
            elif(h == 6):
                msg_from_neighbor = d_6_t1[neighbor[0],neighbor[1]]
            t1_total_cost_cost_from_neighbors = t1_total_cost_cost_from_neighbors + msg_from_neighbor
        final_cost_for_h = e_data_p_h + e_smooth_h_d + t1_total_cost_cost_from_neighbors
        cost_for_different_h_levels.append(final_cost_for_h)
    return min(cost_for_different_h_levels)

# accumulating total cost at t2 time
def accumulate_cost_t2(message_board, d_val):
    for i in range(im_height):
        for j in range(im_width):
            # adjacency list creation
            adjacency_list_of_ij = create_adjacency_list(i,j)
            edata_q_d = 0
            if(d_val == 0):
                edata_q_d = d_0[i,j]
            elif(d_val == 1):
                edata_q_d = d_1[i,j]
            elif(d_val == 2):
                edata_q_d = d_2[i,j]
            elif(d_val == 3):
                edata_q_d = d_3[i,j]
            elif(d_val == 4):
                edata_q_d = d_4[i,j]
            elif(d_val == 5):
                edata_q_d = d_5[i,j]
            elif(d_val == 6):
                edata_q_d = d_6[i,j]
            sum_of_t1_adjacent_messages = 0
            for adjacent_pixel in adjacency_list_of_ij:
                t1_msg_from_adjacent_pixel = calculate_m_t2_p_q(i, j, adjacent_pixel, d_val)
                sum_of_t1_adjacent_messages = sum_of_t1_adjacent_messages + t1_msg_from_adjacent_pixel
            total_accumulated_cost_t1 = edata_q_d + sum_of_t1_adjacent_messages
            message_board[i,j] = total_accumulated_cost_t1


################################################################################
################ DISPARITY MESSAGE BOARD INITIALIZATION ########################
################## MIN. DISPARITY AFTER INITIALIZATION #########################
######################### DEPTH CALCULATION ####################################
################################################################################

left_image = cv.imread('images/left.png', 0)
right_image = cv.imread('images/right.png', 0)
im_height = right_image.shape[0]
im_width = right_image.shape[0]


# padding the left image
left_image_padded = np.zeros(shape=(im_height+2,im_width+2), dtype="uint8")
left_image_padded[1:22,1:22] = left_image
# print("---------------padded left image---------------------")
# print(DataFrame(left_image_padded))

# padding the right image
right_image_padded = np.zeros(shape=(23,29), dtype="uint8")
#right_image_padded[1:22,6:27] = right_image
right_image_padded[1:22,7:28] = right_image
# print("---------------padded right_image---------------------")
# print(DataFrame(right_image_padded))

# create empty message boards
d_0 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_3 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_4 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_5 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_6 = np.zeros(shape=(im_height,im_width), dtype="uint8")

# initialiize message boards
E_zcen(left_image_padded, right_image_padded, 0, d_0)
E_zcen(left_image_padded, right_image_padded, 1, d_1)
E_zcen(left_image_padded, right_image_padded, 2, d_2)
E_zcen(left_image_padded, right_image_padded, 3, d_3)
E_zcen(left_image_padded, right_image_padded, 4, d_4)
E_zcen(left_image_padded, right_image_padded, 5, d_5)
E_zcen(left_image_padded, right_image_padded, 6, d_6)

# print row 9,10,11 from the initial message boards
#print("--------printing row 9,10,11 from the initial message boards---------")
# print("-------d_0------------------")
# print_row_9_1_11(d_0)
# print("-------d_1------------------")
# print_row_9_1_11(d_1)
# print("-------d_2------------------")
# print_row_9_1_11(d_2)
# print("-------d_3------------------")
# print_row_9_1_11(d_3)
# print("-------d_4------------------")
# print_row_9_1_11(d_4)
# print("-------d_5------------------")
# print_row_9_1_11(d_5)
# print("-------d_6------------------")
# print_row_9_1_11(d_6)


# disparities with min E_zcen values across all message boards
d_min = np.zeros(shape=(im_height,im_width), dtype="int8")
for i in range(21):
    for j in range(21):
        a = np.array([d_0[i][j], d_1[i][j], d_2[i][j], d_3[i][j], d_4[i][j], d_5[i][j], d_6[i][j]])
        indices_of_min_values = np.where(a == min(a))[0]
        #print(indices_of_min_values)
        if (len(indices_of_min_values) > 1):
            #print(len(indices_of_min_values))
            d_min[i][j] = -1
        else:
            d_min[i][j] = indices_of_min_values[0]

# print("---------printing whole d_min for min disparity values-------------- ")
# print(DataFrame(d_min))
# print("---------printing row 9,10,11 for min disparity values-------------- ")
# print_row_9_1_11(d_min)

# depth images
d_depth = np.zeros(shape=(im_height,im_width), dtype="uint8")
for i in range (21):
    for j in range (21):
        if d_min[i][j] <= 0:
            d_depth[i][j] = 0 # to skip division by 0 for d=0
        else:
            d_depth[i][j] = int(round((.2 * 500)/d_min[i][j]))
print("depth values")
print("------------")
#print_row_9_1_11(d_depth)
print(DataFrame(d_depth))
cv.imshow('depth mage',d_depth)
cv.waitKey(0)
cv.destroyAllWindows()


################################################################################
###################### BELIEF PROPAGATION ######################################
################################################################################

# create empty message boards for t1 time
d_0_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_1_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_2_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_3_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_4_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_5_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_6_t1 = np.zeros(shape=(im_height,im_width), dtype="uint8")

# populate message boards in t1 time
accumulate_cost_t1(d_0_t1, 0)
accumulate_cost_t1(d_1_t1, 1)
accumulate_cost_t1(d_2_t1, 2)
accumulate_cost_t1(d_3_t1, 3)
accumulate_cost_t1(d_4_t1, 4)
accumulate_cost_t1(d_5_t1, 5)
accumulate_cost_t1(d_6_t1, 6)

# chosen minimum disparity after t1
d_min_after_t1 = np.zeros(shape=(im_height,im_width), dtype="int8")
for i in range(21):
    for j in range(21):
        a = np.array([d_0_t1[i][j], d_1_t1[i][j], d_2_t1[i][j], d_3_t1[i][j], d_4_t1[i][j], d_5_t1[i][j], d_6_t1[i][j]])
        indices_of_min_values = np.where(a == min(a))[0]
        #print(indices_of_min_values)
        if (len(indices_of_min_values) > 1):
            #print(len(indices_of_min_values))
            d_min_after_t1[i][j] = -1
            pass
        else:
            d_min_after_t1[i][j] = indices_of_min_values[0]
print("min. disparity after T1")
print("-----------------------")
print(DataFrame(d_min_after_t1))
plt.imshow(d_min_after_t1)
plt.title("min. disparity after T1")
plt.show()


# create empty message boards for t2 time
d_0_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_1_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_2_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_3_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_4_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_5_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")
d_6_t2 = np.zeros(shape=(im_height,im_width), dtype="uint8")

# populate message boards in t2 time
accumulate_cost_t2(d_0_t2, 0)
accumulate_cost_t2(d_1_t2, 1)
accumulate_cost_t2(d_2_t2, 2)
accumulate_cost_t2(d_3_t2, 3)
accumulate_cost_t2(d_4_t2, 4)
accumulate_cost_t2(d_5_t2, 5)
accumulate_cost_t2(d_6_t2, 6)

# chosen minimum disparity after t2
d_min_after_t2 = np.zeros(shape=(im_height,im_width), dtype="int8")
for i in range(21):
    for j in range(21):
        a = np.array([d_0_t2[i][j], d_1_t2[i][j], d_2_t2[i][j], d_3_t2[i][j], d_4_t2[i][j], d_5_t2[i][j], d_6_t2[i][j]])
        indices_of_min_values = np.where(a == min(a))[0]
        #print(indices_of_min_values)
        if (len(indices_of_min_values) > 1):
            #print(len(indices_of_min_values))
            d_min_after_t2[i][j] = -1
            pass
        else:
            d_min_after_t2[i][j] = indices_of_min_values[0]
print("min. disparity after T2")
print("-----------------------")
print(DataFrame(d_min_after_t2))
plt.imshow(d_min_after_t2)
plt.title("min. disparity after T2")
plt.show()
