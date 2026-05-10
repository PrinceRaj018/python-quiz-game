score = 0

print("-" * 40)
print("(Quiz Time)\n")
print("-" * 40)

print("Q1. which is the capital of india ?")
print("a) Mumbai")
print("b) Delhi")

answer = input("\nquestion here: ")

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer is Delhi\n")

print("-" * 40)

print("Q2. which is formula (a+b)^2 ?")
print("a) a^2 + b^2 + 2ab")
print("b) a^2 + b^2 - 2ab")

answer = input("\nquestion here: ")

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer is (A)\n")

print("-" * 40)

print("Q3. national animal of india ?")
print("a) lion")
print("b) tiger")

answer = input("\nquestion here: ")

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer is tiger\n")

print("-" * 40)

print("Q4. Which is the Smallest Country in the world ?")
print("a) Vatican City")
print("b) Monaco")

answer = input("\nquestion here: ")

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer is Vatican City\n")

print("-" * 40)

print("Q5. Which is the biggest Country in the world ?")
print("a) Russia")
print("b) China")

answer = input("\nquestion here: ")

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct Answer is Russia\n")

print("Quiz is Completed\n")

print("=" * 40)

print("Your Score is:", score)

percentage = (score / 5) * 100

print("percentage:", percentage)

if percentage >= 90:
    print("Excellent!")

elif percentage >= 70:
    print("Good")

elif percentage >= 50:
    print("Average")

else:
    print("Keep Practicing!")

print("=" * 40)
