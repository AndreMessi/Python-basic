print("======================")
nilai=70

if 80 <= nilai <= 100:
    print("nilai anda A")
elif 70 <= nilai < 80:
    print("nilai anda B")
elif 60 <= nilai < 70:
    print("nilai anda C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T lakukan perbaikan")
else:
    print("nlai anda tidak lulus mata kuliah ini")

#operator untuk ifelse  
gorengan=["bakwan","tahu","ubi","pisang","molen","perkedel"]
beli="tahu"

if beli in gorengan:
    print("saya bilang ,ya saya jual",beli)
if not beli in gorengan:
    print("saya tidak jual",beli)