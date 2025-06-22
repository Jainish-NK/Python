try:
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    ans = no1/no2
    print(f"ans = {ans}")

except Exception as e:
    print(f"{e}")
    print(f"Can't divide by zero")

except ZeroDivisionError as e:
    print(f"Cannot divided by zero")
except ValueError as e:
    print(f"value error cls{e}")

    