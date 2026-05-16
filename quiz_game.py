score = 0
total = 30

questions = [
    {
        "question": "Q1. Which is the capital of India?",
        "a": "Mumbai",
        "b": "Delhi",
        "answer": "b",
        "correct": "Delhi"
    },
    {
        "question": "Q2. Formula of (a+b)²?",
        "a": "a² + b² + 2ab",
        "b": "a² + b² - 2ab",
        "answer": "a",
        "correct": "a² + b² + 2ab"
    },
    {
        "question": "Q3. National animal of India?",
        "a": "Lion",
        "b": "Tiger",
        "answer": "b",
        "correct": "Tiger"
    },
    {
        "question": "Q4. Smallest country in the world?",
        "a": "Vatican City",
        "b": "Monaco",
        "answer": "a",
        "correct": "Vatican City"
    },
    {
        "question": "Q5. Biggest country in the world?",
        "a": "Russia",
        "b": "China",
        "answer": "a",
        "correct": "Russia"
    },
    {
        "question": "Q6. Which planet is closest to the Sun?",
        "a": "Venus",
        "b": "Mercury",
        "answer": "b",
        "correct": "Mercury"
    },
    {
        "question": "Q7. How many bones in the human body?",
        "a": "206",
        "b": "208",
        "answer": "a",
        "correct": "206"
    },
    {
        "question": "Q8. Who invented the telephone?",
        "a": "Thomas Edison",
        "b": "Alexander Graham Bell",
        "answer": "b",
        "correct": "Alexander Graham Bell"
    },
    {
        "question": "Q9. What is the chemical symbol of water?",
        "a": "HO",
        "b": "H2O",
        "answer": "b",
        "correct": "H2O"
    },
    {
        "question": "Q10. Which is the largest ocean?",
        "a": "Atlantic Ocean",
        "b": "Pacific Ocean",
        "answer": "b",
        "correct": "Pacific Ocean"
    },
    {
        "question": "Q11. How many continents are there?",
        "a": "7",
        "b": "6",
        "answer": "a",
        "correct": "7"
    },
    {
        "question": "Q12. Which is the longest river in the world?",
        "a": "Amazon",
        "b": "Nile",
        "answer": "b",
        "correct": "Nile"
    },
    {
        "question": "Q13. Who is the father of computers?",
        "a": "Charles Babbage",
        "b": "Alan Turing",
        "answer": "a",
        "correct": "Charles Babbage"
    },
    {
        "question": "Q14. Which is the fastest animal on land?",
        "a": "Cheetah",
        "b": "Lion",
        "answer": "a",
        "correct": "Cheetah"
    },
    {
        "question": "Q15. How many players in a cricket team?",
        "a": "10",
        "b": "11",
        "answer": "b",
        "correct": "11"
    },
    {
        "question": "Q16. Which country invented chess?",
        "a": "China",
        "b": "India",
        "answer": "b",
        "correct": "India"
    },
    {
        "question": "Q17. What is the full form of CPU?",
        "a": "Central Processing Unit",
        "b": "Computer Processing Unit",
        "answer": "a",
        "correct": "Central Processing Unit"
    },
    {
        "question": "Q18. Which gas do plants absorb?",
        "a": "Oxygen",
        "b": "Carbon Dioxide",
        "answer": "b",
        "correct": "Carbon Dioxide"
    },
    {
        "question": "Q19. How many days in a leap year?",
        "a": "365",
        "b": "366",
        "answer": "b",
        "correct": "366"
    },
    {
        "question": "Q20. Who wrote the Ramayana?",
        "a": "Valmiki",
        "b": "Tulsidas",
        "answer": "a",
        "correct": "Valmiki"
    },
    {
        "question": "Q21. Which is the hardest natural substance?",
        "a": "Gold",
        "b": "Diamond",
        "answer": "b",
        "correct": "Diamond"
    },
    {
        "question": "Q22. How many colors in a rainbow?",
        "a": "7",
        "b": "6",
        "answer": "a",
        "correct": "7"
    },
    {
        "question": "Q23. Which planet is known as the Red Planet?",
        "a": "Jupiter",
        "b": "Mars",
        "answer": "b",
        "correct": "Mars"
    },
    {
        "question": "Q24. Who invented the light bulb?",
        "a": "Thomas Edison",
        "b": "Nikola Tesla",
        "answer": "a",
        "correct": "Thomas Edison"
    },
    {
        "question": "Q25. What is the full form of AI?",
        "a": "Automated Intelligence",
        "b": "Artificial Intelligence",
        "answer": "b",
        "correct": "Artificial Intelligence"
    },
    {
        "question": "Q26. Which language is used for AI development?",
        "a": "Python",
        "b": "HTML",
        "answer": "a",
        "correct": "Python"
    },
    {
        "question": "Q27. How many planets in our solar system?",
        "a": "9",
        "b": "8",
        "answer": "b",
        "correct": "8"
    },
    {
        "question": "Q28. Which is the smallest bone in human body?",
        "a": "Stapes (ear)",
        "b": "Femur",
        "answer": "a",
        "correct": "Stapes (ear)"
    },
    {
        "question": "Q29. Who is the founder of Microsoft?",
        "a": "Bill Gates",
        "b": "Steve Jobs",
        "answer": "a",
        "correct": "Bill Gates"
    },
    {
        "question": "Q30. What does RAM stand for?",
        "a": "Random Access Memory",
        "b": "Read Access Memory",
        "answer": "a",
        "correct": "Random Access Memory"
    }
]

print("=" * 40)
print("       WELCOME TO QUIZ GAME!")
print("    Total Questions: 30")
print("=" * 40)

for q in questions:
    print("\n" + q["question"])
    print("a)", q["a"])
    print("b)", q["b"])

    answer = input("\nYour answer (a/b): ").lower()

    if answer == q["answer"]:
        print("✓ Correct!")
        score += 1
    else:
        print("✗ Wrong! Correct answer is:", q["correct"])

    print("-" * 40)

print("\n" + "=" * 40)
print("         QUIZ COMPLETED!")
print("=" * 40)
print("Your Score:", score, "/", total)

percentage = (score / total) * 100
print("Percentage:", round(percentage, 1), "%")

if percentage == 100:
    print("PERFECT SCORE! GENIUS! 🏆")
elif percentage >= 90:
    print("Excellent! Outstanding! 🔥")
elif percentage >= 70:
    print("Good Job! Keep it up! 💪")
elif percentage >= 50:
    print("Average. Practice more!")
else:
    print("Keep Practicing! You got this!")

print("=" * 40)
