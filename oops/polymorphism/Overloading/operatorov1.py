class Book:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        print(f"self {self.pages}")
        print(f"other {other.pages}")
        #return Book(self.pages + other.pages)
    
    def __sub__(self,nextobj):
        return self.pages - nextobj.pages
    

b1 = Book(100)
b2 = Book(200)

b3 = b1 + b2

b4 = b1 - b2
print(b4)

