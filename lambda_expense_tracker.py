"""This project using lambda functions in python to build an expenses tracker"""
"""
# first, we will ook at how lists work, for revision 
my_list = [1, 2]

my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

my_list.insert(1, 1)
print(my_list)

my_list.pop()
print(my_list)  """

#lets start building the expenses app 

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount , 'category': category})

def print_expenses(expense):
    print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def total_expenses(expenses):
    return sum(map(lambda expense : expenses['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []

    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
            
# lambda are simple unknownimous functions that are idea for one time jobs .. here is an example 

test = lambda x: x *2 
# to test it 
#print(test(3))
#print(test(4))

