m = int(input("Nhập số hàng của A: "))
n = int(input("Nhập số cột của A: "))
A = []
for i in range(m):
    dong = []
    for i in range(n):
        x = int(input(f"A[{i}][{i}]: "))
        dong = dong + [x]
    A = A + [dong]
n2 = int(input("Nhập số hàng của B: "))
p = int(input("Nhập số cột của B: "))
if n != n2:
    print("Không thể nhân hai ma trận")
else:
    B = []
    for i in range(n2):
        dong = []
        for i in range(p):
            x = int(input(f"B[{i}][{i}]: "))
            dong = dong + [x]
        B = B + [dong]
    C = []
    for i in range(m):
        dong = []
        for j in range(p):
            tong = 0
            for k in range(n):
                tong = tong + A[i][k] * B[k][j]
            dong = dong + [tong]
        C = C + [dong]
    print("Ma trận tích là:")
    for i in range(m):
        for ii in range(p):
            print(C[i][ii], end=" ")
        print()