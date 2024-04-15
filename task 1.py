import random

# Define questions and answers for each difficulty level
questions_easy = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter"
}

questions_medium = {
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the tallest mammal on Earth?": "Giraffe"
}

questions_hard = {
    "In which year did World War I begin?": "1914",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the powerhouse of the cell?": "Mitochondria"
}

def quiz_game(difficulty):
    # Select questions based on difficulty level
    if difficulty == "easy":
        questions = questions_easy
    elif difficulty == "medium":
        questions = questions_medium
    elif difficulty == "hard":
        questions = questions_hard
    else:
        print("Invalid difficulty level.")
        return

    # Initialize score
    score = 0

    # Shuffle the questions
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    # Iterate through the questions
    for question in question_keys:
        answer = input(f"{question} ")
        if answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {questions[question]}")

    print(f"Quiz completed! Your final score is {score}/{len(questions)}")

# Main program
print("Welcome to the Quiz Game!")
print("Choose a difficulty level: easy, medium, or hard")
difficulty_level = input("Enter your choice: ")

quiz_game(difficulty_level.lower())
