# Pertemuan 3: Tipe Data List dalam Python

# Membuat list kosong
my_list = []

# Menambahkan elemen ke list
my_list.append(10)
my_list.append("Halo")
my_list.append(3.14)
my_list.append([1, 2, 3])  # List dalam list

# Mengakses elemen-elemen dalam list
print("List lengkap:", my_list)
print("Elemen ke-0:", my_list[0])
print("Elemen ke-1:", my_list[1])
print("Elemen ke-3:", my_list[3])

# Mengubah elemen dalam list
my_list[0] = 20
print("Setelah diubah:", my_list)

# Menghapus elemen dari list
my_list.remove("Halo")
print("Setelah dihapus:", my_list)

# Melakukan iterasi melalui list
print("Menggunakan loop for:")
for item in my_list:
    print(item)
