def is_palindrome(val):
    val = str(val)
    sample = ''
    for i in range(len(val) - 1, -1, -1):
        sample += val[i]

    print(sample)
    return val == sample


print(is_palindrome(4432))

print(is_palindrome('racecar'))
