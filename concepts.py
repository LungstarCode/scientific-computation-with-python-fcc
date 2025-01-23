import string 
import secrets
import re


def generate_password(length, nums, lowercase, uppercase, chars):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    pattern = letters + digits + special

    password = ''
    

    while True:   
        constraints = {
        (nums, r'\d'),
        (lowercase, r'[a-z]'),
        (chars, rf'[{special}]'),
        (uppercase, r'[A-Z]'),
    }

        for _ in range(length):
            password += secrets.choice(pattern)

        if all(
            contraint <= all(re.findall(pattern , password))

            for contraint , pattern in constraints):
                break
    return password


print(generate_password(16, 1,1 ,1,1))




