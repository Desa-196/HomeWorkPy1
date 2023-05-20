#Задача 2: Найдите сумму цифр трехзначного числа.

readInt = 0

while(True):
    try:
        readInt = int(input("Введите трехзначное число:"))
        if 1000 > readInt > 99:
            break
        else:
            print('Число должно быть трехзначным!')
            
    except:
        print('Введено не число!')
