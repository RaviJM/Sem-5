# All highest rating food reviews with all columns data

import csv

fp = open("D:\\COLLEGE\\Python Lab\\ques3\\food_reviews.csv", "r")

fpreader = csv.reader(fp)

dict1 = dict()  #stores in the form: Food_Name: [Rating, Serial_Number]

fields = next(fpreader)
list1 = enumerate(fields)

for el in list1:
    if el[1] == "Rating":
        indexOfRatingColumn = el[0]
    if el[1] == "Food_Name":
        indexOfFood_NameColumn = el[0]
    if el[1] == "Serial_Number":
        indexOfSerial_Number = el[0]

for row in fpreader:
    if row[indexOfFood_NameColumn] != '' and row[indexOfRatingColumn] != '':
        foodName = row[indexOfFood_NameColumn]
        rating = float(row[indexOfRatingColumn])
        serialNumber = int(row[indexOfSerial_Number])
        tempList = [rating, serialNumber]

        if foodName not in dict1:
            dict1[foodName] = tempList
        else:
            if rating > dict1[foodName][0]: #then the value in dict1 gets replaced
                dict1[foodName] = tempList
fp.close()


# traverse again to print
fr = open("D:\\COLLEGE\\Python Lab\\ques3\\food_reviews.csv", "r")
frreader = csv.reader(fr)

serialList = []
for ele in dict1:
    serialList.append(dict1[ele][1])

serialList = sorted(serialList)
next(frreader)

print("Top ratings of all food items are:")

iterer = 0
for row in frreader:
    if iterer < len(serialList):    # to prevent out of range error
        rowNo = serialList[iterer]
    if int(row[indexOfSerial_Number]) == rowNo:
        print(row)
        iterer += 1

fr.close()