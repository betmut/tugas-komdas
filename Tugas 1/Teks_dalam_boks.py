'''==Author==
    Nama    : Mohammad Mathew Elhans
    NIM     : G5401221009

    === Deskripsi Program ===
    Program ini bertugas untuk menyimpan 4 input string maksimal 20 kata kemudian 
    menampilkannya di layar dalam bentuk border 8 x 30.
'''


def pesan_eror(pesan):
    '''fungsi ini digunakan untuk menunjukkan pesan eror 
    jika terjadi kesalahan dalam penginputan.
    '''

    border_horizontal(30, '=')
    print(pesan)
    border_horizontal(30, '=')


def user_input(nomor):
    '''fungsi ini digunakan untuk menyuruh user untuk menginput string. Jika panjang string lebih dari 20 atau tidak 
    menginput apa-apa, menyuruh user untuk mengulang menginput lagi. Jika tidak terjadi kesalahan,
    Mengakhiri komputasi dan mengembalikan input.
    '''
    
    while True:
        huruf = input(f'masukkan teks {nomor}: ')
        if len(huruf) >=20:
            pesan_eror('ERROR: Maaf, karakter tidak boleh lebih dari 20')
        elif len(huruf) == 0:
            pesan_eror('ERROR: Anda tidak menginput apa-apa, silakan dicoba lagi')
        else:
            return huruf
        
def cetak_input(input):
    '''fungsi yang digunakan untuk menampilkan input beserta border kiri dan kanan
    '''
    spasi= ' '*(24-len(input)) 
    print(f'|    {input}'+ spasi + '|')

def border_horizontal(panjang, jenis_border):
    '''Fungsi yang digunakkan untuk membuat border horizontal dengan menentukan panjang bordernya dan jenis bordernya
    (misalkan *, -, dll)
    '''
    print(panjang * jenis_border)

def border_vertikal():
    '''Fungsi yang digunakan untuk membuat border vertikal kiri dan kanan
    '''
    print('|                            |')

def laporan(karakter):
    '''Fungsi yang digunakan untuk menampilkan berapa banyak kata pada input'''
    print(f'{karakter} memiliki {len(karakter)} karakter')


def program_utama():
    '''Fungsi dimana program berjalan'''
    
    #menyuruh untuk memasukkan input dan menyimpannya ke variabel
    input_1 = user_input('pertama')
    input_2 = user_input('kedua')
    input_3 = user_input('ketiga')
    input_4 = user_input('keempat')

    #membuat border horizontal sepanjang 30, dan border vertikal sebanyak 2 di atas
    border_horizontal(30, '-')
    for _ in range(2):
        border_vertikal()

    #menyuruh untuk mencetak input yang telah dimasukkan
    cetak_input(input_1)
    cetak_input(input_2)
    cetak_input(input_3)
    cetak_input(input_4)

    #membuat border horizontal sepanjang 30, dan border vertikal sebanyak 2 di bawah
    for _ in range(2):
        border_vertikal()
    border_horizontal(30, '-')

    #membuat laporan banyak kata dari input
    print('LAPORAN')
    border_horizontal(30, '-')
    laporan(input_1)
    laporan(input_2)
    laporan(input_3)
    laporan(input_4)
    border_horizontal(30, '-')

#memanggil fungsi program_utama() untuk menjalankan program
program_utama()


