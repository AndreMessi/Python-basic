angka=0

while angka < 5:
    print ('nilai angka ini adalah',angka)
    angka=angka+1

    print('di luar while')

    start=True
    angka=0

    while start :
        print("didalam while")
        if angka is 100:
            start=False
            print('ok angka 100 ditemukan')
        angka +=1