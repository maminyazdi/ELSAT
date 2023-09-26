import csv
import config
from numpy import *

#config.init()

with open('C:/Workspace/Dataset/Grouping/combinedMatrix.csv', "r",
          encoding='utf-8') as combinedMatrix:
    combinedMatrix = csv.reader(combinedMatrix, delimiter=",")
    combinedMatrix = list(combinedMatrix)

    upperValue = 1
    lowerValue = 0.20

    while upperValue <= 1:
        print("<<<<<<<<<<<<<<<<<< PCC Between "+str(lowerValue)+" to "+ str(upperValue) +">>>>>>>>>>>>>>>>>>>>>>>")
        firstArray = array([])
        secondArray = array([])
        traversedList = []
        full_events_name = []
        for midx1, matrix1 in enumerate(combinedMatrix[1:]):
            # print(">>>>>: " + str( midx1))

            # matrix1.pop(0)
            firstArray = list(map(int, matrix1[1:]))
            if firstArray not in traversedList:
                traversedList.append(firstArray)
            else:
                continue

            # traversedList.append(firstArray) if firstArray not in traversedList else traversedList

            for midx2, matrix2 in enumerate(combinedMatrix[1:]):
                secondArray = list(map(int, matrix2[1:]))

                if (corrcoef([firstArray, secondArray])[0][1] >= lowerValue and corrcoef([firstArray, secondArray])[0][
                    1] <= upperValue):
                    matrixName1 = matrix1[0]
                    matrixName2 = matrix2[0]
                    if matrixName1 != matrixName2:
                        variableNames = matrix1[0] + " VS " + matrix2[0]
                        if variableNames not in full_events_name:
                            print(matrix1[0] + " VS " + matrix2[0])
                            print(corrcoef([firstArray, secondArray])[0][1])
                            print()
                            full_events_name.append(variableNames)
        upperValue += 0.03
        upperValue= round(upperValue, 2)
        lowerValue += 0.03
        lowerValue = round(lowerValue, 2)
        full_events_name.clear()

    # next(combinedMatrix)

    print("PCC DONE!")