'''
====== Chat Room Menu ======
1. Join Chat
2. Leave Chat
3. Show Active Users
4. Exit
Enter your choice (1-4): 1
Enter username to join: alice
✅ User 'alice' joined the chat.
'''
'''
print("====== Chat Room Menu ======")
print("1. Join chat")
print("2. Leave chat")
print("3. Show Active Users")
print("4. Exit")

activate_users = set()

while True:
    choice = input("Enter Your Choice (1-4) : ")
    if choice == '1':
        username = input("\nEnter The Username To Join chat ")
        if username in activate_users:
            print(f"❌ User '{username}' is already in the chat.")
        else:
            activate_users.add(username)
            print(f"✅ User '{username}' joined the chat.")        

    elif choice == '2':
        username = input("\nEnter The Username To Leave chat ")
        if username in activate_users:
            activate_users.remove(username)
            print(f"✅ User '{username}' left the chat.")
        else:
            print(f" user '{username}' is not in the chat.")

    elif choice == '3':
        username = input("\nEnter The Username To Show Active Users ")
        if activate_users:
            print("Active Users : ",activate_users)
        else:
            print("No active users in the chat.")
    
    elif choice == '4':
        username = input("\nEnter The Username To Exit chat ")
        print(f"❌ User '{username}' exited the chat.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
print("Thank you for using the chat room!")
'''

chatRoom = set({})
while True:
    choice = input("\n1. Join Chat\n2. Leave Chat\n3. Show Activate Users\n4. Exit\nEnter your Chat Room Choice (1-4) : ")

    match choice:
        case 1 : userName = input("\nEnter The UserName To Join chat : ")
                    if userName in chatRoom:
                         print(f"X User '{i}' is already in the chat.")
                    else:
                     