SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def convert_number(s:str) -> int:
    s = list(s.upper())
    numbers = []
    if len(s) == 1:
        return SYMBOLS[s]
    
    while len(s) >=1 :
        if len(s) > 1:
            if SYMBOLS[s[0]] >= SYMBOLS[s[1]]:
                numbers.append(SYMBOLS[s[0]])
                s.pop(0)
            else:
                numbers.append(SYMBOLS[s[1]] - SYMBOLS[s[0]])
                s.pop(0)
                s.pop(1)
        else:
            numbers.append(SYMBOLS[s[0]])
            s.pop(0)

    return sum(numbers)
            


print(convert_number("dc"))