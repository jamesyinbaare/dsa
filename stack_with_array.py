size = 3
data = [0] *(size)

top = -1

def push(x):
    global top
    if top >= size-1:
        print("Stack Overflow")
    else:
        top = top +1
        data[top] = x

push("ham")
push("egg")
push("spam")

print(data[0: top+1])

push("new")
