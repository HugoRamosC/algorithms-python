def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 1:
        return True

    elif len(word) == 0 or word[low_index] != word[high_index]:
        return False

    elif low_index <= high_index:
        low_index += 1
        high_index -= 1
        return is_palindrome_recursive(word, low_index, high_index)

    return True
    # raise NotImplementedError
