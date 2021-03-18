
# Data diri
dict = {'Nama':'Yukuri Hanjani Putri',
        'Hobi1':'Menggambar','Hobi2':'Berenang','Hobi3':'Mendengar musik',
        'Sos_med1':'ig:@yukuri_hanjani','Sos_med2':'Line:yukurihanjani3','Sos_med3':'twitter:@hahahaha',
        'Lagu1':'Rehat','Lagu2':'Heartbreak Anniversary','Lagu3':'Monokrom','Lagu4': 'Happy' ,
        'Makanan1':'Tempe','Makanan2':'Magelangan','Makanan3':'Indomie'}

# Mengubah satu hobi
dict['Hobi2'] = 'Menonton film'

# Mengubah satu sosial media
dict['Sos_med1'] = 'tiktok : @haihaihai'

# Menghapus dua makanan
del dict['Makanan2']
del dict['Makanan3']

# Menambah satu Hobi
dict['Hobi4'] = 'Memasak'

# Menampilkan dictionary
print(dict)