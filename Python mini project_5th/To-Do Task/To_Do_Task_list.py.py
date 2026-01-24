
tasks = []
import pyttsx3
import time

def speak_text(text, speed ="normal"):
    engine = pyttsx3.init()
    if speed == "slow":
        engine.setProperty('rate', 140)
        engine.setProperty('volumn', 0.6)
    elif speed == "very slow":
        engine.setProperty('rate', 80)
        engine.setProperty('volumn', 0.4)       
    engine.say(str(text))
    engine.runAndWait()
    engine.stop()
    time.sleep(0.4)

speak_text("Enter your name", "slow")
name = input("Enter your name: ")

speak_text("Enter date", "slow")
Date = input("Enter date(DD/MM/YYYY): ")
while True:
    print("Enter your task: ")
    speak_text("Enter! your task!", 'slow')
    task = input()
    tasks.append(task)
    print("Do you want to add more task? (yes or no): ")
    speak_text("Do you want to add more task? (yes or no): ", 'slow')
    More_task =input()
    if More_task == "no":
        break

print("So",name + " your " + Date +" task list is")
speak_text("So!" + name +" Your " + Date +" task list is", "very Slow")
for task in tasks:
    print(task)
    speak_text(task)

speak_text("Good luck! have a nice day")