marksheets = {"std1":{"maths":29,"sci":28,"drawing":30},"std2":{"maths":28,"sci":35,"drawing":30}}
print(marksheets)

for i,j in marksheets.items():
    print(i)
    for sub,marks in j.items():
        print(f"sub = {sub},marks = {marks}")
    print()

