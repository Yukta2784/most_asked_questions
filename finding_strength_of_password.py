s="test"
substrings=[]
c=0
for i in range(0,len(s)):
    for j in range(0,len(s)):
        substrings.append(s[i:j+1])
print(substrings)
for k in substrings:
    k=set(k)
    c=c+len(k)
        
print(    
print(c)


