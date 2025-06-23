hisotry = [["yt","netflix","inst","yt","yt","prime"],["hotstar","yt","prime","netlifx"],
           ["yt","netflix","gpt","yt","yt","gpt"],["hotstar","yt","prime","google"]]


#remove yt from all day history

for x in hisotry:
    #x = ["yt","netflix","inst","yt","yt","prime"]
    i=0
    while i<len(x):
        if x[i] == "yt": #x[0] == "netflix"
            x.pop(i) 
        else:
            i += 1
print(hisotry)

