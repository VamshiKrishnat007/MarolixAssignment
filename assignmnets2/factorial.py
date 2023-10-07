def factorial_fun(num1):
    result=1
    for loop in range(1,num1+1):
        result*=loop
    return result



num1=int(input("Enter number: \n"))
Result=factorial_fun(num1)
print("Factorial of "+str(num1)+" is "+str(Result))