import os
import config
import pandas as pd
import numpy as np

from pm4py.objects.log.adapters.pandas import csv_import_adapter


def convertCSVtoXES():
    dataframe = csv_import_adapter.import_dataframe_from_path( config.abstractedCombinedLog, sep=";")

    #Adding new columns
    np.random.seed(0)
    sLength = len(dataframe['Activity'])
    conceptName = pd.Series(np.random.randn(sLength))
    resourceOrgName = pd.Series(np.random.randn(sLength))

    dataframe = dataframe.assign(conceptName= str(conceptName.values))
    dataframe = dataframe.assign(resourceOrgName= str(resourceOrgName.values))

    dataframe.rename(columns={'conceptName':'concept:name'}, inplace=True)
    dataframe.rename(columns={'resourceOrgName':'org:resource'}, inplace=True)

    #dataframe = str(dataframe['conceptName'])

    for index, row in dataframe.iterrows():

        rowActVal = row['Activity']
        newRowActVal = "'Activity':'"+rowActVal+"'"

        rowConceptNameActivity = row['concept:name']
        #newRowConceptNameActivity = "'concept:name':'"+rowActVal+"'"
        newRowConceptNameActivity = rowActVal

        rowCase = row['case:concept:name']
        newRowCaseVal = "'case:concept:name': '"+rowCase+"'"

        rowResource = row['Resource']
        newRowResource = "'Resource': '" + rowResource + "'"
        newRowResourceOrgName = "'org:resource': '" + rowResource + "'"

        rowTime = row['time:timestamp']
        strRowTime = rowTime.strftime("%Y-%M-%D %H:%M:%S.%f")
        newRowTimeVal = "'time:timestamp':Timestamp('"+strRowTime+"')"

        dataframe.at[index, 'Activity'] = newRowActVal
        dataframe.at[index, 'concept:name'] = newRowConceptNameActivity
        dataframe.at[index, 'Resource'] = newRowResource
        dataframe.at[index, 'org:resource'] = newRowResourceOrgName
        dataframe.at[index, 'case:concept:name'] = newRowCaseVal
        dataframe.at[index, 'time:timestamp'] = newRowTimeVal

    dataframe.to_csv(config.xesReadyFormatLog)
    return (dataframe)
