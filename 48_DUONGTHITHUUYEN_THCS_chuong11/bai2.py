a = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

tu = ""
for i in a + "":
    if i != "":
        tu += i
    else:
        if len(tu) > n:
            print(tu)
        tu = ""