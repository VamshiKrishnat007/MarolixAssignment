def check_prime_num(Input1):
    count=0
    for loop in range(1,Input1+1):
        if Input1%loop==0:
            count+=1
    if count<=2:
        print("it's prime number")
    else:
        print("Not a prime number")



Input1=int(input("Enter Input: "))

Result=check_prime_num(Input1)
