noidung = "Python là một ngôn ngữ lập trình mạnh mẽ,dễ học và có nhiều ứng dụng.Nó được sử dụng rộng rãi trong phát triển web,khoa học dữ liệu,trí tuệ nhân tạo và tự động hóa.Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, với nhiều thư viện phong phú và giải quyết mội vấn đề "
with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write(noidung)
with open("vanban.txt", "r", encoding="utf-8") as f:
    data = f.read()
    words = data.split()
    print(f"Tổng số từ: {len(words)}")
tan_suat = {}
for word in words:
    word = word.strip(".,").lower()
    tan_suat[word] = tan_suat.get(word, 0) + 1

for k, v in tan_suat.items():
    print(f"{k}: {v}")