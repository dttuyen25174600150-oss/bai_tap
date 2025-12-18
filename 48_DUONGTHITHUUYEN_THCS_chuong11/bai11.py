n = int(input("Nhập kích thước ma trận : "))
ma_tran = []
for i in range(n):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập phần tử a[{i}][{j}]: "))
        dong = dong + [x]  
    ma_tran = ma_tran + [dong]


doi_xung = True
for i in range(n):
    for j in range(n):
        if ma_tran[i][j] != ma_tran[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break
if doi_xung:
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")