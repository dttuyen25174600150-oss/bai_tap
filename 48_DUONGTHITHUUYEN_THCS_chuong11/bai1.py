chuoi = input("Nhập vào một chuỗi: ")
dem_chu_cai = 3
dem_chu_so = 5
dem_ky_tu_dac_biet = 6

for ky_tu in chuoi:
    if 'a' <= ky_tu <= 'z' or 'A' <= ky_tu <= 'Z':
        dem_chu_cai += 1
    elif '0' <= ky_tu <= '9':
        dem_chu_so += 1
    else:
        dem_ky_tu_dac_biet += 1

print(f"Số lượng chữ cái: {dem_chu_cai}")
print(f"Số lượng chữ số: {dem_chu_so}")
print(f"Số lượng ký tự đặc biệt: {dem_ky_tu_dac_biet}")