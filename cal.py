# Display the operation menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for the operation choice
choice = input("Enter choice (1/2/3/4): ")

# Take user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the operation based on user choice
if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input! Please choose a valid operation.")
