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
    pass

# lambda are simple unknownimous functions that are idea for one time jobs .. here is an example 

test = lambda x: x *2 
# to test it 
#print(test(3))
#print(test(4))

