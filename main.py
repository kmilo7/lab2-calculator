while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
    print(f"The result of the Addition of {num1} and {num2} is: {result}")
    break

"""
print("Welcome to the Kmilo's Calculator! \n ----------------------")

while True:
    
    opt = input(("Please select an operation: (avoid using letters, symbols or spaces or 0)\
        \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulus\n---------\n"))

    while opt not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please try again.")
        opt = input(("Please select an operation: (avoid using letters, symbols, spaces or 0)\
            \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulus\n---------\n"))

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if opt == "1":
        ope = "Addition"
        result = float(num1) + float(num2)
    elif opt == "2":
        ope = "Subtraction"
        result = float(num1) - float(num2)
    elif opt == "3":
        ope = "Multiplication"
        result = float(num1) * float(num2)
    elif opt == "4":
        ope = "Division"
        result = float(num1) / float(num2)
    elif opt == "5":
        ope = "Modulus"
        result = float(num1) % float(num2)

    print(f"The result of the {ope} of {num1} and {num2} is: {result}")
    break

print("----------------------\nThanks for using Kmilo's Calculator!")"""