dict1=dict(eval(input("Enter the 1st dictionary:")))
print(dict1)
dict2=dict(eval(input("Enter the 2nd dictionary:")))
print(dict2)
dict1.update(dict2)
print("After updation:")
print(dict1)


'''Enter the 1st dictionary:{'name':'hrit', 'age':20}
{'name': 'hrit', 'age': 20}
Enter the 2nd dictionary:{'roll':212}
{'roll': 212}
After updation:
{'name': 'hrit', 'age': 20, 'roll': 212}'''