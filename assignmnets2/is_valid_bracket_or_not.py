def is_valid(s):
    stack = []
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        
        if char in bracket_map.keys():
            
            stack.append(char)
        elif char in bracket_map.values():
            if not stack or stack.pop()!= bracket_map[char]:
                return False
        else:
            return False

    return len(stack) == 0
print(is_valid("[]"))



    
    
    
    
    
    
    
    
    
    
    
    
    
    