#counting valid and invalid reviews

import csv

fp = open("D:\\COLLEGE\\Python Lab\\ques3\\food_reviews.csv", "r")

fpreader = csv.reader(fp)
next(fpreader)

totalRows = 0
invalidCounter = 0
for row in fpreader:
    totalRows += 1

    flag = 1
    for data in row:
        if data == '':
            flag = 0
            break
    if flag == 0:
        invalidCounter += 1

print("Total Rows are: ", totalRows)
print("Total invalid Rows are: ", invalidCounter)
print("Total valid Rows are: ", totalRows - invalidCounter)
