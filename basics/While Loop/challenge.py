chances = 3
score = 0
question = {
    1: {"question": "10 + 10 = ?", "answer": 20},
    2: {"question": "10 * 10 = ?", "answer": 100},
    3: {"question": "50 / 2 = ?", "answer": 25},
    4: {"question": "20 - 10 = ?", "answer": 10},
    5: {"question": "12 + 12 = ?", "answer": 24},
}

index = 1  # Starting index for the questions
while chances > 0 and index <= len(question):
    q = question[index]  # Access the current question using the index
    print(f"Chances: {chances}")
    user_answer = int(input(f"{q['question']} "))
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        chances -= 1
    index += 1  # Move to the next question

print(f"Final Score: {score}/{len(question)}")
print("Game Over!")
