import config
import pandas as pd
import csv

def emulateMissingRid(token):
    with open(config.singleUserBackendLog, "r",encoding='utf-8') as singleUserBackendLog:
        
        singleUserBackendLog = csv.reader(singleUserBackendLog,delimiter=";")
        
        # rid emulation
        nextRidValue  = 0
        rowsCount = 0
        nonDigitIndexs = []
        print(token)
        if 'lsDnySG4yhlHr08uPDipNZtcHKq7hbbFpPUkheuWCUfk5qzfv3gL0E875ptHEx4f' in token :
            print("Yohoo")

        for bIdx, bRow in enumerate(singleUserBackendLog):
            rowsCount+=1
            if bRow[4].isdigit():
                nextRidValue = bRow[4]
                if len(nonDigitIndexs) > 0:
                    userData = pd.read_csv(config.singleUserBackendLog, sep=';')
                    for rowIndex in nonDigitIndexs:
                        columnName = userData.columns.values[4]
                        userData.set_value(rowIndex-1, columnName, nextRidValue)
                        nonDigitIndexs.remove(rowIndex)
                        
                    userData.to_csv(config.singleUserBackendLog, index=False , sep=';')    
            else:
                nonDigitIndexs.append(bIdx)
                
            
    if rowsCount == len(nonDigitIndexs) and len(nonDigitIndexs)!=0:
        return True
    else:
        return False 