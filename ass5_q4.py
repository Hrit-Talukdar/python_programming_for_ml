s = set(eval(input("Enter the set: ")))
new_set = set()
for element in s:
    new_set.add(element)
print("Original set:", s)
print("New set:", new_set)