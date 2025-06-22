#write mode : open --data over....
#write mode : if file not exits ... create -- write if file exits overri..

#with open("./File/ex1.txt","w") as file:
#   file.write("this is example run again....")

with open("./File/ex1.txt","a") as file:
    file.write("This is example run again...")


# users = ['ram',"shyam","amit","sumit","ajay","jaya"]
# with open("./File/users.txt","a") as file:
#     file.writelines(users)



users = ['ram',"shyam","amit","sumit","ajay","jaya"]
with open("./File/users.txt","a") as file:
    file.writelines(i + '\n' for i in users)

    