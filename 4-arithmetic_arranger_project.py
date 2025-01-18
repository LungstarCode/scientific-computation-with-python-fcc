def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Initialize storage for arranged lines
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operator, num2 = parts

        # Validate the operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Validate the operands
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Validate operand length
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Determine the width of the problem
        width = max(len(num1), len(num2)) + 2

        # Format the problem
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)

        # Calculate the answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))

    # Join the arranged parts with four spaces in between
    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    # Append answers if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
