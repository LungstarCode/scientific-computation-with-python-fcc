
"""In this project, you are going to build a program that takes a camelCase or PascalCase formatted string as input and converts that to a snake_case formatted string using two approaches. First, you'll use a for loop and then list comprehension to achieve the same results. You'll see how list comprehension can make your code more concise."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []

    for char in pascal_or_camel_cased_string:

        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
