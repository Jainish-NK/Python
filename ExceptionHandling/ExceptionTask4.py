def validate_from():
    try:
        email = input("Enter your email : ")
        age = int(input("Enter your age : "))

        if "@" not in email:
            raise ValueError("Invalid email address.")
        age = int(age)
        if age <= 0:        
             raise ValueError("Age must be a number.")
        
        print("From submitted successfully!")
    
    except ValueError as e:
        print(e)
    finally:
        print("From Validation completed...")

validate_from()