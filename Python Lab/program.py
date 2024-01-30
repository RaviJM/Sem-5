import schedule
import logging
import time


def dailyStandUpMeeting():
    logging.info("Daily stand-up meeting started.")
    print("Daily stand-up meeting at 9:00 AM for 15 minutes.")
    mins = 15*60
    time.sleep(mins)
    print("Daily stand-up meeting finished.")
    logging.info("Daily stand-up meeting finished.")
    

def teamCollaborationSession():
    logging.info("Team collaboration session started.")
    print("Team collaboration session at 11:00 AM for 1 hour.")
    mins = 60 * 60
    time.sleep(mins)
    print("Team collaboration session finished.")
    logging.info("Team collaboration session finished.")


def projectReviewMeeting():
    logging.info("Project review meeting started.")
    print("Project review meeting at 3:00 PM for 45 minutes.")
    mins = 45 * 60
    time.sleep(mins)
    print("Project review meeting finished.")
    logging.info("Project review meeting finished.")


def personalTrainingSession():
    logging.info("Personal training session at the gym started.")
    print("Personal training session at gym at 6:30 PM for 1 hour.")
    mins = 60 * 60
    time.sleep(mins)
    print("Personal training session at gym finished.")
    logging.info("Personal training session at the gym finished.")


logging.basicConfig(filename="D:\\COLLEGE\\Python Lab\\Theory\\Exam\\programLogFile.log", filemode="a", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


schedule.every().day.at("09:00").do(dailyStandUpMeeting)

schedule.every().monday.at("11:00").do(teamCollaborationSession)
schedule.every().wednesday.at("11:00").do(teamCollaborationSession)

schedule.every().friday.at("15:00").do(projectReviewMeeting)

schedule.every().tuesday.at("18:30").do(personalTrainingSession)
schedule.every().thursday.at("18:30").do(personalTrainingSession)

logging.info("program execution started")
print("program execution started")

while True:
    schedule.run_pending()
    time.sleep(1)
