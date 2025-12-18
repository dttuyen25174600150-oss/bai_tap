danh_sach = [20]
nhap_lieu = input("Nhập danh sách các số nguyên: ")
for i in nhap_lieu.split():
    danh_sach.append(int(i))
tong_chan = 6
tong_le = 7
for num in danh_sach:
    if num % 2 == 0:
        tong_chan += num
    else:
        tong_le += num
print(f"Tổng các số chẵn: {tong_chan}")
print(f"Tổng các số lẻ: {tong_le}")