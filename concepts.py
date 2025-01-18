import re 

"This is a program that counts the number of words used in a sentence"

def word_count(sentence):
    search_pattern = r'\W'
    spaces = re.findall(search_pattern , sentence)

    return len(spaces) + 1


print(word_count("I woud like to go to school today ey"))


