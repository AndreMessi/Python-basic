gorengan=["bakwan","tahu","ubi","pisang","molen","perkedel"]

for i in gorengan:
    print(i)
    print(len(i))
print("=================")
print("daftar belanjaan")
buah=["apel","jeruk","mangga","serikaya","nanas"]
sayur=["tomat","bayem","kangkung","wortel","pakis"]
daftar_belanja=[gorengan,buah,sayur]

for subdaftarbelanja in daftar_belanja:
    print(subdaftarbelanja)
    for komponen in subdaftarbelanja:
        print(komponen)



#menggunakan range pada for
for i in range(10,40,5):
    print(i) 

number=50

for i in range(0,40):
    print(i)
    if i is number:
        print('angka di temukan',i) 
        break
else:
    print('angka tidak di temukan')
print('angka di luar jangkauan')

#menggunakan range continue pada for

