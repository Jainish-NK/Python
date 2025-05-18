a = b = c = 0

print("Vote (1 = A,2 = B,3 = C):\n")

for i in range(10):
    vote = int(input(f"Vote {i+1}: "))

    if vote == 1:
        a +=1
    elif vote == 2:
        b +=1
    elif vote == 3:
        c += 1
    else:
        print("Invalid vote! Skipped.")
        continue

print("\nRes:")
print("A =",a)
print("B =" ,b)
print("C =",c)

if a>b and a>c:
    print("Winner : A")
elif b>a and b>c:
    print("Winner : B")
elif c>a and c>b:
    print("Winner : C")
else:
    print("It's a tie!")