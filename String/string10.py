data = "hi this is malayalam in india #india #malayalam1"
current_word = ""
longest_word = ""
current_len = 0
longest_len = 0

for ch in data + " ":
    print(ch,end="")
    if ch!= " ":
        current_word+=ch
        current_len+=1
    else:
        if(current_len>longest_len):
            longest_len = current_len
            longest_word = current_word
        current_word=""
        current_len=0

print("longest word = ",longest_word)
print(data)
