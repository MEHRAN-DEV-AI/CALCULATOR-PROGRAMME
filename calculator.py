def sum(a,b):
    sum1 = (a+b)
    print(f"THE SUM IS: {sum1} ")

def minus(a,b):
    minus= (a - b)
    print(f"THE MINUS IS: {minus} ")

def multiply(a,b):
    multiple= (a*b)
    print(f"THE MULTIPLE IS: {multiple} ")


def divide(a,b):
    if b == 0:
        print("Division by zero is not allowed. Please enter a non-zero number for the divisor.")
    else:
        div= a/b
        print(f"THE DIVIDE IS: {div} ")


if __name__ == "__main__":
    while True:
        try:
            a = int(input("ENTER 1ST NUMBER:  "))
            b = int(input("ENTER 2ND NUMBER: ")) 
            user = input("PLZ CHOOSE ONE OPERATOR:(+ , - , * , / ): ")
            
            if user == "+":
                sum(a, b)
            elif user == "-":
                minus(a, b)
            elif user == "*":
                multiply(a, b)
            elif user == "/":
                result = divide(a, b)
                if result is not None:
                  break  # Break out of the loop if division is successful
            else:
                print("ENTER VALID OPERATOR: ")
        
        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")
        except ZeroDivisionError:
            print("Division by zero is not allowed. Please enter a non-zero number for the divisor.")
    
        print("Calculation completed successfully.")
        