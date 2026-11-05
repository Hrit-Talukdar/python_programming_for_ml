d = eval(input("Enter the dictionary: "))
result = {}
for key, value in d.items():
    if value not in result.values():
        result[key] = value

print("Dictionary after removing duplicate values:", result)