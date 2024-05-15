import mylib
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate


print("\033[1;35mЗадача №1 \033[3;34m")

x = int(input("Введите M(x) >>> "))  # 3
y = int(input("Введите M(y) >>> "))  # 2

M_z = 8 * x - 5 * y + 7

print(f"\033[4;32mОтвет:\033[0m {M_z}")

print("\033[1;35mЗадача №2 \033[3;34m")

D_x = float(input("Введите D(x) >>> "))  # 1.5
D_y = int(input("Введите D(y) >>> "))  # 1

z = f"8 * {D_x} - 5 * {D_y} + 7"
z = z.split(" ")
D_8 = int(z[0]) ** 2
D_5 = int(z[4]) ** 2
D_7 = 0

D_z = D_8 * D_x - D_5 * D_y + D_7

print(f"\033[4;32mОтвет:\033[0m {D_z}")
'''
print("\033[1;35mЗадача №3 \033[3;34m")
a = float(input("Вероятность, что студент сдаст экзамен А >>> "))
b = float(input("Вероятность, что студент сдаст экзамен Б >>> "))
c = int(input("Сколько всего экзаменов >>> "))
nota = 1 - a
notb = 1 - b

X = []
for i in range(1, c + 1):
    X_i = i
    X.append(X_i)

P = [nota * notb, a * notb + nota * b, a * b]

df2 = pd.DataFrame({
    "Xi": X,
    "Pi": P
})

print(df2)
'''
print("\033[1;35mЗадача №4 \033[3;34m")
xi = input("Введите все xi >>> ")  # 2, 4, 6, 8
pi = input("Введите все pi >>> ")  # 0.4, 0.2, 0.1, 0.3
yj = input("Введите все yj >>> ")  # 0, 1, 2
pj = input("Введите все pj >>> ")  # 0.5, 0.2, 0.3


xi = xi.split(", ")
for i in range(len(xi)):
    xi[i] = int(xi[i])

pi = pi.split(", ")
for i in range(len(pi)):
    pi[i] = float(pi[i])

yj = yj.split(", ")
for i in range(len(yj)):
    yj[i] = int(yj[i])

pj = pj.split(", ")
for i in range(len(pj)):
    pj[i] = float(pj[i])

zij = []
for i in range(0, len(xi)):
    for j in range(0, len(yj)):
        z = 2 * xi[i] + 3 * yj[j]
        zij.append(z)

pij = []
for i in range(0, len(pi)):
    for j in range(0, len(pj)):
        p = pi[i] * pj[j]
        pij.append(p)

M_z = 0
M_z2 = 0
for i in range(len(zij)):
    M_z += (zij[i] * pij[i])
    M_z2 += ((zij[i] ** 2) * pij[i])

D_z = M_z2 - (M_z ** 2)

print(f"\033[4;32mОтвет:\033[0m\n    M(z) = {M_z}\n    D(z) = {D_z}")


print("\033[1;35mЗадача №5 \033[3;34m")
xi = input("Введите все xi >>> ")  # 3, 4, 5, 6, 7
pi = input("Введите все pi >>> ")  # 0.1, 0.2, 0.4, 0.1, 0.2


xi = xi.split(", ")
for i in range(len(xi)):
    xi[i] = int(xi[i])

pi = pi.split(", ")
for i in range(len(pi)):
    pi[i] = float(pi[i])

F_x = [0]
for i in range(len(pi)):
    F_x.append(round(F_x[i] + pi[i], 1))

X = [f"x <= {xi[0]}"]
for i in range(len(xi)):
    X.append(f"{xi[i - 1]} < x <= {xi[i]}")
X.pop(1)
X.append(f"{xi[len(xi) - 1]} < x")

df = pd.DataFrame({
    "F(x)": F_x,
    "X": X
})

P = 0
for i in range(len(xi)):
    if xi[i] > 5:
        P += pi[i]

M_x = 0
M_x2 = 0
for i in range(len(xi)):
    M_x += (xi[i] * pi[i])
    M_x2 += ((xi[i] ** 2) * pi[i])

D_x = M_x2 - (M_x ** 2)

print(f"\033[4;32mОтвет:\033[0m\n a)\n{df}\n\nб) P(x>5) = {round(P, 1)}\n\nв) M(x) = {round(M_x, 2)}\n   "
      f"D(x) = {round(D_x, 2)}")

print("\033[1;35mЗадача №6 \033[3;34m")
gran = input("Введите границы интегрирования >>> ")  # 0, 2
gran = gran.split(", ")
for i in range(len(gran)):
    gran[i] = int(gran[i])

