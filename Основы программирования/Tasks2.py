#Task1 Дробная часть
def func1(X):
    index = X.find('.')
    stroka = X[index:]
    print('0' + stroka)
func1(input('X = '))

#Task2 Цена товара
def func2(cost):
    cost = cost.split(".")
    print(*cost)
func2(input('Введите цену товара: '))

#Task3 Округление по российским правилам
def func3(x):
    if (x%1) >= 0.5:
        x += 1
        x //= 1
        print(int(x))
    else:
        x //= 1
        print(int(x))
        return
func3(float(input('x = ')))

#Task4 Проценты
def func4(P, X, Y):
    allmoney = X + Y
    percent = (allmoney * P) / 100
    newmoney = str(allmoney + percent)
    newmoney = newmoney.split(".")
    print(*newmoney)
func4(float(input('P = ')), float(input('X = ')), float(input('Y = ')))

#Task5 Сложные проценты (не рабочая)
def func5(P, X, Y, K):
    count = 0
    aldmoney = X + Y
    while count != K:
        percent = (aldmoney * P) / 100
        count += 1
        newmoney = aldmoney + percent
        aldmoney = newmoney
    allmoney = str(aldmoney)
    allmoney = allmoney.split(".")
    print(*allmoney)
func5(float(input('P = ')), float(input('X = ')), float(input('Y = ')), float(input('K = ')))

#Task6 Делаем срезы
def func6(stroka):
    print(stroka[2])
    print(stroka[-1])
    print(stroka[0:5])
    print(stroka[:-2])
    print(stroka[::2])
    print(stroka[1::2])
    print(stroka[::-1])
    print(stroka[::-2])
    print(len(stroka))
func6(input())

#Task7 Первое и последнее вхождение
def func7(stroka):
    Vhod_1 = stroka.find("f")
    Vhod_2 = stroka.rfind("f")
    if Vhod_1 == -1:
        print()
    elif Vhod_1 == Vhod_2:
        print(Vhod_1)
    else:
        print(Vhod_1, Vhod_2)
func7(input())

#Task8 Удаление фрагмента
def func8(stroka):
    index1 = stroka.find("h")
    index2 = stroka.rfind("h")
    newstroka1 = stroka[:index1]
    newstroka2 = stroka[index2 + 1:]
    allstroka = newstroka1 + newstroka2
    print(allstroka)
func8(input())

#Task9 Дублирование фрагмента
def func9(stroka):
    index1 = stroka.find("h")
    index2 = stroka.rfind("h")
    neckline1 = stroka[:index1 + 1]
    neckline2 = stroka[index1 + 1:index2]
    neckline3 = stroka[index2:]
    double_neckline2 = neckline2 * 2
    print(neckline1 + double_neckline2 + neckline3)
func9(input())

#Task10 Второе вхождение
def func10(stroka):
    index1 = stroka.find("f")
    index2 = stroka.rfind("f")
    if index1 < index2:
        print(index2)
    elif index2 == (-1):
        print(-2)
    elif index1 == index2:
        print(-1)
func10(input())

#Task11 Переставить два слова
def func11(stroka):
    index = stroka.find(" ")
    word1 = stroka[:index]
    word2 = stroka[index + 1:]
    print(word2, word1)
func11(input())

#Task 12 Количество слов
def func12(stroka):
    print(stroka.count(" ") + 1)
func12(input())

#Task13 Замена подстроки
def func13(stroka):
    print(stroka.replace("1", "one"))
func13(input())

#Task14 Удаление символа
def func14(stroka):
    print(stroka.replace("@", ""))
func14(input())

#Task15 Замена внутри фрагмента
def func15(stroka):
    index1 = stroka.find("h")
    index2 = stroka.rfind("h")
    neckline1 = stroka[:index1 + 1]
    neckline2 = stroka[index1 + 1:index2].replace("h", "H")
    neckline3 = stroka[index2:]
    print(neckline1 + neckline2 + neckline3)
func15(input())

#Task16 Вставка символов
def func16(stroka):
    number = 0
    border1 = 0
    border2 = 1
    newstroka = ''
    while number < len(stroka):
        number += 1
        newstroka += stroka[border1:border2]+'*'
        border1 += 1
        border2 += 1
    print(newstroka[:-1])
func16(input())

#Task17 Удалить каждый третий символ
def func17(stroka):
    newstroka = ''
    long = len(stroka)
    for i in range(long):
        if i % 3 != 0:
            newstroka = newstroka + stroka[i]
    print(newstroka)
func17(input())

# Task18 Алфавит
def func18(stroka):
    for i in stroka:
        if (ord(i) > 1) and (ord(i) < 10):
            continue
        else:
            print(ord(i))


func18(input())

# Task19 Пара символов
def func19(stroka):
    number = 0
    border1 = 0
    border2 = 2
    newstroka = ''
    while number < len(stroka):
        number += 1
        newstroka += stroka[border1:border2]+' '
        border1 += 2
        border2 += 2
    if len(stroka)%2 == 0:
        print(newstroka[:-2])
    else:
        print(newstroka[:-2] + '_')


func19(input())

# Task20 Список друзей (уверен, что это можно решить другим способом, но я его еще не познал)
def func20(stroka):
    space_1 = stroka.find(' ')
    space_2 = stroka.rfind(' ')
    name_1 = stroka[:space_1]
    name_2 = stroka[space_1 + 1:space_2]
    name_3 = stroka[space_2 + 1:]
    if (len(name_1) == 4) and (len(name_2) == 4) and (len(name_3) == 4):
        print(name_1, name_2, name_3)
    elif (len(name_1) == 4) and (len(name_2) == 4):
        print(name_1, name_2)
    elif (len(name_2) == 4) and (len(name_3) == 4):
        print(name_2, name_3)
    elif (len(name_1) == 4) and (len(name_3) == 4):
        print(name_1, name_3)
    elif len(name_1) == 4:
        print(name_1)
    elif len(name_2) == 4:
        print(name_2)
    else:
        print(name_3)


func20(input())
