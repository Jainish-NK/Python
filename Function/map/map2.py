sales = [100,200,300,400,903]

sales_list = list(map(lambda x : x*0.9,sales))
print(sales_list)

sales = [100,200,300,400,500,600,700]
dis = float(input("Enter The discount : "))

sales_list = list(map(lambda x : x*(1-dis/100)+1,sales))
print(sales_list)