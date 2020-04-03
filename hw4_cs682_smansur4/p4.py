import numpy as np

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
# for row_index in range(len(test_edge_image)):
#     print("---------------------")
#     indices_nonzero = np.where(test_edge_image[row_index] == 255)
#     print("indices_nonzero",indices_nonzero[0])
#     indices_zero = np.where(test_edge_image[row_index] == 0)
#     print("indices_zero", indices_zero[0])
#
#     for item in indices_nonzero[0]:
#         print("abs distance", np.abs(indices_zero[0] - item))
#         print("min dis", min(np.abs(indices_zero[0] - item)))


test_edge_image = np.zeros((6,10)).astype("uint8")
edt_matrix = np.zeros((6,10)).astype("uint8")

test_edge_image[1,2] = 255
test_edge_image[1,3] = 255
test_edge_image[1,4] = 255
test_edge_image[1,5] = 255

test_edge_image[2,2] = 255
test_edge_image[2,3] = 255
test_edge_image[2,4] = 255
test_edge_image[2,5] = 255
test_edge_image[2,6] = 255
test_edge_image[2,7] = 255
test_edge_image[2,8] = 255

test_edge_image[3,1] = 255
test_edge_image[3,2] = 255
test_edge_image[3,3] = 255
test_edge_image[3,4] = 255
test_edge_image[3,5] = 255
test_edge_image[3,6] = 255
test_edge_image[3,7] = 255
test_edge_image[3,8] = 255

test_edge_image[4,3] = 255
test_edge_image[4,4] = 255
test_edge_image[4,5] = 255
test_edge_image[4,6] = 255
test_edge_image[4,7] = 255

for row_index in range(len(test_edge_image)):
    print("---------------------")
    indices_nonzero = np.where(test_edge_image[row_index] == 255)
    print("indices_nonzero",indices_nonzero[0])
    indices_zero = np.where(test_edge_image[row_index] == 0)
    print("indices_zero", indices_zero[0])

    for item in indices_nonzero[0]:
        print("abs distance", np.abs(indices_zero[0] - item))
        print("min dis", min(np.abs(indices_zero[0] - item)))
        val = min(np.abs(indices_zero[0] - item))
        edt_matrix[row_index, item] = val

    print(edt_matrix ** 2)
