import csv
import config


#create user matrix
def createUserMatrix(matrix, hasWeight,events_list):
    with open(config.singleUserBackendLog, 'r', encoding='utf-8') as singleUserBackendLog, \
         open(config.singleUserFrontEndLog, 'r', encoding='utf-8') as singleUserFrontEndLog, \
         open(config.columnOne, 'a', encoding='utf-8', newline='' ) as columnOne, \
         open(config.userMatrix, "w", encoding='utf-8', newline='') as userMatrix:

        singleUserBackendLog = csv.reader(singleUserBackendLog, delimiter=";")
        singleUserFrontEndLog = csv.reader(singleUserFrontEndLog, delimiter=";")
        columnOne = csv.writer(columnOne, delimiter="\n")
        userMatrix = csv.writer(userMatrix, delimiter="\n")

        # allow for loop to traverse the frontEndLog multiple times
        fontEndlog = list(singleUserFrontEndLog)


        fIndex = 0
        flagValue = 0
        matrixRowCount = 1

        x = 0


        def createMatrixRow(matrixRowCount):
            matrix.append([])
            x = 0
            while x < len(matrix[0]):
                matrix[matrixRowCount].append(0)
                x += 1
            return matrix[matrixRowCount]

        createMatrixRow(matrixRowCount)
        
        for bIdx, bRow in enumerate(singleUserBackendLog):
            previous_weight = 0
            if flagValue == int(bRow[4]):  # Same row? - create the descriptive matrix
                if hasWeight:
                    previous_weight = matrix[matrixRowCount][matrix[0].index(bRow[3])]
                    matrix[matrixRowCount][matrix[0].index(bRow[3])] = previous_weight+1
                else:
                    matrix[matrixRowCount][matrix[0].index(bRow[3])] = 1

            elif matrixRowCount < len(matrix[0]):
                matrixRowCount += 1
                createMatrixRow(matrixRowCount)
                if hasWeight:
                    previous_weight = matrix[matrixRowCount][matrix[0].index(bRow[3])]
                    matrix[matrixRowCount][matrix[0].index(bRow[3])] = previous_weight+1
                else:
                    matrix[matrixRowCount][matrix[0].index(bRow[3])] = 1
            
            if int(bRow[4]) == 0:
                flagValue = int(bRow[4])
                columnOne.writerow(["PageLoading"])
                matrix[matrixRowCount][0] = "PageLoading"
                print("PageLoading")

            if int(bRow[4]) > 0:
                flagValue = int(bRow[4])

                # loop front end table
                for fIdx, fRow in enumerate(fontEndlog):
                    if fIdx == fIndex:
                        fIndex += 1

                        if int(fRow[3]) == int(bRow[4]):
                            columnOne.writerow([fRow[2]])
                            if fRow[2] not in events_list:
                                events_list.append(fRow[2])
                            print(fRow[2])
                            matrix[matrixRowCount][0] = fRow[2]
                            fIndex = fIdx
                            break
        # removes the header
        del matrix[0]
        userMatrix.writerow(matrix)
        return matrix, events_list


#create user log
def createUserLog():
    with open(config.singleUserBackendLog, 'r', encoding='utf-8') as singleUserBackendLog, \
         open(config.singleUserFrontEndLog, 'r', encoding='utf-8') as singleUserFrontEndLog, \
         open(config.combinedLog, "a", encoding='utf-8', newline='') as combinedLog:

        singleUserBackendLog = csv.reader(singleUserBackendLog, delimiter=";")
        singleUserFrontEndLog = csv.reader(singleUserFrontEndLog, delimiter=";")
        combinedLog = csv.writer(combinedLog, delimiter=";")

        # allow for loop to traverse the frontEndLog multiple times
        fontEndlog = list(singleUserFrontEndLog)

        fIndex = 0

        for bIdx, bRow in enumerate(singleUserBackendLog):

            event_value = ""
            if int(bRow[4]) == 0:
                event_value = "PageLoading"
                combinedLog.writerow([ bRow[0], bRow[1], bRow[2], event_value])

            if int(bRow[4]) > 0:
                # loop front end table
                for fIdx, fRow in enumerate(fontEndlog):
                    if fIdx == fIndex:
                        fIndex += 1

                        if int(fRow[3]) == int(bRow[4]):
                            event_value = fRow[2]
                            combinedLog.writerow([bRow[0], bRow[1], bRow[2], event_value])

                            fIndex = fIdx
                            break








