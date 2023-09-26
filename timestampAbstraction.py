import csv
import config
import numpy as np

def abstractLogs():
    with open(config.abstractedCombinedLog, "w", encoding='utf-8', newline='') as abstractedCombinedLog,\
         open(config.combinedLog, "r", encoding='utf-8', newline='') as combinedLog,\
         open(config.combinedLogFull, "w", encoding='utf-8', newline='') as combinedLogFull:

        abstractedCombinedLog = csv.writer(abstractedCombinedLog, delimiter=";")
        combinedLogFull = csv.writer(combinedLogFull, delimiter=";")
        combinedLog = csv.reader(combinedLog, delimiter=";")

        combinedLog = list(combinedLog)

        combined_rows = ["", "", "", ""]
        last_row = []
        last_event = ""
        updateFirstrow = True
        abstractedCombinedLog.writerow(["time:timestamp","case:concept:name","Resource","Activity"])
        combinedLogFull.writerow(["time:timestamp","time:timestamp","case:concept:name","Resource","Activity"])
        for idx, row in enumerate(combinedLog):

            timestamp = row[0]
            access_token = row[1]
            service = row[2]
            event = row[3]

            if idx == 0:
                last_event = event

            # if same event
            if last_event == event:
                if updateFirstrow:
                    first_row = [timestamp, access_token, service, event]
                    abstractedCombinedLog.writerow(first_row)
                    combined_rows[0] = first_row[0]
                    updateFirstrow = False

                last_row = [timestamp, access_token, service, event]
            else:
                if len(last_row) > 0:
                    abstractedCombinedLog.writerow(last_row)
                    combined_rows[1] = last_row[0]
                    combined_rows[2] = last_row[1]
                    combined_rows[3] = last_row[3]
                    last_row = []

                if combined_rows[1] == "":
                    combined_rows[1] = combined_rows[0]
                    combinedLogFull.writerow(combined_rows)
                else:
                    combinedLogFull.writerow(combined_rows)
                    combined_rows = ["", "", "", ""]
                first_row = [timestamp, access_token, service, event]
                abstractedCombinedLog.writerow(first_row)
                combined_rows[0] = first_row[0]
                combined_rows[2] = first_row[1]
                combined_rows[3] = first_row[3]

                last_event = event