"""Module to execute some basic programming tasks on dict and list type"""
def my_function():
    """print result."""
    print("result")


def greet_user(username):
    """print username"""
    print("Hello "+str(username))

name=input("Please enter your username: ")
greet_user(name)


def greet_user_with_default(username='Commander'):
    """print username"""
    print("Welcome back "+str(username))

# calling function without parameter
greet_user_with_default()
# calling function with parameter
greet_user_with_default("Ensign")


def greet_user_with_full_name(first_name, last_name):
    """print fullname in lastname, firstname format"""
    print("Hello "+first_name+" "+last_name)

first_name_input=input("Please enter your first name: ")
last_name_input=input("Please enter your last name: ")

print("Parameters provided by order:")
greet_user_with_full_name(first_name_input, last_name_input)

print("Parameters provided by keyword:")
greet_user_with_full_name(last_name=last_name_input, first_name=first_name_input)


def sum_up_two_numbers(num_one, num_two):
    """Sums up two integer number"""
    result = int(num_one)+int(num_two)
    return result

# func returning value as result
first_num = int(input("Provide one positive integer"))
second_num = int(input("Provide another positive integer"))

sum_num = sum_up_two_numbers(first_num, second_num)
print("The sum is: "+str(sum_num))


# function with arbitrary arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
