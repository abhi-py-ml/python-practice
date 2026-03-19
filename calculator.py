class Calculator:
    def __init__(self):
        self.history = []

    def user_input(self):
        while True:
            expression = input("Enter Expression: ").strip()

            if expression in ['history', 'exit']:
                return expression

            if any(ch.isalpha() for ch in expression):
                print("Enter valid expression!")
                continue

            return expression

    def show_menu(self):
        print("=" * 30)
        print("      CLI CALCULATOR")
        print("=" * 30)
        print("Use operators: +  -  *  /  **  %")
        print("history → Show history")
        print("exit    → Quit program")

    def calculate(self):
        while True:
            self.show_menu()

            operator = self.user_input()

            if operator == 'exit':
                print("Program ended")
                break

            elif operator == 'history':
                if not self.history:
                    print("History is empty")
                else:
                    for item in self.history:
                        print(item)
                continue

            try:
                result = eval(operator)
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
            except Exception:
                print("Invalid expression!")
                continue

            print("Result:", result)
            print("-" * 30)

            self.history.append(f"{operator} = {result}")



cal = Calculator()
cal.calculate()


            
                

        
        

        












    
        
    

      
