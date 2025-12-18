A = set(map(int, input("Nhập A: ").split()))
B = set(map(int, input("Nhập B: ").split()))

print("A không B:", A - B)
print("B không A:", B - A)
print("Giao:", A & B)
