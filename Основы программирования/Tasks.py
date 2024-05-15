# Task1 Степень двойки
def func1(a):
    if (a >= 0) and (a <= 100):
        print(2 ** a)
    else:
        print("ОШИБКА!!!")
func1(int(input('a = ')))

# Task2 Последняя цифра
def func2(a):
    if (a > 0) and (a <= 10000):
        print(a % 10)
    else:
        print("ОШИБКА!!!")
func2(int(input('a = ')))

# Task3 Первая цифра двузначного числа
def func3(a):
    if (a > 9) and (a < 100):
        print(a // 10)
    else:
        print("ОШИБКА!!!")
func3(int(input('a = ')))

# Task4 100 раз подряд
def func4(a):
    print(a * 100)
func4('A')

# Task5 Вторая справа цифра
def func5(a):
    if a >= 10:
        b = a // 10
        print(b % 10)
    elif (a < 10) and (a > 0):
        print(0)
    else:
        print("ОШИБКА!!!")


func5(int(input('a = ')))

# Task6 Сумма цифр трехзначного числа
def func6(a):
    if (a > 99) and (a < 1000):
        b = a % 10
        c = a // 10
        c = c % 10
        d = a // 100
        d = d % 10
        print(b + c + d)
    else:
        print("ОШИБКА!!!")


func6(int(input('a = ')))

# Task7 Электронные часы-1
def func7(N):
    if (N <= (10 ** 7)) and (N >= 0):
        H = N // 60
        M = N - (H * 60)
        print(H, M)
    else:
        print('Ошибка!!!')
func7(int(input('N = ')))

# Task8 Следующее и предыдущее
def func8(N):
    if (N >= -1000) and (N <= 1000):
        print('The next number for the number', N, 'is', N + 1)
        print('The previous number for the number', N, 'is', N - 1)
    else:
        print('Ошибка!!!')
func8(int(input('N = ')))

# Task9 0 в 1 и наоборот
def func9(N):
    if N in (0, 1):
        a = not N
        a = int(a)
        print(a)
    else:
        print('Ошибка!!!')
func9(int(input('N = ')))

# Task10 Следующее четное
def func10(N):
    if (N >= 0) and (N <= 1000):
        if N % 2 == 0:
            N += 2
        else:
            N += 1
        print(N)
    else:
        print('Ошибка!!!')
func10(int(input('N = ')))

# Task11 100 раз подряд в квадрате
def func11(N):
    if (N >= 0) and (N <= 1000):
        N = str(N)
        N = N * 100
        N = int(N)
        N = N ** 2
        print(N)
    else:
        print('sm;kv')
func11(int(input('N = ')))

# Task12 МКАД
def func12(v, t):
    count = 0
    if (v > -1000) and (v < 1000) and (t > -1000) and (t < 1000):
        S = v * t
        count = S // 109
        count = count * 109
        print(S - count)
    else:
        print('sascjno')
func12(int(input('v = ')), int(input('t = ')))

# Tack13 Электронные часы-2 (Недоработана)
def func13(N):
    if N >= 0:
        M = (N // 60) % 60
        H = (N // 60) // 60
        S = N % 60
        print(H, ':', M, ':', S)
        if S > 10:
            S = str(S)
            S = '0' + S
            print(H, ':', M, ':', S)
        elif M > 60:
            M = str(M)
            M = '0' + M
            print(H, ':', M, ':', S)
        else:
            print(H, ':', M, ':', S)
    else:
        print('Ошибка!!!')
func13(int(input('N = ')))

# Task14 Разность времен
def func14(H1, M1, S1, H2, M2, S2):
    N1 = (H1 * 3600) + (M1 * 60) + S1
    N2 = (H2 * 3600) + (M2 * 60) + S2
    S = N2 - N1
    print(S)
func14(int(input('H1 = ')), int(input('M1 = ')), int(input('S1 = ')), int(input('H2 = ')), int(input('M2 = ')), int(input('S2 = ')))

#Task15 Автопробег
def func15(N, M):
    if (N >= 0) and (M >= 0):
        b = M % N
        if b == 0:
            print(M // N)
        else:
            print((M // N) + 1)
    else:
        print('Ошибка!!!')
func15(int(input('N = ')), int(input('M = ')))

#Task16 Симметричное число (Не работает)
def func16(N):
    if (N % 100) == (N // 100):
        print('1')
    else:
        print('0')
func16(int(input('N = ')))

#Task17 Максимум из двух
def func17(N, M):
    if (N > 0) and (N <= 1000) and (M > 0) and (M <= 1000):
        if N > M:
            print(N)
        else:
            print(M)
    else:
        print('Ошибка!!!')
func17(int(input('N = ')), int(input('M = ')))

#Task18 Проверка на делимость
def func18(A, B):
    if (A % B) == 0:
        print('YES')
    else:
        print('NO')
func18(int(input('A = ')), int(input('B = ')))

#Task19 Какое число больше?
def func19(A, B):
    if A > B:
        print('1')
    elif A < B:
        print('2')
    else:
        print('0')
func19(int(input('A = ')), int(input('B = ')))

#Task20 Максимум трех чисел
def func20(A, B, C):
    if (A > B) and (A > C):
        print(A)
    elif (B > A) and (B > C):
        print(B)
    else:
        print(C)
func20(int(input('A = ')), int(input('B = ')), int(input('C = ')))

#Task21 Високосный год
def func21(N):
    if ((N % 4) == 0) and not((N % 100) == 0):
        print('YES')
    else:
        print('NO')
func21(int(input('N = ')))

#Task22 Ход короля
def func22(A, B, C, D):
    if A == C - 1 and B == D - 1:
        print('YES')
    else:
        print('NO')
func22(int(input('A = ')), int(input('B = ')), int(input('C = ')), int(input('D = ')))

#Task23 Квартиры
def func23(x, y):
    if y % (y - x + 1) == 0:
        print('YES')
    else:
        print('NO')
func23(int(input('x = ')), int(input('y = ')))

#Task24 Цвет клеток шахматной доски
def func24(A, B, C, D):
    if not((A + B + C + D) % 2):
        print('YES')
    else:
        print('NO')
func24(int(input('A = ')), int(input('B = ')), int(input('C = ')), int(input('D = ')))

#Task25 Шоколадка
def func25(n, m, k):
    if (k < m * n) and (not(k % m) or not(k % n)):
        print('YES')
    else:
        print('NO')
func25(int(input('n = ')), int(input('m = ')), int(input('k = ')))

#Task26 Коровы
def func26(N):
    if 11 <= N <= 14:
        print(N, 'korov')
    else:
        M = N % 10
        if M == 0 or (5 <= M <= 9):
            print(N, 'korov')
        elif M == 1:
            print(N, 'korova')
        else:
            print(N, 'korovy')
func26(int(input('N = ')))

#Task27 Координатные четверти
def func27(x1, x2, y1, y2):
    if x1 * x2 and y1 * y2:
        print('YES')
    else:
        print('NO')
func27(int(input('x1 = ')), int(input('x2 = ')), int(input('y1 = ')), int(input('y2 = ')))

#Task28 Тип треугольника
def func28(a, b, c):
    C = max(a, b, c)
    B = min(a, b, c)
    A = (a + b + c) - B - C
    if C >= A + B:
        print('impossible')
    elif (C ** 2) == (A ** 2) + (B ** 2):
        print('rectangular')
    elif (C ** 2) < (A ** 2) + (B ** 2):
        print('acute')
    else:
        print('obtuse')
func28(int(input('a = ')), int(input('b = ')), int(input('c = ')))

#Task29 Четные и нечетные
def func29(A, B, C):
    if ((A + B) % 2) or ((B + C) % 2 or ((A + C) % 2)):
        print('YES')
    else:
        print('NO')
func29(int(input('A = ')), int(input('B = ')), int(input('C = ')))

#Task30 Сколько чисел совпадает?
def func30(A, B, C):
    if A == B == C:
        print('3')
    elif (A == B) or (B == C) or (A == C):
        print('2')
    else:
        print('0')
func30(int(input('A = ')), int(input('B = ')), int(input('C = ')))

#Task31 Мороженое
def func31(k):
    if k in (3, 4, 5) or (k > 7):
        print('YES')
    else:
        print('NO')
func31(int(input('k = ')))