import numpy as np
import pandas as pd
import scipy.stats as sps
from pandas import DataFrame

df = pd.DataFrame({
    'Аукционный дом': ['Аукцион 25', 'СфераКар'] * 25,
    'Марка автомобиля': ['TOYOTA', 'NISSAN', 'HONDA', 'SUBARU', 'MAZDA'] * 10,
    'Модель автомобиля': ['ALLION', 'AD', 'CIVIC', 'IMPREZA G4', 'CX-8', 'CALDINA', 'AURA', 'ACCORD', 'FORESTER',
                          'AZ-1'] * 5,
    'Цвет автомобиля': ['Черный', 'Белый', 'Серебристый', 'Красный', 'Зеленый'] * 10,
    'Аукцион': ['ARAI Bayside', 'AEP Nyusatsu'] * 25,
    'Оценка состояния автомобиля': sps.randint(low=0, high=10).rvs(size=50),
    'Количество лотов на аукционе': sps.randint(low=0, high=100).rvs(size=50),
    'Стартовая цена лота': sps.randint(low=100000, high=500000).rvs(size=50),
    'Конечная цена лота': sps.randint(low=600000, high=5000000).rvs(size=50)
})

multi_index = df.groupby(['Аукционный дом', 'Марка автомобиля', 'Модель автомобиля']).sum().index
print(multi_index)
print('')

# количество автомобилей на аукционе с каждым цветом (способ 1)
df_count_color_1 = df.groupby(['Марка автомобиля', 'Модель автомобиля'])['Цвет автомобиля'].value_counts()

print('1й способ!!!')
print('')
print(df_count_color_1)
print('')

# количество автомобилей на аукционе с каждым цветом (способ 2)
count_white = [0, 0, 0, 0, 0, 0]
count_green = [0, 0, 0, 0, 0, 0]
count_red = [0, 0, 0, 0, 0, 0]
count_silver = [0, 0, 0, 0, 0, 0]
count_black = [0, 0, 0, 0, 0, 0]
count_all = [0, 0, 0, 0, 0, 0]
for i in df['Цвет автомобиля']:
    if i == 'Белый':
        count_white[0] += 1
        count_white[5] += 1
        count_all[0] += 1
        count_all[5] += 1
    elif i == 'Зеленый':
        count_green[1] += 1
        count_green[5] += 1
        count_all[1] += 1
        count_all[5] += 1
    elif i == 'Красный':
        count_red[2] += 1
        count_red[5] += 1
        count_all[2] += 1
        count_all[5] += 1
    elif i == 'Серебристый':
        count_silver[3] += 1
        count_silver[5] += 1
        count_all[3] += 1
        count_all[5] += 1
    elif i == 'Черный':
        count_black[4] += 1
        count_black[5] += 1
        count_all[4] += 1
        count_all[5] += 1

color = ['Белый', 'Зеленый', 'Красный', 'Серебристый', 'Черный', 'All']
car = ['NISSAN', 'MAZDA', 'SUBARU', 'HONDA', 'TOYOTA', 'All']
df_bla = count_white, count_green, count_red, count_silver, count_black, count_all
df_count_color_2 = pd.DataFrame(df_bla, car, color)
print('2й способ!!!')
print('')
print(df_count_color_2)
print('')

# количество автомобилей на аукционе с каждым цветом (способ 3)
df_count_color_3 = pd.crosstab(df['Марка автомобиля'], df['Цвет автомобиля'], margins=True)
print('3й способ!!!')
print('')
print(df_count_color_3)
print('')
'''
# средняя оценка каждой макри и модели автомобиля
df_sr_ocenk_car = pd.crosstab(df['Марка автомобиля'], df['Модель автомобиля'], values=df['Оценка состояния автомобиля'],
                              aggfunc=np.mean)
print('средняя оценка каждой макри и модели автомобиля')
print(df_sr_ocenk_car)

# средние параметры по каждой марке автомобиля
df_info_marks_car = pd.pivot_table(df, index=['Марка автомобиля'])
print('средние параметры по каждой марке автомобиля')
print(df_info_marks_car)

# количество автомобилей определенной марки и модели на определенном аукционе
df_count_car_on_auk = pd.pivot_table(df, values='Количество лотов на аукционе', index=['Модель автомобиля',
                                                                                       'Марка автомобиля'],
                                     columns=['Аукцион'], aggfunc=np.sum)
print('количество автомобилей определенной марки и модели на определенном аукционе')
print(df_count_car_on_auk)

# количество автомобилей определенной марки и модели на определенном аукционе и общее количество на обоих аукционах
df_countcar = pd.pivot_table(df, values='Количество лотов на аукционе', index=['Модель автомобиля', 'Марка автомобиля'],
                             columns=['Аукцион'], aggfunc=np.sum, margins=True)
print('количество автомобилей определенной марки и модели на определенном аукционе и общее количество на обоих аукционах')
print(df_countcar)

# основная информация об автомобилях
df_car_info = pd.pivot_table(df,
                             values=['Количество лотов на аукционе', 'Стартовая цена лота'],
                             index=['Модель автомобиля', 'Марка автомобиля'],
                             columns=['Аукцион'],
                             aggfunc=[np.min, np.mean, np.max],
                             margins=True)
print('основная информация об автомобилях')
print(df_car_info)
'''
df.to_csv('AuctionCar.csv')
