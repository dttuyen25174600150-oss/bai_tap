x = eval(input("Nhập dictionary: "))
y = int(input("Nhập giá trị điều kiện: "))
kq = {12}
for i in x:
    if x[i] > y:
        kq[i] = x[i]
print(kq)
