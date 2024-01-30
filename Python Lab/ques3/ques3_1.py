#counting number of unique Reviews and Food Items

import csv

fp = open("D:\\COLLEGE\\Python Lab\\ques3\\food_reviews.csv", "r")

fpreader = csv.reader(fp)

fields = next(fpreader)
list1 = enumerate(fields)

setOfFoodItems = set()

indexOfFoodItemColumn = 0
indexOfReviewsColumn = 0
reviewCounter = 0

for el in list1:
    if el[1] == "Food_Name":
        indexOfFoodItemColumn = el[0]
    if el[1] == "Review":
        indexOfReviewsColumn = el[0]

for row in fpreader:
    if row[indexOfFoodItemColumn] != '':
        set.add(setOfFoodItems, row[indexOfFoodItemColumn])
    if row[indexOfReviewsColumn] != '':
        reviewCounter += 1

print("Total number of Reviews are: ", reviewCounter)
print("Total number of unique Food Items are: ", len(setOfFoodItems), "   Which are: ", setOfFoodItems)
