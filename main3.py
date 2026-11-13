print("Welcome to the Kmilo's Calculator! \n----------------------")

print("----------------------\nSelect number and operators alternately \n----------------------")

while True:

    result = float(input("Enter the first number: "))

    while True:
        
        operator = input(f"+ \n- \n* \n/ \n% \n=\n---------\n--- {result} ---\nEnter the operator: ")
        
        if operator == "=":
            print(f"The final result is: {result}")
            result = 0
            break
        elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "%":
            numberB = float(input("Enter the next number: "))
            if operator == "+":
                result += float(numberB)
            elif operator == "-":
                result -= float(numberB)
            elif operator == "*":
                result *= float(numberB)
            elif operator == "/":
                result /= float(numberB)
            elif operator == "%":
                result %= float(numberB)
            else:
                print("!!! Invalid operator. Please try again.")
                continue
        else:
            print("!!! Invalid operator. Please try again.")
            continue

    decition = str(input("Do you want to make another operation? (y/n): ")).lower()

    while decition not in ["y", "n"]:
        print("Invalid input. Try again...")
        decition = str(input("Do you want to make another operation? (y/n): ")).lower()

    if decition == "y":
        continue
    elif decition == "n":
        break
        
print("----------------------\nThanks for using Kmilo's Calculator!")