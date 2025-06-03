#function as a object
def greet(name):
    return f"Hello {name}"

x = greet #()* no ()

message = x("Jainish") #function
print(message)
print(x("Kunj"))
