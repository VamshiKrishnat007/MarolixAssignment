year=int(input("Enter Year: \n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("its leap year")
        else:
            print("it's not a leap year")
    else:
        print("Its leap year")
else:
    print("Not a leap year")
