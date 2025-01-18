import re 
import string 
import secrets



def password_gen(length = 16 , nums= 1, uppercase= 1, lowercase = 1, special_characters = 1):

    
    letters =  string.ascii_letters
    chars = string.punctuation
    numbers = string.digits 

    all_chars = letters + chars + numbers 
    password = ''

    for _ in range(length):
        password += secrets.choice(all_chars)
   
    while True: 

        constraints  = [
            (nums, r'\d'),
            (uppercase, r'[A-Z]' ),
            (lowercase, r'[a-z]'),
            (special_characters, rf'[{chars}]')
        ]

        if all( 
            constraint <= len(re.findall(pattern , password)) 
            for constraint , pattern in constraints 
        ):
            break
    return password
print("Generated password: ", password_gen())