#file udf object
#relative path , absolute path
#D:\royal\25fasttrackpython\filehandling/fileDemo1.py
#./file1.py


# file = open("demo1.txt","w")
# file = open("./File/demo1.txt","w")
# file.write("Hello this is first file from prog...")
# file.close()

with open("./File/demo2.txt","w") as file:
    file.write("Hello this is with...")

#reopen...
#file.writ("ok")   ValueError: I/O operation on closed file.  

