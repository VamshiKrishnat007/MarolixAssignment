Input1=int(input("Enter your age: \n"))
if Input1<=12:
    print("Child")
elif Input1>12 and Input1<20:
    print("Teenager")
elif Input1>=20 and Input1<60:
    print("Adult")
else:
    print("senior")