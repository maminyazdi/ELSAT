import pandas as pd
import config

def cleanMatrix():
    descriptive_matrix = pd.read_csv(config.combinedMatrix, sep=',')
    descriptive_matrix = descriptive_matrix.replace(['\[', '\]', ' '], ['', '', ''], regex=True)

    # Get names of indexes for which the first column has value 0
    indexNames = descriptive_matrix[descriptive_matrix["['Groups'"] == '0'].index
    # Delete these row indexes from dataFrame
    descriptive_matrix.drop(indexNames, inplace=True)



    descriptive_matrix.to_csv(config.combinedMatrix, index=False, sep=',')

