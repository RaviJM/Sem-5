import csv

fp = open("D:\\COLLEGE\\Python Lab\\Practice\\marks.csv", "r")
reader = csv.reader(fp)
arr=[]
counter = 0
for row in reader:
    counter += 1
    if (counter==1):
        continue

    avg = (int(row[2]) + int(row[3]) + int(row[4]))/3
    arr.append(avg)
fp.close()

filee=open("D:\\COLLEGE\\Python Lab\\Practice\\marks.csv", "a")
writee=csv.writer(filee)
# for row in writee:
    



# field = next(reader)
# print(field)