ver = gran[0]
niz = gran[1]


def f1(x):
    return x * (x / 2)


def f2(x):
    return (x ** 2) * (x / 2)


M_x, err = integrate.quad(f1, ver, niz)

d, err2 = integrate.quad(f2, ver, niz)
D_x = d - (M_x ** 2)


print(f"\033[4;32mОтвет:\033[0m\n M(x) = {M_x}\n D(x) = {D_x}")

print("\033[1;35mЗадача №7 \033[3;34m")
dip = input("Введите диапазон x >>> ")  # 0 < x <= 6

if dip.find(" < x <= ") == 1:
    dip_del = dip.split(" < x <= ")
    for i in range(len(dip_del)):
        dip_del[i] = int(dip_del[i])

elif dip.find(" <= x < ") == 1:
    dip_del = dip.split(" <= x < ")
    for i in range(len(dip_del)):
        dip_del[i] = int(dip_del[i])

niz = dip_del[0]
ver = dip_del[1]

dip1 = f"x <= {niz}, x > {ver}"

f_x = 'x / 18'


df7 = pd.DataFrame({
    'Значение': [0, f_x],
    'Диапазон': [dip1, dip]
})


def f1(x):
    return x * (x / 18)


def f2(x):
    return (x ** 2) * (x / 18)


M_x, err = integrate.quad(f1, niz, ver)

d, err2 = integrate.quad(f2, niz, ver)
D_x = d - (M_x ** 2)


print(f"\033[4;32mОтвет:\033[0m\n a)\n{df7}\n\nб) M(x) = {round(M_x)}\n   "
      f"D(x) = {round(D_x)}")

diip = [-2, -1, 0]
znach_f = [0, 0, 0]
znach_F = [0, 0, 0]
for x in range(niz, ver + 1):
    diip.append(x)
    znach_f.append(x / 18)
    znach_F.append((x ** 2) / 36)

diip.append(7)
diip.append(8)
diip.append(9)
znach_F.append(0)
znach_F.append(0)
znach_F.append(0)
znach_f.append(0)
znach_f.append(0)
znach_f.append(0)

# plt.plot(diip, znach_F)
# plt.plot(diip, znach_f)

print("\033[1;35mЗадача №8 \033[3;34m")
dip = input("Введите диапазон x >>> ")  # 0 < x <= 2

if dip.find(" < x <= ") == 1:
    dip_del = dip.split(" < x <= ")
    for i in range(len(dip_del)):
        dip_del[i] = int(dip_del[i])

elif dip.find(" <= x < ") == 1:
    dip_del = dip.split(" <= x < ")
    for i in range(len(dip_del)):
        dip_del[i] = int(dip_del[i])

niz = dip_del[0]
ver = dip_del[1]

znach1 = int(input(f"Введите значение х при х <= {niz} >>> "))  # 0
znach2 = input(f"Введите значение х при {niz} < x <= {ver} >>> ")  # (x ** 2) / 4
znach2 = int(input(f"Введите значение х при х > {ver} >>> "))  # 1

dip1 = f"x <= {niz}, x > {ver}"


f_x = 'x / 2'


df8 = pd.DataFrame({
    'Значение': [0, f_x],
    'Диапазон': [dip1, dip]
})


def f1(x):
    return x * (x / 2)


def f2(x):
    return (x ** 2) * (x / 2)


M_x, err = integrate.quad(f1, niz, ver)

d, err2 = integrate.quad(f2, niz, ver)
D_x = d - (M_x ** 2)

for i in range(0, 1 + 1):
    Px = (i ** 2) / 4

F_1 = (1 ** 2) / 4
F_2 = (2 ** 2) / 4
P_x = F_2 - F_1

print(f"\033[4;32mОтвет:\033[0m\n a)\n{df8}\n\nв) P(x = 1) = {znach1}\n   P(x < 1) = {Px}\n   P(1 <= x < 2) = {P_x}\n\n"
      f"г) M(x) = {M_x}\n   D(x) = {D_x}")

diip = [-2, -1, 0]
znach_f = [0, 0, 0]
znach_F = [0, 0, 0]
for x in range(niz, ver + 1):
    diip.append(x)
    znach_f.append(x / 2)
    znach_F.append((x ** 2) / 4)

diip.append(3)
diip.append(4)
diip.append(5)
znach_F.append(1)
znach_F.append(1)
znach_F.append(1)
znach_f.append(1)
znach_f.append(1)
znach_f.append(1)

# plt.plot(diip, znach_F)
# plt.plot(diip, znach_f)

plt.show()
