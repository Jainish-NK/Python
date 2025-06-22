with open("./File/logo.png","rb") as file:
    img_data = file.read()
    print(img_data)

with open("./File/logocpy.png","wb") as file:
    file.write(img_data)