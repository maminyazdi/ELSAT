# Configuration and settings
import os
import glob

def init():
    global originalFrontEndLog, \
           originalBackEndLog , \
           cleanFrontEndLog, \
           cleanBackEndLog, \
           accessTokensFile, \
           singleUserBackendLog, \
           singleUserFrontEndLog, \
           groupingLog, \
           headerMatrix, \
           userMatrix, \
           combinedMatrix, \
           combinedLog, \
           abstractedCombinedLog, \
           combinedLogFull, \
           columnOne, \
           xesReadyFormatLog, \
           processModelVis


    mainFolder = "C:/Workspace/Dataset/"

    #Clear the files and re-write
    files = glob.glob(mainFolder+"Grouping/*")
    for f in files:
       os.remove(f)

    originalFrontEndLog =   mainFolder+"original/FrontEndLogs.csv"
    originalBackEndLog =    mainFolder+"original/BackEndLogs.csv"

    cleanFrontEndLog =      mainFolder+"Cleaned logs/Cleaned logs-FrontEnd.csv"
    cleanBackEndLog =       mainFolder+"Cleaned logs/Cleaned logs-BackEnd.csv"

    accessTokensFile =      mainFolder+"Grouping/accessTokens.csv"
    singleUserBackendLog =  mainFolder+"Grouping/BackEndSingleUser.csv"
    singleUserFrontEndLog = mainFolder+"Grouping/FrontEndSingleUser.csv"
    groupingLog =           mainFolder+"Grouping/grouping.csv"
    headerMatrix =          mainFolder+"Grouping/headerMatrix.csv"
    userMatrix =            mainFolder+"Grouping/userMatrix.csv"
    combinedMatrix =        mainFolder+"Grouping/combinedMatrix.csv"
    columnOne =             mainFolder+"Grouping/columnOne.csv"

    combinedLog =           mainFolder+"Grouping/combinedLog.csv"
    abstractedCombinedLog = mainFolder+"Grouping/abstractedCombinedLog.csv"
    combinedLogFull =       mainFolder+"Grouping/combinedLogFull.csv"

    xesReadyFormatLog =     mainFolder + "Grouping/xesReadyFormatLog.csv"
    processModelVis   =     mainFolder + "Grouping/visualizationPM"