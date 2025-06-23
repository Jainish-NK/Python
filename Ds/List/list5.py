num = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []

for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


team =[["virat","batsman"],["pandya","all rounder"],["bumrah","bowler"],["ms","keeper"]]
print(team)
print(team[0])  # Accessing the first player's name
print(team[1][0])
team[1][1] = "batsman"
print(team)

for i in team:
    for j in i:
        print(j,end=" ")
    print()  # Print a new line after each player's details


for i,j in team:
    print(i," ",j)