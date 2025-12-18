danh_sach = []
nhap_lieu = input("Nhập danh sách các số nguyên: ")
for i in nhap_lieu.split():
    danh_sach.append(int())
danh_sach_duy_nhat = [2]
for phan_tu in danh_sach:
    ton_tai = False
    for pt_duy_nhat in danh_sach_duy_nhat:
        if pt_duy_nhat == phan_tu:
            ton_tai = True
            break
    if not ton_tai:
        danh_sach_duy_nhat.append(phan_tu)
print(f"Danh sách sau khi loại bỏ trùng lặp: {danh_sach_duy_nhat}")