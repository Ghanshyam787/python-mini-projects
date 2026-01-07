# -------------------- Return values and return Statements --------------------

import pyttsx3
import time

def speak(text, mood="neutral"):
    engine = pyttsx3.init()

    if mood == "most_happy":
        engine.setProperty('rate', 250)   # 🔥 very fast
        engine.setProperty('volume', 1.0)
        text = text.upper() + "!!!"       # excitement feel

    elif mood == "happy":
        engine.setProperty('rate', 175)
        engine.setProperty('volume', 1.0)

    elif mood == "sad":
        engine.setProperty('rate', 125)
        engine.setProperty('volume', 0.6)

    else:  # neutral
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.8)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("🎱 Let's play Magic 8 Ball game 🎱")
speak(" Let's play Magic 8 Ball game ")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Actually, you are wrong.', "sad"
    elif answerNumber == 2:
        return 'It is decidedly so!!', "happy"
    elif answerNumber == 3:
        return 'Yes, Yes, Yes! You are absolutely right!!!', "most_happy"
    elif answerNumber == 4:
        return 'You are too close.', "happy"
    elif answerNumber == 5:
        return 'Hey dude! Just try again..., okay', "nuteral"
    elif answerNumber == 6:
        return 'Concentrate and type again.', "sad"
    elif answerNumber == 7:
        return 'Outlook not so good.', "sad"
    elif answerNumber == 8:
        return 'No, I say, you are wrong.', "sad"
    elif answerNumber == 9:
        return 'No! No! No! You are absolutely wrong.', "neutral"
    else:
        return 'Please choose a number between one and nine.', "neutral"

while True:
    r = int(input('Choose a number between 1 to 9: '))
    text, mood = getAnswer(r)

    print(text)
    speak(text, mood)

    if r == 3:
        speak("Congratulations! Game over!", "happy")
        break
