import random

common_passwords = ["123456", "password", "12345678", "qwerty", "abc123", "111111"]

def check_password(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if password in common_passwords:
        print("This is a very common password. Please choose a different one.")
        return

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    print("\n--- Password Check ---")
    if length < 8:
        print("Missing: At least 8 characters")
    if not has_upper:
        print("Missing: Uppercase letter (A-Z)")
    if not has_lower:
        print("Missing: Lowercase letter (a-z)")
    if not has_digit:
        print("Missing: A number (0-9)")
    if not has_special:
        print("Missing: A special character (!@#$%^&*)")

    if score <= 2:
        print("\nPassword Strength: WEAK")
        print("Tip: Add uppercase letters, numbers, and special characters.")
    elif score <= 4:
        print("\nPassword Strength: MEDIUM")
        print("Tip: Add more variety to make it stronger.")
    else:
        print("\nPassword Strength: STRONG")
        print("Great password!")

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    for i in range(12):
        password += random.choice(chars)
    print("Suggested strong password:", password)

# Main program
print("=== Password Strength Checker ===")

while True:
    print("\n1. Check password strength")
    print("2. Generate a strong password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter your password: ")
        check_password(password)
    elif choice == "2":
        generate_password()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")