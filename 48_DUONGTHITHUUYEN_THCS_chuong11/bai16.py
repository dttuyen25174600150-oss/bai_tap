n = input("Nhập chuỗi: ")
a = {}
for i in n:
    if i in a:
       i[a] += 1
    else:
        i[a] = 1
print(a)

