strings = "mynameispranavandimok"

m = ["a","s","s","w","p","r","a","n","a","v","o","k"]


dicts = {}

for i in strings:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1
    

seen = set()

for j in m:
    if j in dicts:
        seen.add(f"{j} : {dicts[j]}")
    else:
        seen.add(f"{j} : 0")
        
for s in sorted(seen):
    print(s)
