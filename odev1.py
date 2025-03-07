file1 = open("odev.txt", "w")
file1.write(input("Bir metin giriniz: "))
file1.close()

file2 = open("odev.txt", "r")
print(file2.read())
file2.close()

file3 = open("odev2.txt", "w")
for i in range(5):
    file3.write(input("Bir metin giriniz: ") + "\n")
file3.close()


# Ödev: Dosya Okuma ve Yazma (Araştırma ve Uygulama)
# Konu: Dosya işlemleri (read, write, append).
# Görev:
# •	Kullanıcının girdiği metni bir .txt dosyasına yazan bir Python programı yazın.
# •	Daha sonra yazılan bu dosyayı okuyarak içeriğini ekrana yazdırın.
# •	Kullanıcıdan alınan 5 farklı satır verisini bir dosyaya kaydedin ve ardından bu dosyadaki verileri satır satır okuyarak ekrana yazdırın.
