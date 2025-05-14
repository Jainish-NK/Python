#scanf 
#cin 
#input function

#with para with argument
#input function always return string..

#no1 = int(input("enter value of no1 : "))
#print("value of no1 = ",no1+2)
#print("type of no1 = ",type(no1))

#pers = float(input("Enter value of pers : "))
#print("value of pers = ",pers)

#name = input("enter name")  
#print("name = ",name)


#-------------------------------------------------------------------------------------------------------------------------

#implicit Example

a = 5       # int
b = 2.5     # float

result = a + b  # Python implicitly converts 'a' to float

print(result)       # Output: 7.5
print(type(result)) # Output: <class 'float'>

#-----------------------------------------------------------------------------------------------------------------------

#Explicit Example

x = "100"
y = int(x)

print(y + 5)

x = "100.3"
y = float(x)

print(y+2.0)