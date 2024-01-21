import random
from collections import Counter

someWords = '''elma muz mango çilek
turuncu üzüm ananas kayısı limon hindistan cevizi karpuz
kiraz papaya dut şeftali liçi kavun'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print("Kelimeyi tahmin et! İPUCU: kelime bir meyvenin adıdır")

    for i in word:
        print('_', end=' ')
    print()

    playing = True

    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Tahmin edilecek harfi girin: '))
            except:
                print("Yalnızca bir harf girin! : ")
                continue

            if not guess.isalpha():
                print("Yalnızca bir MEKTUP girin: ")
                continue
            elif len(guess) > 1:
                print('Yalnızca TEK bir harf girin: ')
                continue
            elif guess in letterGuessed:
                print('Bu mektubu zaten tahmin ettiniz: ')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1

                elif Counter(letterGuessed) == Counter(word):
                    print('The word is:', end=' ')
                    print(word)
                    flag = 1
                    print('Tebrikler kazandın!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()