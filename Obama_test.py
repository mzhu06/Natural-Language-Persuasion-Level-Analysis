import csv
from persuasiveTool import textCheck
import numpy as np
import xlrd

sheetname = "Sheet"
modelName = ["LogisticRegression","LinearDiscriminantAnalysis","GaussianNB","SupportVectorMachine"]
# data = []
# result=[]
workbook = xlrd.open_workbook("ObamaSpeech.xlsx", on_demand=True)
sheet = workbook.sheet_by_name(sheetname)
arrayofvalues = sheet.col_values(2,1)

print("start print")
#iteration of the col
for item in arrayofvalues:
     print(item)
     data = []
     count = 0
     #go through 4 models
     out = open('Obama_012', 'a', newline='')
     for colResult in textCheck(item, modelName):
          #print the result of each model
          print(colResult)
          #count the first element in the result
          if colResult[0] == 1.0:
               count += 1

     #if statement to determine the output
     print("count:{}".format(count))

     if count >= 3:
          rowresult = 2
     elif count == 2:
          rowresult = 1
     else:
          rowresult = 0
     # print("count:")
     # print(count)
     print("pause,check rowresult")
     print(rowresult)
     print("#####################################")
     csv_write = csv.writer(out, dialect="excel")
     temp = [item, rowresult]
     csv_write.writerow(temp)
