import pandas as pd 
from simpledbf import Dbf5
from src.appConfig import getAppConfigDict
from src.helperFunctions import generateFileNameSuffix
import os 
appConfig = getAppConfigDict()

pathyy_yy = appConfig["schd2021-2022"]
compSchFilesFolderPath = appConfig["compSchd2021-2022"]

fileNameSuffixList = generateFileNameSuffix(2021, 2022)
allFilesList = os.listdir(pathyy_yy)
count= 0

for fileName in fileNameSuffixList:
    sdl1FileName = 'sdl1' + fileName
    sdl2FileName = 'sdl2'  + fileName
    sdl21FileName = 'sdl21' + fileName
    sdl22FileName = 'sdl22' + fileName
    combine1MonthDf = pd.DataFrame()
    if sdl1FileName in allFilesList:
        sdl1Dbf =Dbf5(pathyy_yy + sdl1FileName )
        sdl1Df = sdl1Dbf.to_dataframe()
        #changing column 0th and 1st index with Date, and BLK
        sdl1Df.columns.values[0] = "Date"
        sdl1Df.columns.values[1] = "BLK" 
        sdl1Df.set_index(['Date', 'BLK'], inplace=True)
        combine1MonthDf = pd.concat([combine1MonthDf, sdl1Df], axis=1)
        # print(sdl1FileName)
        # count = count +1

    if sdl2FileName in allFilesList:
        sdl2Dbf =Dbf5(pathyy_yy + sdl2FileName )
        sdl2Df = sdl2Dbf.to_dataframe()
        #changing column 0th and 1st index with Date, and BLK
        sdl2Df.columns.values[0] = "Date"
        sdl2Df.columns.values[1] = "BLK" 
        sdl2Df.set_index(['Date', 'BLK'], inplace=True)
        combine1MonthDf = pd.concat([combine1MonthDf, sdl2Df], axis=1)
        # print(sdl2FileName)
        # count = count +1

    if sdl21FileName in allFilesList:
        sdl21Dbf =Dbf5(pathyy_yy + sdl21FileName )
        sdl21Df = sdl21Dbf.to_dataframe()
        #changing column 0th and 1st index with Date, and BLK
        sdl21Df.columns.values[0] = "Date"
        sdl21Df.columns.values[1] = "BLK" 
        sdl21Df.set_index(['Date', 'BLK'], inplace=True)
        combine1MonthDf = pd.concat([combine1MonthDf, sdl21Df], axis=1)
        # print(sdl21FileName)
        # count = count +1

    if sdl22FileName in allFilesList:
        sdl22Dbf =Dbf5(pathyy_yy + sdl22FileName )
        sdl22Df = sdl22Dbf.to_dataframe()
        #changing column 0th and 1st index with Date, and BLK
        sdl22Df.columns.values[0] = "Date"
        sdl22Df.columns.values[1] = "BLK" 
        sdl22Df.set_index(['Date', 'BLK'], inplace=True)
        combine1MonthDf = pd.concat([combine1MonthDf, sdl22Df], axis=1)
        # print(sdl22FileName)
        # count = count +1
    
    combine1MonthDf.reset_index(inplace=True)
    combine1MonthDf.to_excel(f'{compSchFilesFolderPath}sdl{fileName}.xlsx')
    # print(combine1MonthDf)