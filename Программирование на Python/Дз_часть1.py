import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math

dat = [["Вжик", "Zipper the Fly", "fly", "0.7"],
       ["Гайка", "Gadget Hackwrench", "mouse", None],
       ["Дейл", "Dale", "chipmunk", "1"],
       ["Рокфор", "Monterey Jack", "mouse", "0.8"],
       ["Чип", "Chip", "chipmunk", "0.2"]]

# №1
df = pd.DataFrame(dat, columns=["ru_name", "en_name", "class", "cheer"])

df["cheer"] = pd.to_numeric(df["cheer"])

assert type(df) == pd.core.frame.DataFrame, "Объект df не является датафреймом"
assert df.shape == (5, 4), "Неверное число строк и столбцов"
assert df.dtypes.values[-1] == float, "Последний столбец не имеет тип float"

# №2
N = len(df.index)
assert N == 5, "Неверный ответ"

# №3
cn = 0
length = len(df.index)

df = df.fillna('NaN')

for i in range(0, length):
    if df.cheer[i] != "NaN":
        cn += 1
    else:
        continue

assert cn == 4, "Неверный ответ"

# №4
g = df.iat[2, 1]

assert g == 'Dale', "Неверный ответ"

# №5 и 6
df1 = df.copy()
df1 = df1.drop(['cheer'], axis=1)
df1 = df1.drop(labels=[0, 4], axis=0)
df1 = df1.reset_index(drop=True)
df1.rename(columns={"ru_name": 0, "en_name": 1, "class": 2}, inplace=True)

assert df1.shape == (3, 3), "Неверное число строк и столбцов"
assert df1[1].values[-2] == "Dale", "Выбраны не те строки или столбцы"

assert sum(df.T.index == ["ru_name", "en_name", "class", "cheer"]) == 4, "Неверно"

# №7
df["logcheer"] = ["0", "0", "0", "0", "0"]
for i in range(length):
    if df["cheer"].values[i] == 'NaN':
        df["logcheer"].values[i] = np.NaN
    else:
        df["logcheer"].values[i] = math.log(df["cheer"].values[i])

assert math.isclose(df["logcheer"].values[-2], -0.22314, abs_tol=1e-5), "Неверно"
assert math.isnan(df["logcheer"].values[-4]), "Неверно"

# №8
x = []
alla = []
for i in range(length):
    alla.append(df["class"].values[i])
    if df["class"].values[i] not in x:
        x.append(df["class"].values[i])

y = []
for i in x:
    count = 0
    for a in alla:
        if i == a:
            count += 1
    y.append(count)

plt.title('Класс и количество посторений')
plt.xlabel('Класс')
plt.ylabel('Количество повторений')
plt.bar(x, y)
plt.show()

# №9
L = [{'id': 53050,
      'text': 'В рамках проекта «Социальный лифт» Вышка предоставляет льготы при поступлении абитуриентам, оказавшимся'
              ' в сложных жизненных обстоятельствах и социально-экономических условиях. В 2019 году льготу получил 71 '
              'человек, а в этом году университет готов оказать поддержку уже 165 абитуриентам.\n\nМы поговорили с '
              'ребятами, поступившими по программе, и делимся их историями в новом видео.\n\nПодробнее об условиях '
              'участия, сроках и количестве мест можно прочитать по ссылке: r.hse.ru/lift',
      'likes': {'count': 56, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 14370}},
     {'id': 53163,
      'text': 'Даже в самом загруженном расписании стоит оставить немного места для заботы о себе. «Вышка для своих» '
              'делится мартовской подборкой мероприятий [club6222726|Центра психологического консультирования ВШЭ]: от '
              'хатха-йоги до групповых кинопросмотров',
      'likes': {'count': 6, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 2460}},
     {'id': 53161,
      'text': 'Начался прием заявок на соискание премии HSE Alumni Awards. 19 марта стартует открытое '
              'онлайн-голосование, которое определит шорт-листы по каждой номинации. Лауреатами премии могут стать '
              'выпускники всех кампусов Вышки.\n\nЗаявки принимаются до 15 марта на сайте премии: bit.ly/2TzuxXn',
      'likes': {'count': 4, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 2144}},
     {'id': 53159,
      'text': 'Вышка заняла первое место среди российских вузов по десяти предметам в рейтинге QS World University '
              'Rankings by Faculty & Subject 2020. Всего университет представлен в 19 предметных рейтингах, а по пяти '
              'из них входит в топ-100 глобального списка.\n\nВ этом году ВШЭ также присутствует в 4 из 5 отраслей QS, '
              'в том числе впервые в «Естественных науках»',
      'likes': {'count': 90, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 7136}},
     {'id': 53136,
      'text': 'Почему изучать космос сложно, но интересно, для чего нужно наблюдать за геокороной Земли и как вернуть '
              'престиж профессии учёного? Рассказывает преподаватель факультета физики ВШЭ Игорь Балюкин, победитель '
              'конкурса ИКИ РАН в номинации «Лучшая работа, выполненная молодыми учеными»',
      'likes': {'count': 15, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 4255}},
     {'id': 53133,
      'text': 'В феврале и начале марта сотрудники Вышки провели заключительный этап олимпиады '
              '[club154631231|«Я — профессионал»] по восьми направлениям. В соревнованиях приняли участие более 1600 '
              'студентов из 65 регионов и 212 вузов',
      'likes': {'count': 4, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 3266}},
     {'id': 53132,
      'text': 'В первый день весны на краешке Москвы прошёл зимний спортивный фестиваль [club35314658|HSE SNOW FEST], '
              'в котором приняли участие 460 человек. Горячий чай с блинами, квесты, соревнования по горным лыжам и '
              'сноуборду ждали студентов, преподавателей и выпускников Вышки',
      'likes': {'count': 76, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 6847}},
     {'id': 53130,
      'text': 'Команда [club24893373|МИЭФ] и сборная Вышки заняли первое и второе места на российском этапе '
              '«инвестиционной олимпиады» CFA Institute Research Challenge. В апреле студенты отправятся на '
              'европейский финал в Иорданию, а в случае успеха — в Нью-Йорк на глобальный финал конкурса',
      'likes': {'count': 23, 'user_likes': 0, 'can_like': 1, 'can_publish': 1},
      'views': {'count': 4376}}]

info = pd.DataFrame(L)

assert info.shape == (8, 4), "Неверное число строк или столбцов"

# №10
nlikes = []
for i in range(len(info.likes)):
    dict_likes = info.likes[i]
    nlikes.append(dict_likes['count'])

nviews = []
for i in range(len(info.views)):
    dict_views = info.views[i]
    nviews.append(dict_views['count'])

info["nlikes"] = nlikes
info["nviews"] = nviews

assert info.loc[3, "nlikes"] == 90, "Неверное решение"
assert info.loc[6, "nlikes"] == 76, "Неверное решение"
assert info.loc[5, "nviews"] == 3266, "Неверное решение"
assert info.loc[2, "nviews"] == 2144, "Неверное решение"
