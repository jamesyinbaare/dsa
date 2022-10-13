def check_palindrome(expr):
    if type(expr) == int:
        expr = str(expr)
    expr = list(expr.upper())
    str_len = len(expr)
    first_half = None
    second_half = None

    last = int(str_len/2)
    first_half = expr[:last]

    if str_len % 2 == 0:
        second_half = expr[-last:]
    else:
        second_half = expr[-last-1:]

    second_half = second_half[::-1]

    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            return False
    
    return True
    
    




print(check_palindrome("Tattarrattat"))
print(check_palindrome("Rotavator"))
print(check_palindrome("Detartrated"))
print(check_palindrome("Saippuakivikauppias"))
print(check_palindrome("James"))
print(check_palindrome(121))
print(check_palindrome(1211))