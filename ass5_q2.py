d=dict(eval(input("Enter the dictionary: ")))
s=[]
s1=[]
for a in d.keys():
    s.append(a)
for b in d.values():
    s1.append(b)
mv=s1[0]
mk=s[0]
for i in range(1, len(s)):
    if s1[i] > mv:
        mv=s1[i]
        mk=s[i]
print("The key that has max key value: ",mk)

'''Enter the dictionary: {'a':10, 'b':15, 'c':9, 'd':88, 'e':5}
The key that has max key value:  d'''