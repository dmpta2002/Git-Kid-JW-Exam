import streamlit as st
import os 


# Define questions, choices, and correct answers
questions = [
    "What does the book of Genesis say about the origin of the universe?",
    "How old do scientists estimate the universe to be?",
    "How does the Bible describe the length of the creative periods?",
    "What does the Hebrew word for 'day' in the Bible refer to?",
    "What separated from the water, creating an open space, according to the Genesis story?",
    "What event allowed the day to be distinguished from the night in the Genesis story?",
    "What appeared after the water receded in the Genesis story?",
    "What did God create in the last period according to the Genesis story?",
    "According to the provided information, who built all things according to the Bible?",
    "What does the Bible offer logical and reasonable answers to, according to the text?"
]

choices = [
    ["A) It was created by scientists", "B) It started with the formation of Earth", "C) It was created by a creator mentioned in the Bible", "D) It is a myth and not to be believed"],
    ["A) One billion years old", "B) Fourteen billion years old", "C) One hundred years old", "D) One trillion years old"],
    ["A) Six days of twenty-four hours each", "B) Six days of different lengths", "C) Six months of continuous creation", "D) Six years of creative activity"],
    ["A) Only a twenty-four-hour period", "B) Periods of time of different lengths", "C) Only daytime", "D) Only nighttime"],
    ["A) Rocks", "B) Dense clouds", "C) Plants", "D) Animals"],
    ["A) Appearance of the sun", "B) Planting of trees", "C) Creation of animals", "D) Arrival of humans"],
    ["A) The sun", "B) The moon", "C) Dry land", "D) Mountains"],
    ["A) Plants", "B) Human beings", "C) Marine animals", "D) Birds"],
    ["A) Scientists", "B) Human beings", "C) God", "D) Jehovah's Witnesses"],
    ["A) Answers about science", "B) Answers about the purpose of life", "C) Answers about the future", "D) Answers about the internet"]
]

correct_answers = ["C", "B", "B", "B", "A", "A", "C", "B", "C", "B"]

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the video file
video_file = os.path.join(current_dir, r"C:\Users\dmpta\OneDrive\Documents\DISC-MAIN\Education\Git\Git Kid JW Exam\creadojw.mp4")

# Display the video
st.video(video_file) 

# Display questions and collect answers
answers = []
for i, question in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    user_answer = st.radio("", choices[i], key=f"{question}_answer")
    answers.append(user_answer.split(")")[0])

# Calculate grade
grade = sum([1 if a == c else 0 for a, c in zip(answers, correct_answers)])
total_questions = len(questions)
percentage = (grade / total_questions) * 100

# Display grade
if st.button("Submit"):
    st.write(f"## Your Grade: {grade}/{total_questions} ({percentage:.2f}%)")
