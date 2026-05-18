#  AI Study Assistant (NLP-Based Learning Tool)

##  Overview

AI Study Assistant is a Python-based educational tool that uses basic Natural Language Processing (NLP) techniques to help students learn more effectively.
It can summarize notes, generate quizzes, detect topics, and provide feedback in multiple languages with voice support.

---

##  Features

*  Text Summarization (frequency-based NLP)
*  Quiz Generation (fill-in-the-blank)
*  Topic Detection (Math, Science, Computer)
*  Multilingual Feedback (English, Hindi, Korean, Japanese)
*  Voice Output (Text-to-Speech)
*  File Input Support (.txt)

---

##  Concepts Used

* Natural Language Processing (NLP)
* Tokenization (sentence & word level)
* Frequency Analysis
* Keyword Extraction
* Rule-Based AI Logic
* Text-to-Speech (TTS)

---

##  Technologies Used

* Python
* NLTK
* pyttsx3

---

##  Requirements

### 🔹 Python Version

* Python 3.8 or above

### 🔹 Libraries Required

* nltk
* pyttsx3

---

##  Installation

Install required libraries using pip:

```bash
pip install nltk pyttsx3
```

---

## ▶ How to Run

### Step 1: Download the project

Save the Python file `main.py` in a folder.

### Step 2: Open terminal / command prompt

Navigate to the project folder:

```bash
cd path_to_your_folder
```

### Step 3: Run the program

```bash
python main.py
```

---

##  How It Works

1. User chooses language
2. User inputs notes (manual or file)
3. System processes text using NLP:

   * Tokenization
   * Frequency analysis
4. Generates:

   * Summary
   * Quiz
   * Topic detection
5. User answers quiz
6. System evaluates performance and gives feedback

---

##  File Input Instructions

* Only `.txt` files are supported
* Example:

  ```
  notes.txt
  ```
* Enter full path when prompted:

  ```
  Enter file path: notes.txt
  ```

---

##  Limitations

* Does not deeply understand context (rule-based system)
* Quiz generation is simple (keyword-based)
* Topic detection depends on predefined keywords

---

##  Future Improvements

* Add Graphical User Interface (GUI)
* Use machine learning models for better accuracy
* Improve quiz generation (MCQ format)
* Add speech-to-text input
* Expand topic detection

---

##  Author

* GHANSHYAM KUMAR BARNWAL

---

##  Note

This project is designed as an undergraduate-level AI application to demonstrate practical use of NLP concepts in education.
