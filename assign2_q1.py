n=int(input("Enter marks: "))
if n>=95:
    print("Outstanding.")
elif n>=90 and n<95:
    print("Excellent.")
elif n>=85 and n<90:
    print("grade-A.")
elif n>=80 and n<85:
    print("grade-B.")
elif n>=75 and n<80:
    print("grade-C.")
elif n>=70 and n<75:
    print("grade-D")
else :
    print("Better luck next time.")
