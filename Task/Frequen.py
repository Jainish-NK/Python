s = "banana"
done = ""

for i in range(len(s)):
    ch = s[i]
    found = False
    for d in done:
        if ch == d:
            found = True
            break
    if found:
        continue

    count = 0
    for j in range(len(s)):
        if s[j] == ch:
            count += 1
    print(ch, ":", count)
    done += ch
