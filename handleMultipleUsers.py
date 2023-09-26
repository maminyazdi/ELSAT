import csv
import config
import createMatrixBase
import generateUserMatrix

def createcsvfiles(accesstokenvalue):
    #print(">>>>>>>>createcsvfiles()")
    with open(config.cleanBackEndLog, 'r',
              encoding='utf-8') as BackEnd, \
            open(config.cleanFrontEndLog, "r",
                 encoding='utf-8') as FrontEnd, \
            open(config.singleUserBackendLog, "w",
                 encoding='utf-8', newline='') as BackEndSingleUser, \
            open(config.singleUserFrontEndLog, "w",
                 encoding='utf-8', newline='') as FrontEndSingleUser:

        BackEnd = csv.reader(BackEnd, delimiter=";")
        FrontEnd = csv.reader(FrontEnd, delimiter=";")
        BackEndSingleUser = csv.writer(BackEndSingleUser, delimiter=";")
        FrontEndSingleUser = csv.writer(FrontEndSingleUser, delimiter=";")

        accsesstokenvalue1 = accesstokenvalue
        flag = True

        for bIdx, bRow in enumerate(BackEnd):
            timestamp1= bRow[0]
            accessToken1 = bRow[1]
            servicescope1 = bRow[2]
            resource1 = bRow[3]
            rid1 = bRow[4]

            if (accessToken1 == accsesstokenvalue1) :
                BackEndSingleUser.writerow([timestamp1, accessToken1, servicescope1, resource1, rid1])



        for fIdx, fRow in enumerate(FrontEnd):
            timestamp2 = fRow[0]
            accessToken2 = fRow[1]
            page2 = fRow[2]
            rid2 = fRow[3]

            if (accessToken2 == accsesstokenvalue1):
                FrontEndSingleUser.writerow([timestamp2, accessToken2, page2, rid2])

        #matrix = createMatrixBase.createheadermatrix()
        #generateUserMatrix.createUserMatrix(matrix)

#       descriptiveMatrixGenerator.makeusermatrix(accsesstokenvalue1)