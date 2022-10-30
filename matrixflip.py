from collections import defaultdict


cols = defaultdict(list)
mat =[
    [112, 42, 83, 119], 
    [56, 125, 56, 49], 
    [15, 78, 101, 43], 
    [62, 98, 114, 108]
    ]

mid = len(mat)//2
print("mid: ", mid)
for r in range(len(mat)):
    row = mat[r]
   

    if sum(row[:mid]) < sum(row[mid:]):
        mat[r] = row[::-1]

for current_r in range(len(mat)):
    for next_r in range(len(mat)):
        if sum(mat[next_r][:mid]) < sum(mat[current_r][:mid]):
            temp = mat[current_r]
            mat[current_r] = mat[next_r]
            mat[next_r] = temp
        
for r in mat:
    print(r)


a = [5,1, 5, 8, 10]
print("initial a: ", a)
for i in range(len(a)):
    for j in range(len(a)):
        if a[j] < a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp


print("after a: ", a)
