class Demo:

    x = 100 #class level variable..
    print("x",x)

    def test(self):
        a = 10000 #local variable.... 
        print("hello this is test function....")
       # print(self)
        print(f"value of x : {self.x}")
        print(f"value of x = {Demo.x}")
        print(f"value of a = {a}")
        #print(f"value of x = {x}")
        self.name = "JAINISH"

    def myTest(self):
        #print(f"value of a = {self.a}") error
        print(f"value of name = {self.name}")

#object creation class
d = Demo() #[room 1]
d.test() #d.test(d) d.test(object)
#print(d)
print(f"value of x = {d.x}")
d.myTest()
print(d.name)