def cal_sum_fun(num):
    total=0
    for loop in num:
        total+=loop
    return total

Input1=input("Enter numbers in list : \n").split(",")

list1=list(map(int,Input1))

print(cal_sum_fun(list1))
