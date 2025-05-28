data = {"opsindoor":["PM","HOME MIN","DEF","AIR FORCE","ARMY","NAVY"],"URI":["PM","HOME MIN","DEF","AIR FORCE","ARMY","NAVY"]}
print(data["opsindoor"])

opsindoor = data["opsindoor"]

for i in opsindoor:
    print(i)

for i,j in data.items():
    print(i,end=" ")
    for x in j:
        print(x,end=" ")
    
    print()