#Задача 2: Найдите сумму цифр трехзначного числа.

readInt = 0

while(True):
    try:
        readInt = int(input("Введите трехзначное число:"))
    except:
        print('Введено не число!')
        continue

    if 1000 > readInt > 99:
        break
    else:
        print('Число должно быть трехзначным!')
            

print(readInt)
