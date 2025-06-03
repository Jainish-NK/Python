def get_user(batch_size=10):
    total_user = 100
    for i in range(0,total_user,batch_size):
    #i=0
    #i=100

        batch=[]
        for j in range(i,min(i+batch_size,total_user)):
            batch.append(f"user{j}")
        yield batch

for b in get_user():
    print(b)