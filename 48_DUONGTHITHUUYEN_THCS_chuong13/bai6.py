import csv
data = [
    {'ID': '1', 'Ten': 'An', 'Luong': 60000},
    {'ID': '2', 'Ten': 'Bình', 'Luong': 45000},
    {'ID': '3', 'Ten': 'Chi', 'Luong': 70000}
]
with open('nhan_vien.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['ID', 'Ten', 'Luong'])
    writer.writeheader()
    writer.writerows(data)
with open('nhan_vien.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Luong']) > 50000:
            print(f"NV: {row['Ten']} - Lương: {row['Luong']}")