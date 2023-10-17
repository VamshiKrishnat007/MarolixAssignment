def generate_2_combination(words):
    words=sorted(words)
    items=list(range(len(words)))
    # for loop in range(len(words)):
    combination1=[]
    for loop in items:
        combination1.append([loop])
    
    combination2=[]
    for i in combination1:
        for j in items:
            if j>i[-1]:
                combination2.append(i+[j])
    
    
    word_combinations=[]
    for combination in combination2:
        word_combination=[]
        for index in combination:
            word_combination.append(words[index])
        word_combinations.append(tuple(word_combination))
    return sorted(set(word_combinations))

        




words=input().split()
R=generate_2_combination(words)
for combination in R:
    print(" ".join(combination))
        
        
        #python is a programming language