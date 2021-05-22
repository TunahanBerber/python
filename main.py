import random

number = random.randint(1, 100)
due = 5
counter = 0
while due > 0:
    due-=1
    counter+=1
    prediction = int(input("Tahmin Giriniz :"))
    if number==prediction:
        print(f'Tebrikler Tahmininiz Doğru,{counter}. denemede bildiniz. Toplam puanınız {100 -(20 * (counter - 1))}')
        break
    elif number > prediction:
        print("Yanlış tahmin ettiniz. Daha yüksek bir sayı deneyin.")
    else:
        print("Yanlış tahmin ettiniz. Daha düşük bir sayı deneyin.")
    if due == 0:
        print(f'Hakkınız bitti. Tutulan sayı : {number}')
