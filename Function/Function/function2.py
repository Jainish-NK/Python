# def add(a,b):
#     print("add function called...")
#     return a+b


def add(a,b)->str:
    print("add function called...")
    return a+b

ans = add(10,20)
print(ans)
print("ans = ",add(100,3000))
print("ans = ",add("ram","shyam"))