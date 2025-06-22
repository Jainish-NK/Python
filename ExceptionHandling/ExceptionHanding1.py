try:
    no1 = int(input("enter no1 : "))
    no2 = int(input("enter no2 : "))
    ans = no1/no2
    print(f"ans = {ans}")

except ZeroDivisionError as e:
    print(f"Cannot divide by zero")
    #print(f"{e}")

except ValueError as e:
    print(f"{e}")

except Exception as e:
    print(f"{e}")