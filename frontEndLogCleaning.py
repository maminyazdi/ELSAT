# SQL Command to extract logs from DB server
"""
 SELECT
    [Time]
    ,[AccessToken]
    , SUBSTRING([Resource], CHARINDEX('#', [Resource]) , 800) AS Page
    , SUBSTRING([Method], CHARINDEX('#', [Method]) , 800) AS Method
    ,[Counter] AS Rid
  FROM [oauth].[dbo].[ClientLog] WITH (NOLOCK)
  WHERE Time > '2019-08-08'
"""

import csv
import config


def cleanfrontendlog():
    print(">>>>>> Running front end log cleaning process...")
    with open(config.originalFrontEndLog, 'r',
              encoding='utf-8') as originalCSV, \
            open(config.cleanFrontEndLog, "w", encoding='utf-8',
                 newline='') as newCSV:

        csvFileVec = csv.reader(originalCSV, delimiter=";")
        csvWriter = csv.writer(newCSV, delimiter=";")

        # next(csvFileVec)
        csvFileVec = list(csvFileVec)
        inputCount = 1
        outputCount = 1
        for idrow, csvRow in enumerate(csvFileVec[1:]):
            inputCount += 1

            time = csvRow[0]
            accessToken = csvRow[1]
            page = csvRow[2]
            method = csvRow[3]
            rid = csvRow[4]

            method = initial_clean_method(method)
            #method = clean_method1(method)

            if '?' in page:
                questionMarkIndex = page.index('?')
                substringRight = page[questionMarkIndex:]
                substringLeft = page[:questionMarkIndex]
                if substringRight.find('schemaId') > 0 and substringRight.find('ota') > 0:
                    page = page.replace(page, substringLeft + "-OtaId-MetadataSchemaId-")
                elif substringRight.find('schemaId') > 0:
                    page = page.replace(page, substringLeft + "-MetadataSchemaId-")
                elif substringRight.find('ota') > 0:
                    page = page.replace(page, substringLeft + "-OtaId-")
                elif "pid" in substringRight:
                    page = page.replace(page, substringLeft + "-PID-")
                elif "pubid" in substringRight:
                    page = page.replace(page, substringLeft + "-PublicationId-")
                elif "fileId" in substringRight:
                    page = page.replace(page, substringLeft + "-FileId-")

                page = page.replace(page, substringLeft + "-")

            elif 'https://' in page:
                page = page.replace(page, "")
            elif '?' not in page:
                page = page.replace(page, page + "-")

            pageMethod = page + method
            # PCC 97-1
            pageMethod = clean_method1(pageMethod)
            # PCC 94-97
            pageMethod = clean_method2(pageMethod)
            # PCC 91-94
            pageMethod = clean_method3(pageMethod)
            # PCC 82-85
            pageMethod = clean_method4(pageMethod)
            # PCC 79-82
            pageMethod = clean_method5(pageMethod)
            # PCC 53-56
            pageMethod = clean_method6(pageMethod)
            # PCC 41-44
            pageMethod = clean_method7(pageMethod)
            # PCC 23-26
            pageMethod = clean_method8(pageMethod)

            csvWriter.writerow([time, accessToken, pageMethod, rid])
            outputCount += 1

        print("Input # rows: %d" % inputCount)
        print("Ourput # rows: %d" % outputCount)


