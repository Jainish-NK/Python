for i in range(1,6):
    
    units = int(input(f"\nEnter The electricity units for House {i}: "))

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10
    
    print(f"\n House {i} Bill : {bill}\n")
