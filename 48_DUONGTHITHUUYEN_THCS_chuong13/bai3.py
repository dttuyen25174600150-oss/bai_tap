numbers = [10, 20, 30, 40, 50, 66]

with open("so_nguyen.txt", "w") as f:
    for n in numbers:
        f.write(str(n) + "\n")
print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")