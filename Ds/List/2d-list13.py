'''
please entrt y for continue and 'n' for exit
y
enter movie name:
enter relese year:

please entrt y for continue and 'n' for exit
y

enter movie name:
enter relese year:
please entrt y for continue and 'n' for exit
n
[["chava",2025],["abc",2050],[]]
iteration :
for i,j in mopves:
'''

movie = []
while True:
    choice = input("\nplease enter 'y' for continue and 'n' for exit")
    
    if choice == 'y':
        name = input("\nEnter The Movie name : ")
        year = int(input("\nEnter The relese Year : "))

        movie.append([name,year])

    elif choice == 'n':
        break

    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print(movie)

# print("\nAll movie entered")
# for name,year in movie:
#    print(name,year)

