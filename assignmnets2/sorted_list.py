                

list1=[1,8,2,4,6,10,2,15,0]

Length=len(list1)
for loop in range(Length):
    for j in range(loop+1, Length):
        if list1[loop]<=list1[j]:
            continue
            
        else:
            list1[loop],list1[j]=list1[j],list1[loop]
print(list1)
           
            
            
        
        
    
    
    


    