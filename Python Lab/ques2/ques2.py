import os
import shutil

SourcePath = "D:\\COLLEGE\\Python Lab\\ques2\\AllFiles\\"
DestinationPathForCopy = "D:\\COLLEGE\\Python Lab\\ques2\\CopiedFiles\\"
DestinationPathForMove = "D:\\COLLEGE\\Python Lab\\ques2\\MovedFiles\\"

list1 = os.listdir(SourcePath)

for file in list1:
    path = SourcePath + file
    fileName = file.split(".txt")

    if (int(fileName[0]) % 2 == 0):
        #even then copy
        shutil.copy(path,DestinationPathForCopy)
    else:
        #odd then move
        shutil.move(path,DestinationPathForMove)

print("Done successfully")