def initial_clean_method(methodValue):
    method = methodValue

    findMethods1 = ['']
    findMethods2 = ['#reupload_confirm','#uploadButton','acceptTOSArchiveButton','archiveButton']
    findMethods3 = ['#redirect_manage','#manage-tab','#archive-tab','#restore-tab','#submit-tab','#search-tab','noRefer','redirectSubmitPageButton','#simplearchive_navigation','#MetadataSearchLink2','#metadata_navigation']
    findMethods4 = ['saveMetadataButton','#save_button']
    findMethods5 = ['deleteMetadataButton','#delete_confirm']
    findMethods6 = ['btn.btn-success.restoreBtn','restoreButton']
    findMethods7 = ['tableEntry','metadata-col-visibility']
    findMethods8 = ['/html/body/div[3]/div[6]/div.container']
    findMethods9 = ['#accept-tos']
    findMethods10 = ['select2']
    findMethods11 = ['language-box']
    findMethods12 = ['schemaSelected','schemaIdBtn','#schema_rendered']
    findMethods13 = ['downloadButton']
    findMethods14 = ['#search_button']
    findMethods15 = ['updateFileMetadataButton']
    findMethods16 = ['form-control.metadata_property']


    if any(forbidStr in method for forbidStr in findMethods2):
        method = method.replace(method, "ArchiveFile")
    elif any(forbidStr in method for forbidStr in findMethods3):
        method = method.replace(method, "RedirectPage")
    elif any(forbidStr in method for forbidStr in findMethods4):
        method = method.replace(method, "SaveMetadata")
    elif any(forbidStr in method for forbidStr in findMethods5):
        method = method.replace(method, "DeleteMetadata")
    elif any(forbidStr in method for forbidStr in findMethods6):
        method = method.replace(method, "RestoreFile")
    elif any(forbidStr in method for forbidStr in findMethods7):
        method = method.replace(method, "SelectEntry")
    elif any(forbidStr in method for forbidStr in findMethods8):
        method = method.replace(method, "container")
    elif any(forbidStr in method for forbidStr in findMethods9):
        method = method.replace(method, "AcceptTOS")
    elif any(forbidStr in method for forbidStr in findMethods10):
        method = method.replace(method, "LoadDropDown")
    elif any(forbidStr in method for forbidStr in findMethods11):
        method = method.replace(method, "ChangeLanguage")
    elif any(forbidStr in method for forbidStr in findMethods12):
        method = method.replace(method, "SelectSchema")
    elif any(forbidStr in method for forbidStr in findMethods13):
        method = method.replace(method, "DownloadFile")
    elif any(forbidStr in method for forbidStr in findMethods14):
        method = method.replace(method, "SearchFile")
    elif any(forbidStr in method for forbidStr in findMethods15):
        method = method.replace(method, "UpdateFileMetadataButton")
    elif any(forbidStr in method for forbidStr in findMethods16):
        method = method.replace(method, "LoadMetadataContent")
    return method

def clean_method1(methodValue):
    method = methodValue
    findMethods1 = ['RedirectPage']
    findMethods2 = ['SelectEntry']
    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, '#search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage')
    elif any(forbidStr in method for forbidStr in findMethods2):
        method = method.replace(method, '#manage-SelectEntry&#search-SelectEntry')
    return method


def clean_method2(methodValue):
    method = methodValue
    # 96% Similarity
    findMethods1 = ['RedirectPage']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading
    return method

def clean_method3(methodValue):
    method = methodValue
    # 93% Similarity
    findMethods1 = ['ChangeLanguage']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading&ChangeLanguage

    return method

def clean_method4(methodValue):
    method = methodValue
    # 84% Similarity
    findMethods1 = ['UpdateFileMetadataButton','container','RestoreFile']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading&ChangeLanguage&#restore-UpdateFileMetadataButton&#archive-container&#restore-RestoreFile

    return method

def clean_method5(methodValue):
    method = methodValue
    # 81% Similarity
    findMethods1 = ['#manage-SelectEntry&#search-SelectEntry']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading&ChangeLanguage&#restore-UpdateFileMetadataButton&#archive-container&#restore-RestoreFile&#manage-SelectEntry&#search-SelectEntry

    return method

def clean_method6(methodValue):
    method = methodValue
    # 53% Similarity
    findMethods1 = ['#submit-SaveMetadata']
    # 55% Similarity
    findMethods2 = ['#archive-ArchiveFile']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    elif any(forbidStr in method for forbidStr in findMethods2):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading&ChangeLanguage&#restore-UpdateFileMetadataButton&#archive-container&#restore-RestoreFile&#manage-SelectEntry&#search-SelectEntry&#archive-ArchiveFile&#submit-SaveMetadata

    return method

def clean_method7(methodValue):
    method = methodValue
    # 41% Similarity
    findMethods1 = ['#submit-SelectSchema','#search-SearchFile']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, '#submit-SelectSchema&#search-SearchFile')

    return method

def clean_method8(methodValue):
    method = methodValue
    # 23% Similarity
    findMethods1 = ['#submit-SelectSchema&#search-SearchFile']

    if any(forbidStr in method for forbidStr in findMethods1):
        method = method.replace(method, 'PageLoading')
    # #search-RedirectPage&#restore-RedirectPage&#manage-RedirectPage&#submit-RedirectPage&#archive-RedirectPage&PageLoading&ChangeLanguage&#restore-UpdateFileMetadataButton&#archive-container&#restore-RestoreFile&#manage-SelectEntry&#search-SelectEntry&#archive-ArchiveFile&#submit-SaveMetadata&#submit-SelectSchema&#search-SearchFile
    return method