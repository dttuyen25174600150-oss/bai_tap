a = list(map(int, input("Nhập danh sách: ").split()))
b = int(input("Nhập tổng cần tìm: "))
for i in range(len(a)):
    for i in range(i + 1, len(a)):
        if a[i] + a[i] == b:
            print(a[i], a[i])
