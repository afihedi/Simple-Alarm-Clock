from datetime import datetime
from playsound import playsound

alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

def check_time(alarm_time):
    if len(alarm_time) != 11:
        return "Incorrect format, Try again!"
    elif int(alarm_time[0:2]) > 12:
        return "Incorrect hour format, Try again!"
    elif int(alarm_time[3:5]) > 59:
        return "Incorrect minute format, Try again!"
    elif int(alarm_time[6:8]) > 59:
        return "Incorrect second format, Try again!"
    else:
        return "All good"

while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    checking = check_time(alarm_time)
    if checking != "All good":
        print(checking)
    else:
        print(f"Alarm is set for {alarm_time}...")
        break
hour = alarm_time[0:2]
min = alarm_time[3:5]
sec = alarm_time[6:8]
period = alarm_time[9:].upper()

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime("%I")
    current_min = current_time.strftime("%M")
    current_sec = current_time.strftime("%S")
    current_period = current_time.strftime("%p")

    if hour == current_hour and min == current_min and sec == current_sec\
            and period == current_period:
        print("Get Up!!")
        playsound('/Users/frankihediohanma/PycharmProjects/AlarmClock/full_of_love_romantic_alarm.wav')
        break

