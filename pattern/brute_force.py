def brute_force(text, pattern):
    l1 = len(text)
    l2 = len(pattern)

    for i in range(l1):
        for j in range(l2):
            if text[i+j] != pattern[j]: #
                break
            if j == l2-1:
                print(f"TEXT: {text[i:i+j+1]}  PATTERN: {pattern[:j+1]}")
                return i
            print(f"TEXT: {text[i:i+j+1]}  PATTERN: {pattern[:j+1]}")

print(brute_force('acbcabccababcaacbcac','acbcac'))