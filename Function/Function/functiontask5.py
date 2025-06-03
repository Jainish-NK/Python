'''
def pay_with_upi(user):
    print("UPI Payment method called...")
    return f" {user} paid {amount} using UPI"

def pay_with_card(user):
    print("Credit Card Payment method called...")
    return f" {user} paid {amount} using Credit Card"

def pay_with_wallet(user):
    print("Wallet Payment method called...")
    return f" {user} paid {amount} using Wallet"

def pay(method_function,user):
    print("Payment processing started...")
    return method_function(user)


user = input("Enter Your Name: ")
amount = int(input("Enter Amount to Pay: "))

data = None

if amount > 60000:
    data = pay(pay_with_card, user)
elif amount > 30000:
    data = pay(pay_with_upi, user)
elif amount > 1000:
    data = pay(pay_with_wallet, user)
else:
    data = "Amount too low for any payment method."

print("\nResult:", data)
'''


def acidic_soil_handler(soil):
    print("Acidic Soil Habdler called...")
    return f"For {soil}, add lime and grow crops like Rice , Potato, and Straeberry."

def neutral_soil_handler(soil):
    print("Neutral Soil Handler called...")
    return f"{soil} is ideal, You can grow Wheat , Maize , and Barely."

def alkaline_soil_handler(soil):
    print("Alaline Soil Handler called...")
    return f"{soil}, add gypsum and grow crops like Cotton, Barley, and Sugar beet."



def recommend(soil_fun,soil_type):
    print("\nRecommendation System Running...")
    return soil_fun(soil_type)

soil_type = input("Enter Soil Type (e.g. Caly , Sandy , Loamy)")
ph = float(input("Enter Soil pH Value (e.g. 5.5 7.0 , 8.5)"))

res = None

if ph < 6.5:
    res = recommend(acidic_soil_handler,soil_type)
elif 6.5 <= ph <= 7.5:
    res = recommend(neutral_soil_handler,soil_type)
elif ph > 7.5:
    res = recommend(alkaline_soil_handler,soil_type)
else:
    res = "Invalid pH value."

print("\nRes : ",res)