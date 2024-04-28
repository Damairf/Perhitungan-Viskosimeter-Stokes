# Mencari jari-jari bola
print('Mencari jari-jari bola (r)')
print('1. 0.005764\n2. 0.008006\n3. Hitung jari dari diameter')
jari1 = 0.005764
jari2 = 0.008006

while True :
    pilihJari = int(input('Pilih kode jari-jari: '))
    if pilihJari == 1:
        jari = jari1
        print('Kamu memilih jari-jari', jari1)
        print()
        break
    elif pilihJari == 2:
        jari = jari2
        print('Kamu memilih jari-jari', jari2)
        print()
        break
    elif pilihJari == 3:
        print()
        print('Mencari jari-jari dari bola')
        diameter = float(input('Masukkan diameter: '))
        jari = diameter / 2
        print('jari-jari dari diameter', diameter, 'adalah', jari)
        print()
        break
    else:
        print()
        print('Kode tidak valid. Masukkan kode jari-jari')

# Mencari massa jenis bola
print('Mencari massa jenis bola (P)')
print('1. 0.002\n2. 0.0055\n3. Masukkan massa sendiri')
massa1 = 0.002
massa2 = 0.0055
while True:
    pilihMassa = int(input('Pilih kode massa bola: '))
    if pilihMassa == 1:
        massa = massa1
        print('Kamu memilih massa bola 0.002')
        print()
        break
    elif pilihMassa == 2:
        massa = massa2
        print('Kamu memilih massa bola 0.0055')
        print()
        break
    elif pilihMassa == 3:
        massa3 = float(input('Masukkan massa bola: '))
        massa = massa3
        print('Massa bolah adalah', massa)
        print()
        break
    else:
        print()
        print('Kode tidak valid. Masukkan kode massa bola')
kecepatan = 4/3 * 3.14 * jari**3
P = massa / kecepatan
print('Massa jenis kelereng adalah', P)
print()

# Mencari kekentalan zat cair (KZC)
print('Mencari kekentalan zat cair (Pas)')
kedalaman = float(input('Masukkan kedalam(s): '))
waktu = float(input('Masukkan waktu(t): '))
koefisienKZC = (2 * waktu * jari**2) * (9.8 * (P - 1000)) / (9 * kedalaman)
print('Hasil akhir adalah', koefisienKZC)