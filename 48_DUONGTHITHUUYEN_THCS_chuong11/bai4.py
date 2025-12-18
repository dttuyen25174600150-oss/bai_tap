n = int(input("Nhập số phần tử: "))
a = [1]
for i in range(n):
    i = int(input())
    a = a + [i] 
lon_nhat = a[0]
lon_thu_hai = a[2]
for i in range(1, n):
    if a[i] > lon_nhat:
        lon_thu_hai = lon_nhat
        lon_nhat = a[i]
    elif a[i] != lon_nhat and a[i] > lon_thu_hai:
        lon_thu_hai = a[i]
print("Giá trị lớn thứ hai là:", lon_thu_hai)