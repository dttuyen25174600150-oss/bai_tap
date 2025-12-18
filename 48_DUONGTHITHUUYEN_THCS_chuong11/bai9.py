n = int(input("Nhập n: "))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]
print("Tổng đường chéo phụ:", tong)
