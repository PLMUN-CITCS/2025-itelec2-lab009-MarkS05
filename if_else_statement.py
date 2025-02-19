user_input = input("Enter a number: 10")
number = int(user_input)
if number % 2 == 0:
    print("The number", number, "is Even.")
else:
    print("The number", number, "is Odd.")
try:
    #code here
except ValueError:
    print("Invalid input. Please enter an integer.")
