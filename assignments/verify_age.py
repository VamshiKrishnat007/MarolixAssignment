input_Number=int(input("Enter age : \n"))
if input_Number<18:
    print("You are a minor")
elif input_Number<65:
    print("You are an adult")
else:
    print("You are a senior citizen")