import shutil
import os
import schedule
import time

def takeBackup():
    print("I'm called!")
    sourcePath = "D://COLLEGE//Python Lab//Practice//Scheduling//Files//"
    destinationPath = "D://COLLEGE//Python Lab//Practice//Scheduling//Backup//"

    listOfFiles = os.listdir(sourcePath)

    for file in listOfFiles:
        shutil.copy(sourcePath+file, destinationPath)
    print("All files copied!")


schedule.every(1).minutes.do(takeBackup)

for i in range(5):
    schedule.run_pending()
    time.sleep(1)
