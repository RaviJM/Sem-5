fp = open("D:\\COLLEGE\\Python Lab\\ques1\\readme.csv", "r")
fl = open("D:\\COLLEGE\\Python Lab\\ques1\\writeme.csv", "w")

lines = fp.readlines()

for line in lines:
    x = line.split("\n")
    y = x[0]
    z = y.split(',')
    ans = int(z[0]) + int(z[1])
    fl.writelines(str(ans))
    fl.writelines('\n')

print("Addition done successfully and result stored in another csv file!")
fp.close()
