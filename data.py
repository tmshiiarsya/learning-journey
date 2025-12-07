import random

with open('data.txt', 'w') as f:
    for _ in range(20):
        angka = random.randint(1, 100)
        f.write(f"{angka}\n")

print("File data.txt berhasil dibuat)")
