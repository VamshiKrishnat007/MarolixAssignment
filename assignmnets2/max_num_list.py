def max_list_fun(int_list):
    Length=len(int_list)
    max_num=int_list[0]
    for loop in range(Length-1):
        if max_num>=int_list[loop+1]:
            max_num=max_num
        else:
            max_num=int_list[loop+1]
    return max_num



Input1=input().split(",")

int_list=list(map(int,Input1))

Result=max_list_fun(int_list)
print(Result)
