while True:
    num1 = (input())
    num2 = (input())

    try:
        num1=float(num1)
        num2=float(num2)
    except:
        print("Enter a Valid Number")
        continue

    Choose=input("Enter Arthematic Operation. (add/sub/multi/divd): ").lower()
    if Choose not in ["add","sub","multi","divd"]:
        print("Error : Enter valid input")
        continue

    else:
        print("Calculating...")
    
    if Choose == "add":
        print(num1+num2)
    elif Choose == "sub":
        print(num1-num2)
    elif Choose == "multi":
        print(num1*num2)
    else:
        if num2 == 0:
            print("cannot be divided by 0")
        else:
            print(num1/num2)
    ask=input("Continue? (yes/no)").lower()

    if ask == "yes":
        continue
    elif ask == "no":
        print("Program Ended.")
        break
    else:
        print("Invalid input. Exiting.")
        break

            
