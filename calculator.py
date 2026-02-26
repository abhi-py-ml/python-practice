def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except:
            print("Invalid number! Please try again.\n")


def calculate(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "multi":
        return num1 * num2
    elif operation == "divd":
        if num2 == 0:
            return "Cannot divide by 0"
        return num1 / num2


def main():
    while True:
        num1, num2 = get_numbers()

        operation = input("Enter operation (add/sub/multi/divd): ").lower()

        if operation not in ["add", "sub", "multi", "divd"]:
            print("Invalid operation!\n")
            continue

        result = calculate(num1, num2, operation)
        print("Result:", result)

        while True:
            ask = input("Continue? (yes/no): ").lower()
    
            if ask == "yes":
                break
            elif ask == "no":
                print("Program Ended.")
                return
            else:
                print("Invalid input. Please type yes or no.")

            
