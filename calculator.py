history=[]
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
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
    elif operation == "power":
        return num1 ** num2
    elif operation == "mod":
        return num1 % num2

def show_menu():
    print("\nChoose operation:")
    print("add   → Addition")
    print("sub   → Subtraction")
    print("multi → Multiplication")
    print("divd  → Division")
    print("power → Power")
    print("mod   → Modulus")
    print("history → Show history")
    print("exit → Quit program")

def main():
    while True:
        show_menu()
        

        operation = input("Enter operation : ").lower()
        if operation == "exit":
            print("program ended:")
            break
        if operation == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("\nCalculation History:")
                for item in history:
                    print(item)
            continue

        if operation not in ["add","sub","multi","divd","power","mod"]:
            print("Invalid operation!\n")
            continue

        num1, num2 = get_numbers()

        result = calculate(num1, operation, num2)
        print("Result:", result)

        history.append(f"{num1} {operation} {num2} = {result}")

        
            



main()
            
