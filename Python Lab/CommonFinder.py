import os

mainPath = "D:\\COLLEGE\\Python Lab\\Practice\\Folders"
dict ={}
folders = os.listdir(mainPath)
for folder in folders:
    folderPath = os.path.join(mainPath, folder)
    files = os.listdir(folderPath)
    fileList = set()
    for file in files:
        fileList.add(file)
    dict[folder] = fileList

print(dict)
print(dict['G7'] & dict['G8'] & dict['G9'])