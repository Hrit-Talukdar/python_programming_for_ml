A = set(eval(input("Enter first set: ")))
B = set(eval(input("Enter second set: ")))
print("First set:", A)
print("Second set:", B)
# Union
print("Union:", A | B)
# Intersection
print("Intersection:", A & B)
# Difference
print("A - B:", A - B)
print("B - A:", B - A)
# Symmetric Difference
print("Symmetric Difference:", A ^ B)
# Subset
print("A is subset of B:", A <= B)
print("B is subset of A:", B <= A)
# Superset
print("A is superset of B:", A >= B)
print("B is superset of A:", B >= A)
# Disjoint
print("A and B are disjoint:", A.isdisjoint(B))