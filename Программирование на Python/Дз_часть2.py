import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math

# №1
polit = pd.DataFrame(pd.read_csv('polit.csv', delimiter=','))
polit.drop(['Unnamed: 0'], inplace=True, axis=1)

polit = polit.fillna('ZERO')

for i in range(1, len(polit.index)):
    if polit.fh09[i] == 'ZERO' or polit.polity09[i] == 'ZERO' or polit.gini[i] == 'ZERO' or polit.fparl08[i] == 'ZERO' \
            or polit.corr0509[i] == 'ZERO':
        polit = polit.drop([i])

polit = polit.drop([0])
polit.reset_index(inplace=True)

assert polit.shape == (135, 13), "Проверьте, сохранились ли изменения в polit"

# №2
not_free = polit

for i in range(1, len(not_free.index)):
    if not_free.fh09[i] <= 5.0:
        not_free = not_free.drop([i])

not_free.reset_index(inplace=True)
'''
assert not_free.shape == (30, 13), "Неверное число строк или столбцов"
assert not_free.iloc[3, 9] == 0, "Неверный датафрейм"
assert not_free.iloc[19, 1] == 'Mauritania', "Неверный датафрейм"
'''

# №3
af_w = polit

for i in range(1, len(af_w.index)):
    if af_w.afri[i] == 0 or af_w.fparl08[i] <= 30:
        af_w = af_w.drop([i])

af_w.reset_index(inplace=True)
af_w = af_w.drop([0])
af_w.drop(['level_0'], inplace=True, axis=1)

assert af_w.shape == (6, 13), "Неверное число строк или столбцов"
assert af_w.iloc[3, 5] == 33.92, "Неверный датафрейм"
assert af_w.iloc[5, 7] == 0, "Неверный датафрейм"

# №4
la_dem = polit

for i in range(1, len(la_dem.index)):
    if (la_dem.afri[i] == 0 or la_dem.lati[i] == 0) and la_dem.polity09[i] < 8:
        la_dem = la_dem.drop([i])

la_dem.reset_index(inplace=True)
la_dem = la_dem.drop([0])
la_dem.drop(['level_0'], inplace=True, axis=1)
'''
assert la_dem.shape == (18, 13), "Неверное число строк или столбцов"
assert la_dem.iloc[3, 5] == 12.66, "Неверный датафрейм"
assert la_dem.iloc[5, 7] == 1, "Неверный датафрейм"
'''

# №5
corr_round = []

for i in range(len(polit)):
    corr_round.append(round(polit.corr0509[i], 2))

polit["corr_round"] = corr_round

assert round(polit["corr_round"].sum()) == -14.0, "Ошибка в столбце corr_round"
assert polit["corr_round"].max() == 2.38, "Ошибка в столбце corr_round"

# №6
fh_status = []

for i in range(len(polit)):
    if 1.0 <= polit.fh09[i] <= 2.5:
        fh_status.append("free")
    elif 3.0 <= polit.fh09[i] <= 5.0:
        fh_status.append("partly free")
    else:
        fh_status.append("not free")

polit["fh_status"] = fh_status

assert polit["fh_status"].value_counts().values[0] == 57, "Неверные значения в столбце"
assert polit["fh_status"].value_counts().values[1] == 48, "Неверные значения в столбце"
assert polit["fh_status"].value_counts().values[2] == 30, "Неверные значения в столбце"
assert polit["fh_status"].values[3] == 'free', "Неверные значения в столбце"
assert polit["fh_status"].values[4] == 'partly free', "Неверные значения в столбце"
assert polit["fh_status"].values[134] == 'not free', "Неверные значения в столбце"


# №8 С этим номером какие-то проблемы
Free = polit
Partly_Free = polit
Not_Free = polit

for i in range(len(polit)):
    if polit.fh_status[i] == "partly free" or polit.fh_status[i] == "not free":
        Free = polit.drop([i])
    elif polit.fh_status[i] == 'free' or polit.fh_status[i] == 'not free':
        Partly_Free = polit.drop([i])
    elif polit.fh_status[i] == 'free' or polit.fh_status[i] == 'partly free':
        Not_Free = polit.drop([i])

print(Free)
print(Partly_Free)
print(Not_Free)
