import string
import sys
from pathlib import Path


def check_common_passwords(password: str) -> None:
    base = Path(__file__).resolve().parent
    path = base / "common_passwords.txt"
    try:
        with path.open("r", encoding="utf-8") as file:
            common_passwords = set(line.strip() for line in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Common passwords file not found: {path}")
    if password in common_passwords:
        raise ValueError("Password is too common. Please choose a different one.")


def check_password_strength(password: str) -> str:
    score = 0
    length = len(password)

    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special_characters = any(char in string.punctuation for char in password)

    character_types = [uppercase, lowercase, digits, special_characters]

    if length < 8:
        raise ValueError("Password must be at least 8 characters long.")
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


def main() -> None:
    try:
        password = input("Enter a password to check: ")
        check_common_passwords(password)
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
    except (ValueError, FileNotFoundError) as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(1)


if __name__ == "__main__":
    main()