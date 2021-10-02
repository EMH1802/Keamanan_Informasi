print("===================")
print("Ezra Muhammad Hilal")
print("    20190801389    ")
print("===================")

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def enkripsi(abjad):
    str = input("Teks : ")
    key = int(input("Key : "))

    str = str.lower()
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n - key) % 26
            convert = abjad[encrypt]
            result = result + convert
        else:
            result = result + ''

    print(f"Result : {result}")


def dekripsi(abjad):
    str = input("Teks : ")
    key = int(input("Key : "))

    str = str.lower()
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            decrypt = (n + key) % 26
            convert = abjad[decrypt]
            result = result + convert
        else:
            result = result + ''

    print(f"Result : {result}")


pilihan = 'y'

while (pilihan == 'y'):
    print("Menu Pilihan : ")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    menu = input("Menu Yang Di Pilih : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(abjad)
    elif menu == '3':
        print("Keluar Dari Program")
        break
    else:
        print("Menu Tidak Ditemukan")

    print("----------------------------------------")
    pilihan = input("Apakah Ingin Melanjutkan ? (y/n) ")
    print("----------------------------------------")
