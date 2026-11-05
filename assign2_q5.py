x = input("Enter a string: ")

# Reverse the string
print("Reverse string:", x[::-1])

vowels = 0
consonants = 0

for ch in x:
    if ch.isalpha():          # Count only alphabets
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)