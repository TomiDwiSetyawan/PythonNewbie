# print('Hello world')
# print(1+3)

# "Belajar Python"  #single lane

# print("Luas = ", 3*3, " cm")
# print("Luas = %2d " % (5*3), " cm")


# # nilai_sisi = int(input("Masukkan Nilai Sisi : "))
# # print("Luas = " , nilai_sisi**2)

# # nilai1 = int(input("Masukkan Nilai1 : "))
# # nilai2 = int(input("Masukkan Nilai2 : "))
# # nilai3 = int(input("Masukkan Nilai3 : "))
# # print("Total Luas = ", ((nilai1**2)+(nilai2**2)+(nilai3**2)))


# passs = input("Massukan Password : ")
# if(passs=="123"):
#     print("correct")


# L1 = ['surabaya', 'semarang', 'klateng']
# print("Kota Awal : " , L1)
# print("Menghapus semarang dari daftar : " , L1.remove('semarang'), L1)
# print("Menambah banyuwangi dari daftar : " , L1.append('semarang'), L1)

data=("satu", "dua", "tiga", "empat", "lima")
print(data)
i=0
hitungA=0
for x in data:
    for y in data[i]:
        if y=="a":
            hitungA = hitungA+1
    i=i+1

print("jumlah huruf 'a' ada : " , hitungA)