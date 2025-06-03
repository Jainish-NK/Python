'''
decorators in python:
decorators are functions that modify the behavior of another function or method. without changing its code.
A decorator is a function that takes another function as an argument, extends its behavior, and returns a new function.
'''

def order_food(func): #3

    def inner(): #5
        print("ordering food") #6
        func() # 7throw_party()

    return inner #4 





@order_food #2
def throw_party(): #8
    print("throw party function called...") #9

throw_party() #1