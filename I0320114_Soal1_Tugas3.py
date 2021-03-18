# List 10 nama teman
Nama_teman = ['Zanet','Yola','Adhi','Vizal','Bonang','Maurich','Denny','Sekar','Zafira','Rara']

# Menampilkan nama teman indeks nomor 4,6, dan 7
print("Nama teman indeks nomor 4,6, dan 7 adalah",Nama_teman[4],",",Nama_teman[6],", dan",Nama_teman[7])

# Mengganti nama teman pada list 3,5, dan 9
Nama_teman[3] = 'Zedi'
Nama_teman[5] = 'Salma'
Nama_teman[9] = 'Rio'

# Menambahkan 2 nama teman
Nama_teman.append('Tsania')
Nama_teman.append('Rahmat')

# Menampilkan nama teman dengan pengulangan
urutan = 0
for data in range(0,12) :
    print(Nama_teman[urutan])
    urutan = urutan + 1

# Menampilkan panjang list nama teman
print(len(Nama_teman))