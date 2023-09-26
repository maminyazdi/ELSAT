# SQL Command to extract logs from DB server
"""
    SELECT
      [Time]
    , [AccessToken]
    , [ServiceScope]
    , SUBSTRING([Resource], 59, CHARINDEX('?', [Resource]) - 59) AS Call
    , SUBSTRING([Resource], CHARINDEX('&_rid=', [Resource]) + 6, 7) AS Rid
FROM[oauth].[dbo].[Logging] WITH(NOLOCK)
WHERE Time > '2019-08-08 '
AND(AppIdLIKE('9b1e3f75-abdc-4fb7-b150-4a67fce968ff') OR AppId LIKE('96b2251a-f7bf-4115-a976-34324f4cdd36') )
"""

import csv
import config

def cleanbackendlog():
    print(">>>>>>Running back end log cleaning process...")
    with open( config.originalBackEndLog, 'r', encoding='utf-8') as originalCSV, \
         open( config.cleanBackEndLog, "w", encoding='utf-8', newline='') as newCSV:
        csvFileVec = csv.reader(originalCSV, delimiter=";")
        csvWriter = csv.writer(newCSV, delimiter=";")

        inputCount = 1
        

        next(csvFileVec)
        for csvRow in csvFileVec:

            time = csvRow[0]
            accessToken = csvRow[1]
            serviceScope = csvRow[2]
            resource = csvRow[3]
            rid = csvRow[4]
            if inputCount > 1:

                if "eScience/PID/" in resource and "ParseOTA" not in resource:
                    resource = resource.replace(resource, "eScience/PID/PidNumber")

                if "eScience/Archive/Store/" in resource:
                    resource = resource.replace(resource, "eScience/Archive/Store/FileName")



            csvWriter.writerow([time, accessToken, serviceScope, resource, rid])
            inputCount += 1

        print("Input # rows: %d" % inputCount)

