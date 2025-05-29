'''
calulator : add sub mul div

enter 1 for add
    a +b = 20
    print(20)
enter 2 for sub
enter 3 for mul
enter 4 for div

5 for get all answrs

condition: if list empty : user has not entered any operation yet.

if user is doing add:10,20,33
if user is doing mul : 100,300




5 number press
add: 3 times ans are : 10,20,33
mul : 2 times ans are : 100,300 
'''

# Result lists
add_res = []
sub_res = []
mul_res = []
div_res = []

# User-defined functions
def Add(no1, no2):
    res = no1 + no2
    add_res.append(res)
    return res

def sub(no1, no2):
    res = no1 - no2
    sub_res.append(res)
    return res

def mul(no1, no2):
    res = no1 * no2
    mul_res.append(res)
    return res

def div(no1, no2):
    if no2 == 0:
        print("Error: Division by zero!")
        return None
    res = no1 / no2
    div_res.append(res)
    return res

def display_res():
    if not (add_res or sub_res or mul_res or div_res):
        print("List empty: user has not entered any operation yet.")
    else:
        if add_res:
            print("Addition results:", add_res)
        if sub_res:
            print("Subtraction results:", sub_res)
        if mul_res:
            print("Multiplication results:", mul_res)
        if div_res:
            print("Division results:", div_res)

# Main loop
while True:
    print("\nEnter the choice:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show all results")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1 | 2 | 3 | 4:
            no1 = int(input("Enter number 1: "))
            no2 = int(input("Enter number 2: "))

            match choice:
                case 1:
                    print("Result (Addition):", Add(no1, no2))
                case 2:
                    print("Result (Subtraction):", sub(no1, no2))
                case 3:
                    print("Result (Multiplication):", mul(no1, no2))
                case 4:
                    result = div(no1, no2)
                    if result is not None:
                        print("Result (Division):", result)

        case 5:
            display_res()

        case 0:
            print("Exiting calculator...")
            break

        case _:
            print("Invalid choice. Please try again.")
