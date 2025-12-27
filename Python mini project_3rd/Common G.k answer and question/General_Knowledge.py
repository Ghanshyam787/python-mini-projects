            # Simple one word answer question
import time
import winsound
import pyttsx3
#------------Voice Engine Setup--------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)
#---------------Sound Effect-------------------
def correct_sound():
    winsound.Beep(2000, 600)

def wrong_sound():
    winsound.Beep(800, 1000)

def timeover_sound():
    winsound.Beep(400, 1400)

def warning_sound():
    winsound.Beep(1600,400) # last 5 sec buzzer
#-----------------Candidate details:---------------
print('\n--- General Knowledge Quiz ---\n')
print("Welcome to the Smart Quiz Game, Answer each question in 15 second.")
speak("Welcome to the Smart Quiz Game, Answer each question in 15 second.")
time.sleep(1)
print('Candidate details:')
name = input('Candidate name = ')
Father_name = input("Father's name = ")
Mother_name = input("Mother's name = ")
Email = input('Email id = ')

print('\n')
print("Welcome "+ name)

speak("Welcome "+ name)
time.sleep(0.3)

print("Let us go to start quiz game")
speak("Let us go to start quiz game")
time.sleep(0.5)
print("\n")
#--------------------Quiz question------------------
Quiz = [
    {
        "type": "MCQ",
        "question": "Who is the first prime minister of India?",
        "option":"a) Shri Narendra Modi       b) Rajnath singh       c) Rajendra Prasad        d) Jawahar Lal Nehru",
        "answer": "Jawahar Lal Nehru"
    },
    {
        "type": "MCQ",
        "question":"Who is the first president of India?",
        "option":"a) Shrimati Draupadi murmu       b) Rajnath singh       c) Rajendra Prasad        d) Jwaharlal Nehru",
        "answer":"Rajendra Prasad"
    },
    {
        "type": "text",
        "question":"What is the full form of ATM?",
        "answer":"Automated Teller Machine"
    },
    {
        "type": "MCQ",
        "question":"What is the original colour of the Sun?",
        "option":"a) White        b) Red         c) Orange         d) Yellow",
        "answer":"White"
    },
    {
        "type": "text",
        "question":"What is the full of DNA?",
        "answer":"Deoxyribonucleic acid"
    },
    {
        "type": "MCQ",
        "question":"Which US agency work on space research?",
        "option":"a) ISRO       b) NASA       c) ESA       d) Roscosmos",
        "answer":"NASA"
    },
    {
        "type": "MCQ",
        "question":"Which is the famous cold region of Russia?",
        "option":"a) Sahara       b) Siberia       c) Alaska       d) Greenland",
        "answer":"Siberia"
    },
    {
        "type": "text",
        "question":"What is the full form of WHO?",
        "answer":"World Health Organisation"
    },
    {   "type": "MCQ",
        "question":"What is the boiling point of water?",
        "option":"a) 200        b) 75         c) 100         d) 50",
        "answer":"100"
    },
    {   "type": "MCQ",
        "question":"Which Sport was invented in England?",
        "option":"a) Cricket        b) Basketball         c) Hockey         d) Football",
        "answer":"Cricket"
    }
]

score = 0
Time_Limit = 15
# -----------------Quiz Loop----------------
# Loop and Range

for i in range(len(Quiz)):
    print("\nQ",i+1, Quiz[i]["question"])

    if Quiz[i]["type"] == "MCQ":
        print(Quiz[i]["option"])
    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()
    
    Time_Taken = end_time - start_time

    if Time_Taken > Time_Limit:
        print("Time Over")
        engine.say("time over")
        engine.runAndWait()
        time.sleep(0.5)
        timeover_sound()
        print("Correct Answer:", Quiz[i]["answer"])
        continue
    
    if user_answer.lower() == Quiz[i]["answer"].lower():
        print("Excellent, you are correct")
        engine.say("Excellent, you are correct")
        engine.runAndWait()
        correct_sound()
        score += 1
    else:
        print("Wrong answer!")
        engine.say("Wrong answer!")
        engine.runAndWait()
        wrong_sound()
        print("Correct answer:", Quiz[i]["answer"])

print("\n---Quiz Game Completed---\n")
print("Total Score:", score,"/", len(Quiz))
print("Total question", len(Quiz))
print("Total Correct Question: ", score)
