#prodct name : 
#prodyct price:
    
#product: pen
#price : 100
#--------------    
#product: pencil
#price : 200

with open("./File/productData.txt", "a") as f:
    while True:
        product = input("Enter product (or type exit to exit): ")
        if product.lower() == "exit":
            break

        price = int(input("Enter the price: "))
        f.write(f"product : {product}\n")  
        f.write(f"price : {price}\n")
