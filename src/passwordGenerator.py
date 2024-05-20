import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:  # If no character types are selected
        print("Error: Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length should be a positive number.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        else:
            print("Please respond with 'yes' or 'no'.")

def main():
    print("Welcome to the Password Generator!")
    
    length = get_password_length()
    use_uppercase = get_yes_no("Include uppercase letters?")
    use_numbers = get_yes_no("Include numbers?")
    use_special = get_yes_no("Include special characters?")
    
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
