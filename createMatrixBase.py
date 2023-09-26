import csv
import config

#create header
def createheadermatrix():

    #print("createheadermatrix()")

    with open(config.cleanBackEndLog, 'r',
              encoding='utf-8') as cleanBackEndLog, \
            open(config.headerMatrix, "w",
                 encoding='utf-8', newline='') as headerMatrix:

        cleanBackEndLog = csv.reader(cleanBackEndLog, delimiter=";")
        headerMatrix = csv.writer(headerMatrix, delimiter=";")

        matrix = [["Groups"]]
        # Create the header of the matrix
        for bIdx, bRow in enumerate(cleanBackEndLog):

            # bRow[3] is the backend call value
            if bRow[3] not in matrix[0]:
                matrix[0].append(bRow[3])

        headerMatrix.writerow(matrix)
    return matrix



