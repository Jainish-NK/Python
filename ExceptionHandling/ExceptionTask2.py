# create udf function accept *args as param and sum of all numners
# if args has anny other datatype except int raise TypeError with message "Only numbers are allowed"

def sumofnumbers(*args):
    try:
        for i in args:
            if type(i).__name__ != "int":
                raise TypeError("all data must be int")
            else:
                return sum(args)
    except TypeError as e:
        return e

x = sumofnumbers(10,"jay",20,30,50,60)    
print(f"{x}")
                

