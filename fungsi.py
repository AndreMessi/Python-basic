def suaraayam():
    print("kurkurkur")

def hargayam():
    suaraayam()
    print("harga ayam adalah Rp 45 per kg")
hargayam()


#fungsi dengan argumen
def hargatotalayam(kg):
    suaraayam()
    harga=50
    hargatotal= kg*harga
    print('harga',kg,'ayam adalah Rp:',hargatotal)
hargayam()
hargatotalayam(2)
hargatotalayam(0.9)
hargatotalayam(3.5)