number_one = int(input("Write number one "))
number_two = int(input("Write number two "))
operation = input("Set the arithmetic operation ")

if operation == "+":
    print(number_one + number_two)
elif operation == "*":
    print(number_one * number_two)
elif operation == "-":
    print(number_one - number_two)
elif operation == "/":
    print(number_one / number_two)
else:
    print("You either did not write numbers or set a wrong arithmetic operation. Try again.")