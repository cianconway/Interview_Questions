def is_palindrome():
	for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True


# is_palindrome("hellolleh")