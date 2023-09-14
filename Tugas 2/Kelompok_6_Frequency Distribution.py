def banyak_data_interval(arr, batas_bawah, batas_atas):
    #menambahkan elemen list ke data_interval jika batas_bawah< data <batas_atas, 
    #kemudian mengembalikan banyak data dengan banyak bintang
    data_interval = [data for data in arr if (data > batas_bawah) and (data <= batas_atas)]
    return '* ' * len(data_interval) 

def tampilkan_subinterval(batas_bawah, batas_atas, banyak_data):
    #untuk menampilkan banyak data tiap subinterval
    #sengaja dibuat if-else agar :-nya rapi
    if batas_bawah >= 0 and batas_bawah < 10:
        print(f' {batas_bawah} - {batas_atas}   : {banyak_data}')
    elif batas_atas == 100:
        print(f'{batas_bawah} - {batas_atas}  : {banyak_data}') 
    elif batas_atas > 100:
        print(f'{batas_bawah} - {batas_atas} : {banyak_data}')  
    else:  
        print(f'{batas_bawah} - {batas_atas}   : {banyak_data}')

def tampilkan_data(data, akhir , jarak) :
    #membuat subinterval dengan menentukan akhir batas dan jarak subintervalnya
    tampilkan_subinterval(0, jarak, banyak_data_interval(data, -1, 10))
    for lompatan in range(jarak, akhir, jarak):
        tampilkan_subinterval(lompatan+1, lompatan + jarak, banyak_data_interval(data, lompatan, lompatan + 10))


#test code untuk angka acak
if __name__ == '__main__':
    from random import randint

    def masukkan(input, default):
        masukkan = input
        if masukkan == '': #mengembalikan nilai default jika user menekan enter
            return default
        return int(masukkan)

    print(f'=========== frequency distribution ==========='.upper())
    input_batas_akhir = masukkan(input(f'silakan masukkan batas akhirnya [default 100]: '), 100)
    input_jarak_subinterval = masukkan(input(f'silakan masukkan jarak subintervalnya [default 10]: '), 10)
    random_number = masukkan(input(f'masukkan range bilangan acak yg di-generate [default 100]: '), 100)   

    list_data=[randint(0,random_number) for _ in range(random_number)] #list angka acak dari 0-n (inklusif)
    tampilkan_data(list_data, input_batas_akhir, input_jarak_subinterval)
    

