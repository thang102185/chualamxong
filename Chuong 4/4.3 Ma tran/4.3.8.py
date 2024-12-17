n = int(input())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

is_upper = True
is_lower = True

for i in range(n):
    for j in range(n):
        if i > j and A[i][j] != 0:
            is_upper = False
        if i < j and A[i][j] != 0:
            is_lower = False

if is_upper:
    print("UPPER TRIANGLE")
elif is_lower:
    print("LOWER TRIANGLE")
else:
    print("NONE")
