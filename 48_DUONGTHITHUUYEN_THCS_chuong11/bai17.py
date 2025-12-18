a = eval(input("Nhập dictionary: "))
max_key = None
max_val = None
for i in a:
    if max_val is None or a[i] > max_val:
        max_val = a[i]
        max_key = i
print(max_key)
