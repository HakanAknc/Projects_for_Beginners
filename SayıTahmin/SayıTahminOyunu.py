"""
Görev: Aşağıda adımlar verilmiştir:
Kullanıcının bir aralık seçtiği bir Sayı tahmin oyunu oluşturun .
Diyelim ki Kullanıcı A ile B arasında , A ve B'nin Tamsayıya ait olduğu bir aralık seçti.
Sistem tarafından rastgele bir tamsayı seçilecek ve kullanıcının bu tamsayıyı minimum tahmin sayısıyla tahmin etmesi gerekecek.
"""
# minimum tahmin sayısı aralığı
# Minimum tahmin sayısı = log 2 (Üst sınır – alt sınır + 1)

import random
import math

#Alt ve üst sınırların kullanıcıdan alınması
lower = int(input("Alt değeri giriniz: "))
upper = int(input("Üst değeri giriniz: "))

#Rastgele bir sayının seçilmesi
x = random.randint(lower, upper)

#Tahmin hakkı sayısının belirlenmesi
#Kullanıcıya kaç tahmin hakkı olduğunu söyleyen bir mesaj.
#Tahmin hakkı, math.log fonksiyonu ile hesaplanır.
print("\n\tSon ",
      round(math.log(upper - lower + 1, 2)), # # round() kayan noktalı sayıları en yakın tam sayıya doğru yuvarlıyor.
      "tamsayıyı tahmin etme şansın kaldı!\n")

# Tahminlerin sayısı başlatılıyor.
count = 0

# minimum sayının hesaplanması için
# tahmin aralığa bağlıdır
while count < math.log(upper - lower +1, 2):
    count += 1

    # Tahmin hakkı kullanıcıya bildirilir ve kullanıcıdan bir tahmin istenir.
    guess = int(input("Bir sayı tahmin et: "))

    #Durum Kontrolu
    #Kullanıcının tahmininin doğruluğu kontrol edilir ve duruma göre geri bildirim sağlanır
    if x == guess:
        print("Tebrikler doğru sayıyı tahmin ettiniz \n",
              count, ". Denemede buldunuz.")
        break # program bitti
    elif x > guess:
        print("Çok küçük tahmin etmişsin!")
    elif x < guess:
        print("Çok yüksek tahmin ettin")

# Tahmin hakkının bitip bitmediğinin kontrolü ve sonuçların gösterilmesi:
if count >= math.log(upper - lower +1, 2):
    print("\nSayı %d" % x)
    print("\tBir dahaki sefere daha iyi şanslar")