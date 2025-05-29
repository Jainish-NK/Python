def getUsers(user):
    print(user)

getUsers("jainish")
getUsers(["raj","jainish","vidhi","kunj"])

#args
def getStudents(*args):
    print(args)
getStudents()
getStudents("jainish","vidhi","kunj")


#  def test(*args,x):
#      print(args)
#      print(x)

def test(x,y,*args):
    print(args)
    print(x)
test(10,20,30,40)

