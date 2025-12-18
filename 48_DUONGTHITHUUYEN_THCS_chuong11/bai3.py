chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
trang_truoc = False

bat_dau = 0
for i in range(len(chuoi)):
    if chuoi[i] != ' ':
        bat_dau = i
        break

for i in range(bat_dau, len(chuoi)):
    if chuoi[i] != ' ':
        chuoi_moi += chuoi[i]
        trang_truoc = False
    else:
        if not trang_truoc:
            chuoi_moi += ' '
            trang_truoc = True

if chuoi_moi and chuoi_moi[-1] == ' ':
    chuoi_moi = chuoi_moi[:-1]

print(f"Chuỗi sau khi xử lý: {chuoi_moi}")