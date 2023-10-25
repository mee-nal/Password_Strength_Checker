import string

def check_password_strength(password):
    common_passwords = set()
    with open("add your file path") as f:
        common_passwords.update(line.strip() for line in f)

    length = len(password)
    score = 0

    if password in common_passwords:
        print("Password was found in common list.")
        print(f"Score: {score}/7")
        return

    if length > 20:
        score += 4
    elif length > 17:
        score += 3
    elif length > 12:
        score += 2
    elif length > 7:
        score += 1

    characters = [c for c in password if c in string.ascii_letters + string.digits + string.punctuation]
    unique_chars = set(characters)

    if len(unique_chars) > 3:
        score += min(len(unique_chars) - 1, 3)

    print(f"Your password length is {length}, adding {score} points!")

    if score < 4:
        print("Your password is weak.")
    elif score == 4:
        print("Your password is OK.")
    elif 4 < score < 6:
        print("Your password is quite good enough.")
    else:
        print("Your password is strong!")

    print(f"Score: {score}/7")

password = input("Enter your password: ")
check_password_strength(password)
