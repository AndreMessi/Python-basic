
for i in range(1,10):
   
    if i is 6:
        print('angka i temukan',6) 
        continue

    print('nilai saat ini adalah',i)

else:
    print('akhir dari loop')
print('print  di luar loop')


#menggunakan pass

for i in range(1,10):
   
    if i is 6:
        print('angka i temukan',6) 
        #continue
        pass
        print('cek kondisi')

    print('nilai saat ini adalah',i)

else:
    print('akhir dari loop')
print('print  di luar loop')