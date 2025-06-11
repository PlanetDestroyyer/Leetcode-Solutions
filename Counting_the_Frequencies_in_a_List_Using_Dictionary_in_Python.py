nums = [1,2,3,4,5,6,7,4,3,2,3]
m = [1,2,3,4,5,6,4,1,2,5,2,2,4,2,43,4,22,535,645,7,4242,4,42,5,53]
dicts = {}
for i in nums:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1
        
seen = set()
for i in m:
    if i in dicts:
        seen.add(f"{i} : {dicts[i]}")
    else:
        seen.add(f"{i} : 0")
    
for i in sorted(seen):
    print(i)
