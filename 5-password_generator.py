import re
import string 
import secrets

def generate_password(length=16, nums=1, special_chars=1 , uppercase=1, lowercase=1):
    letters = string.ascii_letters
    symbols = string.punctuation
    digits = string.digits 

    all_characters = letters + digits + symbols

    while True:
        password = ""
        #Generate Password 
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),
            (special_chars, rf'[{symbols}]'),
            (uppercase , r'[A-Z]'),
            (lowercase , r'[a-z]')
            ]
        if all(
        contraint <= all(re.findall(pattern, password)) 
        for contraint , pattern in constraints):
            break
    return password 

if __name__ == "__main__":
    new_password = generate_password()
    print("Password Generated:", new_password)