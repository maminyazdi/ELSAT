import pandas as pd
import config

def execute():

    #undersample the PageLoading & increase other rows to the number of second largest class

    descriptive_matrix =  pd.read_csv(config.combinedMatrix, sep=',')

    columnName = descriptive_matrix.columns.values[0]

    pageLoading_Matrix = descriptive_matrix[descriptive_matrix[columnName] == "'PageLoading'"]
    descriptive_matrix = descriptive_matrix[descriptive_matrix[columnName] != "'PageLoading'"]

    max_size = descriptive_matrix["['Groups'"].value_counts().max()
    lst = [descriptive_matrix]
    for class_index, group in descriptive_matrix.groupby("['Groups'"):
        lst.append(group.sample(max_size-len(group), replace=True))
    frame_new = pd.concat(lst)
    otherEventsDF = frame_new.sample(frac=1)

    pageLoadingDf = pageLoading_Matrix[:max_size].sample(frac=1)

    frames = [otherEventsDF,pageLoadingDf]

    cleanedCombinedMatrix = pd.concat(frames)
    cleanedCombinedMatrix = pd.DataFrame(cleanedCombinedMatrix).sample(frac=1)
    cleanedCombinedMatrix.to_csv(config.combinedMatrix, index=False, sep=',')


