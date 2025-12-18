a = list(map(int, input("Nhập danh sách: ").split()))
b = int(input("Nhập b: "))
for i in range :
    last = a[-1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last
print(a)
