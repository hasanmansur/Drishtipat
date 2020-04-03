import numpy as np
import cv2 as cv
import glob

files = [file for file in glob.glob("GaitImages/" + "*")]
files.sort()

for file in files:
    print(file)
    im = cv.imread(file, 0)
    # cv.imshow("im", im)
    # cv.waitKey(0)

    edt_matrix = np.zeros((im.shape[0], im.shape[1])).astype("uint8")

    print("--------row scan-------------")
    for row_index in range(len(im)):
        #print("---------------------")
        indices_nonzero = np.where(im[row_index] > 0)
        #print("indices_nonzero",indices_nonzero[0])
        indices_zero = np.where(im[row_index] == 0)
        #print("indices_zero", indices_zero[0])

        for item in indices_nonzero[0]:
            #print("abs distance", np.abs(indices_zero[0] - item))
            #print("min dis", min(np.abs(indices_zero[0] - item)))
            val = min(np.abs(indices_zero[0] - item))
            edt_matrix[row_index, item] = val

    sqr_edt_matrix = np.square(edt_matrix)
    #print(sqr_edt_matrix)


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
    cv.imshow("edt", edt_matrix)

    # # using opencv distance transform
    # edt_opencv = cv.distanceTransform(im,cv.DIST_L2,5)
    # cv.imshow("edt_opencv", edt_matrix)

    cv.waitKey(0)
