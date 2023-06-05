def is_palindrome_iterative(word):
    if len(word) == 1:
        return True

    elif len(word) == 0:
        return False
    
    low_index = 0
    high_index = -1
    middle = len(word) // 2
    
    while low_index <= middle:
        if word[low_index] != word[high_index]:
            return False
        
        low_index += 1
        high_index -= 1
        
    return True
    # raise NotImplementedError
