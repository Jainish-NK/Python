name = input("\nEnter The Name : ")
addhyphone = ""

for ch in name:
    if ch == ' ':
        addhyphone += '-'
    else:
        addhyphone += ch

print("Res : ",addhyphone)