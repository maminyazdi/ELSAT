import csv
import handleMultipleUsers
import config

def createtokens():
    with open(config.cleanBackEndLog, 'r',
              encoding='utf-8') as BackEnd, \
            open(config.accessTokensFile, "w",
                 encoding='utf-8', newline='') as accessTokens:
        BackEnd = csv.reader(BackEnd, delimiter=";")
        accessTokens = csv.writer(accessTokens, delimiter=";")

        listoftokens = []

        for bIdx, bRow in enumerate(BackEnd):
            timestamp1 = bRow[0]
            accessToken1 = bRow[1]
            servicescope1 = bRow[2]
            resource1 = bRow[3]
            rid1 = bRow[4]

            if accessToken1 not in listoftokens:
                listoftokens.append(accessToken1)
                accessTokens.writerow([accessToken1])
