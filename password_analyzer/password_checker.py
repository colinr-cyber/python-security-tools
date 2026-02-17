import string

def check_common_passwords(password):
    with open("common_passwords.txt", "r") as file:
        common_passwords = set(line.strip() for line in file)
    if password in common_passwords:
        exit("Password is too common. Please choose a different one.")
    return False

def check_password_strength(password):
    score = 0 
    length = len(password)

    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special_characters = any(char in string.punctuation for char in password)

    character_types = [uppercase, lowercase, digits, special_characters]

    if length < 8:
        exit("Password must be at least 8 characters long.")
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1    
    if length >= 16:
        score += 1
    if length >= 20:
        score += 1

    score += sum(character_types)

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter a password to check: ")
    check_common_passwords(password)
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

main()