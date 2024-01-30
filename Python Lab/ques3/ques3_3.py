# top 3 average rating of food

import csv

fp = open("D:\\COLLEGE\\Python Lab\\ques3\\food_reviews.csv", "r")

fpreader = csv.reader(fp)

dict1 = dict()

fields = next(fpreader)
list1 = enumerate(fields)

for el in list1:
    if el[1] == "Rating":
        indexOfRatingColumn = el[0]
    if el[1] == "Food_ID":
        indexOfFood_IDColumn = el[0]


for row in fpreader:
    if row[indexOfRatingColumn] != '' and row[indexOfFood_IDColumn] != '':
        rating = float(row[indexOfRatingColumn])
        food_ID = row[indexOfFood_IDColumn]
        if food_ID not in dict1:
            tempList = [rating,1]
            dict1[food_ID] = tempList
        else:
            dict1[food_ID][0] += rating
            dict1[food_ID][1] += 1


dict2 = dict()
for element in dict1:
    dict2[element] = dict1[element][0] / dict1[element][1]


sortedDict2 = sorted(dict2.items(), key=lambda x:x[1], reverse=True)

print("Top 3 food items are:")
for i in range(0,3):
    print(sortedDict2[i][0], " : ", sortedDict2[i][1])
