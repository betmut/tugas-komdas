import math as mtk

def function_1(x):
    """ Mengembalikan f(x) = x """
    return x

def function_2(x):
    """ Mengembalikan f(x) = (x-2)^2 """
    return (x-2)**2

def function_3(x):
    """ Mengembalikan f(x) = 0 """
    return 0

def sin10(x):
    """ Mengembalikan f(x) = 10.sin(x) """
    return 10 * mtk.sin(x)
    
def exp(x):
    """ Mengembalikan f(x) = e^x """
    return mtk.exp(x)

def define_interval(f,xmin,xmax):
    """
    Mencetak interval [xmin, xmax] dan nilai fungsi pada titik tersebut.

    Argumen:
        f : Fungsi untuk mengevaluasi.
        xmin: Batas bawah interval.
        xmax: Batas atas interval.
    """

    print(f'[xmin, xmax] = [{xmin}, {xmax}]')
    ymin = f(xmin)
    ymax = f(xmax)
    print(f'[ymin, ymax] = [{ymin:.2f}, {ymax:.2f}]')

def sumbu_y():
    """Mencetak representasi visual sumbu y."""
    print('y-'+ ' ' + 120 * '-' + 2 *' ' + 'y+')
 
def plot_function(f, xmin, xmax, scale_x = 0.3, scale_y = 0.5, define_y_negative = 10):
    """
    Plot fungsi f(x) untuk x dalam [xmin, xmax].

    Argumen:
    f : Fungsi untuk membuat plot.
        xmin: Batas bawah plot.
        xmax: Batas atas plot.
        scale_x: Faktor penskalaan untuk nilai x (defaultnya adalah 0,3).
        scale_y: Faktor penskalaan untuk nilai y (defaultnya adalah 0,5).
        define_y_negative: Jumlah karakter sumbu y negatif (defaultnya adalah 10).
    """

    define_interval(f, xmin, xmax)    
    sumbu_y()
    for x in range(xmin,xmax):
        nilai_fungsi =  f(x * scale_x)
        loncatan = int(nilai_fungsi / scale_y)
        spasi = (loncatan + define_y_negative) * ' '

        x_axis = define_y_negative * ' '
        print(x_axis + '|')

        print( spasi + '*')
    print( 'x+')
    print(120 * '-')

def area_between_curve(f1, f2, xmin, xmax, scale_x = 0.3, scale_y = 0.5, define_y_negative = 10):
    """
    Plot luas antara dua kurva, f1(x) dan f2(x), untuk x dalam [xmin, xmax].

    Argumen:
        f1: Fungsi pertama.
        f2: Fungsi kedua.
        xmin: Batas bawah plot.
        xmax: Batas atas plot.
        scale_x: Faktor penskalaan untuk nilai x (defaultnya adalah 0,3).
        scale_y: Faktor penskalaan untuk nilai y (defaultnya adalah 0,5).
        define_y_negative: Jumlah karakter sumbu y negatif (defaultnya adalah 10).
    """    
    define_interval(f2, xmin, xmax)
    sumbu_y()    
    for x in range(xmin,xmax):
        nilai_fungsi_1 =  f1(x * scale_x)
        nilai_fungsi_2 =  f2(x * scale_x)

        loncatan_1 = int(nilai_fungsi_1 / scale_y)
        loncatan_2 = int(nilai_fungsi_2 / scale_y)

        spasi_1 = (loncatan_1 + define_y_negative) * ' '
        spasi_2 = (loncatan_2 + define_y_negative) * ' '

        area = abs(loncatan_2 - loncatan_1)

        x_axis = define_y_negative * ' '
        print(x_axis + '|')   

        print(spasi_1 + (area * '*') + spasi_2)

    print( 'x+')
    print(120 * '-')


#contoh program memploting fungsi
print(40 * ' '+'============ PLOT FUNCTIONS ============')
pi = int(mtk.pi)
flist=[function_1, function_2,function_3 , sin10, exp]
xmin =[ -10,  -10, -10, -5*pi, -9]
xmax =[ 11,  25, 10, 5*pi, 14]

for index in range(len(flist)):
    plot_function(flist[index], xmin[index], xmax[index], scale_x=0.3 , scale_y= 0.5, define_y_negative= 30)


print(40 * ' '+'============ PLOT AREA BETWEEN FUNCTIONS ============')
function_list = [function_2, function_3, sin10, exp]
for index in range(len(function_list)):
    area_between_curve(function_1, function_list[index], xmin[index], xmax[index], scale_x=0.2 , scale_y= 0.5, define_y_negative= 30)




