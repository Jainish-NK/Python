print("Welcome To Cricket Game")
print("\nSelect Mode")
print("\n1.Single Mode")
print("\n2.Multi Mode")

mode = int(input("\nEnter The Mode(1/2): "))



match mode:
    case 1:
        print("You Selected single Player Mode: ")

        print("\nSeleted Difficulty : ")
        print("\n1..Hard")
        print("\n2..Medum")
        print("\n3..Easy")

        diff = int(input("\nEnter The Diffult Level: "))
        match diff:
            case 1 : 
                print("\nYou Selected Hard Diffulty: ")

            case 2 : 
                print("\nYou Selected Medum Diffylty: ")

            case 3 : 
                print("\nYou Selected Easy Diffulty: ")

            case _:
                print("\nInvalid Diff:")


    case 2:
        print("You Selected Multi Player Mode: ")

        print("\nSeleted Difficulty : ")
        print("\n1..Hard")
        print("\n2..Medum")
        print("\n3..Easy")

        diff = int(input("\nEnter The Diffult Level: "))
        match diff:
            case 1 : 
                print("\nYou Selected Hard Diffulty: ")

            case 2 : 
                print("\nYou Selected Medum Diffylty: ")

            case 3 : 
                print("\nYou Selected Easy Diffulty: ")

            case _:
                print("\nInvalid Diff:")