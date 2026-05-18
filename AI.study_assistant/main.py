import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import pyttsx3

# Download required data
nltk.download('punkt')
nltk.download('punkt_tab')

#-------------------------------------------------
#               VOICE ENGINE
#-------------------------------------------------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

#-------------------------------------------------
#               SIMPLE SUMMARIZER
#-------------------------------------------------
def summarize_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    words = [w for w in words if w.isalpha() and len(w) > 3]
    freq = Counter(words)

    sentence_score = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_score[sent] = sentence_score.get(sent, 0) + freq[word]

    summary = sorted(sentence_score, key=sentence_score.get, reverse = True)[:2]
    return " ".join(summary)

#--------------------------------------------------
#                  QUIZ GENERATOR
#--------------------------------------------------
def generate_quiz(text):
    sentences = sent_tokenize(text)
    quiz = []

    for sent in sentences[:5]:
        words = word_tokenize(sent)
        keywords = [w for w in words if w.isalpha() and len(w) > 4]

        if not keywords:
            continue

        answer = random.choice(keywords)
        question = sent.replace(answer, "_________")

        quiz.append({
            "question": question,
            "answer": answer
        })
    if len(quiz) == 0 and len(sentences) > 0:
        sent = sentences[0]
        words = word_tokenize(sent)
        if words:
            answer = words[0]
            question = sent.replace(answer, "_____")
            quiz.append({"question": question, "answer": answer})

    return quiz

# ---------------------------------------------------
#           TOPIC DETECTION (SIMPLE AI)
# ---------------------------------------------------

# Currntly optimized for English, but extendable.
def detect_topic(text):
    text = text.lower()

    math_words = ["equation", "algebra", "geometry",
                  "number"]
    science_words = ["force", "energy", "cell", "atom"]
    cs_words = ["python", "program", "algorithm", "data", "computer"]

    score = {"Math":0, "Science":0, "Computer":0}

    for word in math_words:
        if word in text:
            score["Math"] += 1

    for word in science_words:
        if word in text:
            score["Science"] += 1

    for word in cs_words:
        if word in text:
            score["Computer"] += 1

    if max(score.values()) == 0:
        return "Unknown"

    return max(score, key=score.get)

#-----------------------------------------------------
#              PERFORMANCE ANALYSIS
#-----------------------------------------------------

def analyze(score, total, lang="en"):
    accuracy = score / total

    if lang == "hindi":
        if accuracy > 0.8:
            return "बहुत बढ़िया प्रदर्शन!"
        elif accuracy > 0.5:
            return "अच्छा है, थोडा और अभ्याश करे"
        else:
            return "और मेहनत की जरुरत है"
        
    elif lang == "korean":
        if accuracy > 0.8:
            return "훌륭한 공연"
        elif accuracy > 0.5:
            return "좋아요, 좀 더 연습해 보세요"
        else:
            return "더욱 많은 노력이 필요합니다"
        
    elif lang == "japanese":
        if accuracy > 0.8:
            return "凄いね！"
        elif accuracy > 0.5:
            return "いいぞ、でももう少し練習しよう。"
        else:
            return "さらなる努力が必要だ。"
        
    else:
        if accuracy > 0.8:
            return "Excellent performance!"
        elif accuracy > 0.5:
            return "Good, but revise more."
        else:
            return "Need improvement."
        
# ----------------------------------------------------
#                   FILE INPUT
# ----------------------------------------------------
def read_file():
    print("\nFile Input Mode")
    path = input("Enter full file path (example: notes.txt): ").strip()

    if not path.endswith(".txt"):
        print("Only .txt files are supported.")
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if len(content) == 0:
                print("File is empty.")
                return None

            print("File loaded successfully!")
            return content

    except FileNotFoundError:
        print("File not found. Check path.")
    except Exception as e:
        print("Error reading file:", e)

    return None   
# ----------------------------------------------------
#                   MAIN PROGRAM
# ----------------------------------------------------
def main():
    print("===AI Study Assistant ===")

    lang_choice = input("Choose language (English / Hindi / Korean / Japanese) in lower case:").lower()

    # Multiple Notes Input
    choice = input("1. Type notes\n2. Use file\nChoose: ")

    all_notes = []

    if choice == "2":
        file_text = read_file()
        if file_text is None:
            print("File not found!")
            return
    
        all_notes.append(file_text)

    else:
        print("\nEnter Multiple notes (type END to finish):")

        while True:
            line = input()
            if line.upper() == "END":
                break
            all_notes.append(line)

    for text in all_notes:

        print("\n===================")
        print("Processing New Note")
        print("=====================")

        # Summary
        summary = summarize_text(text)
        print(summary)
        speak(summary)

        # Topic Detection
        topic = detect_topic(text)
        print("\nDetected Topic:", topic)

        # Quiz
        quiz = generate_quiz(text)
        

        if len(quiz) == 0:
            print("Not enough content to generate quiz.")
            speak("Not enough content to generate quiz")
            continue
        
        print("\n --- Quiz ---")
        score = 0

        for i, q in enumerate(quiz, 1):
            print(f"\nQ{i}: {q['question']}")
            speak(q['question'])

            ans = input("Your answer: ")

            if ans.lower() == q["answer"].lower():
                print("Correct")
                speak("Correct")
                score += 1
            else:
                print(f"Wrong! Answer: {q['answer']}")
                speak("Wrong")

        print(f"\nScore: {score}/{len(quiz)}")

    # Analysis
        print("\n--- Performance ---")
        result = analyze(score, len(quiz), lang_choice)
        print(result)

if __name__ == "__main__":
    main()