import ExceptionsFile

# Reading the input file
fr = open("D:\\COLLEGE\\Python Lab\\ques4\\req.txt", "r")

fd = open("D:\\COLLEGE\\Python Lab\\ques4\\Output.txt", "w")

finalMsg = ""

OS = ""
OS_Version = ""
Python_Version = ""
numpy_Version = ""
pandas_Version = ""
tensorflow = ""

lines = fr.readlines()
for line in lines:
    lst = line.strip()
    print(lst)

fr.close()
fd.close()