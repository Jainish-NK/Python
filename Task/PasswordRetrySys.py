correct_pass = "Jainish123"
attempts = 3

while attempts > 0:
    pwd = input("\nEnter The Password: ")

    if pwd == correct_pass:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print("Incorrect! Attempts left : {attempts}")

else:
    print("\nAccess Denied. You used all attempts.")

    