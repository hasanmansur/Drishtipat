import numpy as np


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

print("--------row scan-------------")
for row_index in range(len(test_edge_image)):
    #print("---------------------")
    indices_nonzero = np.where(test_edge_image[row_index] > 0)
    #print("indices_nonzero",indices_nonzero[0])
    indices_zero = np.where(test_edge_image[row_index] == 0)
    #print("indices_zero", indices_zero[0])

    for item in indices_nonzero[0]:
        #print("abs distance", np.abs(indices_zero[0] - item))
        #print("min dis", min(np.abs(indices_zero[0] - item)))
        val = min(np.abs(indices_zero[0] - item))
        edt_matrix[row_index, item] = val

sqr_edt_matrix = np.square(edt_matrix)
print(sqr_edt_matrix)


print("--------column scan-------------")
for column_index in range(sqr_edt_matrix.shape[1]):
    #print("-------------------")
    #print("column_index", column_index)
    values_in_a_column = sqr_edt_matrix[:,column_index]
    #print("values_in_a_column", values_in_a_column)
    row_indices_in_a_column = np.arange(len(values_in_a_column))
    #print("row indices in a column", row_indices_in_a_column)
    indices_nonzero = np.where(values_in_a_column > 0)
    indices_nonzero_list = indices_nonzero[0]
    #print("indices_nonzero_list", indices_nonzero_list)

    for row_index in indices_nonzero_list:
        row_index_minus_row_indices_squared = np.abs(row_indices_in_a_column - row_index) ** 2
        val = min(values_in_a_column + row_index_minus_row_indices_squared)
        edt_matrix[row_index, column_index] = val

print(edt_matrix)
