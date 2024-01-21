"""
Bu oyunda, tercümanımızın içinden rastgele 1 kelime seçeceği bir kelime listesi bulunmaktadır. 
Kullanıcının önce adını girmesi gerekiyor, ardından herhangi bir alfabeyi tahmin etmesi isteniyor. 
Rastgele kelime bu alfabeyi içeriyorsa, çıktı olarak gösterilecektir (doğru yerleşimle birlikte), aksi takdirde 
program sizden başka bir alfabeyi tahmin etmenizi isteyecektir. 
Kullanıcıya kelimenin tamamını tahmin etmesi için 12 tur (buna göre değiştirilebilir) verilecektir.
"""

import random
# random kütüphanesi, rastgele kelime seçmek için kullanılır.

name = input("İsminizi giriniz: ")
print("İyi Şanslar", name)

#Kelimenin seçileceği bir liste.
kelimeler = ['gökkuşağı', 'bilgisayar', 'bilim', 'programlama',
         'python', 'matematik', 'oyuncu', 'koşul',
         'ters', 'su', 'tahta', 'inek']

#Rastgele bir kelimenin seçilmesi:
# choice() fonksiyonu, bir liste, tuple veya string ifadeden rasgele bir öğe döndürülür.
kelime = random.choice(kelimeler)

print("Karekterli tahmin et: ")

tahminler = ''
tahminhakki = 12

while tahminhakki > 0:
    arıza = 0

    for char in kelime:
        if char in tahminler:
            print(char, end=" ")
        else:
            print("_")
            arıza += 1

    if arıza == 0:
        print("Sen kazandın")

        print("Kelimeler: ", kelime)
        break

    print()
    tahmin = input("Bir karekter tahmin et: ")

    tahminler += tahmin

    if tahmin not in kelime:

        tahminhakki -= 1
        print("Yanlış")
        print("Daha fazla tahmin", + tahminhakki, "var")

        if tahminhakki == 0:
            print("Kaybettin")