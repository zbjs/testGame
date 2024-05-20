# import random

# def guess_number():
#     # Generate a random number between 1 and 10
#     secret_number = random.randint(1, 10)
#     attempts = 0

#     print("Welcome to the Number Guessing Game!")
#     print("I've picked a number between 1 and 10. Can you guess it?")

#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
#                 break
#         except ValueError:
#             print("Please enter a valid number.")

# if __name__ == "__main__":
#     guess_number()


import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
