def check_brackets(exp):
    brackets_list = []

    last =" "
    
    for ch in exp:
        if ch in ("{", "[", "("):
            brackets_list.append(ch)
        
        if ch in ("}","]",")"):
            last = brackets_list.pop()
            if last == "{" and ch == "}":
                continue
            elif last == "[" and ch == "]":
                continue
            elif last == "(" and ch == ")":
                continue
            else:
                return False
    
    if len(brackets_list) > 0:
        return False
    else:
        return True




print(check_brackets("(())"))
print(check_brackets("(())["))
print(check_brackets("(()){}"))
print(check_brackets("{(())}"))
print(check_brackets("{("))
print(check_brackets("))}"))
print(check_brackets("{"))