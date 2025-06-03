def process_payment(func):

    def inner():
        print("proceesing Payment...")

        payment_successfully = True

        if payment_successfully:
            print("order conformed!")
            func()
        else:
            print("payment failed...")
    return inner

@process_payment
def place_order():
    print("placing your order...")

place_order()