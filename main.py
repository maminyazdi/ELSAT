import config
import csv, pandas as pd
import createListOfAccessTokens
import handleMultipleUsers
import createMatrixBase
import generateUserMatrix
import frontEndLogCleaning
import backEndLogCleaning
from dataEmulation import emulateMissingRid
import csvToXesConverter, cleanFinalMatrix
import imbalancedDataSet
import timestampAbstraction, processModelVis

config.init()

backEndLogCleaning.cleanbackendlog()
frontEndLogCleaning.cleanfrontendlog()

createListOfAccessTokens.createtokens()

with open(config.accessTokensFile, "r", encoding='utf-8') as accessTokens, \
        open(config.combinedMatrix, "w", encoding='utf-8', newline='\n') as combinedMatrix:
    accessTokens = csv.reader(accessTokens, delimiter=";")
    combinedMatrix = csv.writer(combinedMatrix, delimiter="\n")

    originalheaderMatrix = createMatrixBase.createheadermatrix()

    """ 
    wantWeight = input("Do you need weighted matrix? Y/N")
    if wantWeight.lower() == "y":
        hasWeight = True
    else:
        hasWeight = False
      """

    events_list = []
    for token in accessTokens:
        handleMultipleUsers.createcsvfiles(token[0])
        headerMatrix = createMatrixBase.createheadermatrix()

        if emulateMissingRid(token):
            continue

        userMatrix, events_list = generateUserMatrix.createUserMatrix(headerMatrix, False, events_list)
        originalheaderMatrix.extend(userMatrix)
        generateUserMatrix.createUserLog()

    combinedMatrix.writerow(originalheaderMatrix)
    cleanFinalMatrix.cleanMatrix()

    imbalancedDataSet.execute()

    timestampAbstraction.abstractLogs()
    dataframe = csvToXesConverter.convertCSVtoXES()
    # processModelVis.inductiveMinerProcessModelVis(dataframe)
    # processModelVis.heuristicMinerProcessModelVis(dataframe)
    processModelVis.dfgProcessModelVis(dataframe)
    print(events_list)



