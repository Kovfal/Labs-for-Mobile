import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
print('Ряд распределения дискретной случайной величины и визуализация её распределения')

X = np.array([-10, -7, -4, 9])
p = np.array([0.2, 0.2, 0.3, 0.3])
print('X: ', X)
print('p: ', p)
r = pd.DataFrame([X, p])
r.columns = [''] * len(X)
r.index = ['X', 'p']
print(r.loc['X'])
print(r.loc['p'])
print(sum(r.loc['p']))
print(any(r.loc['p'] > 1))
print(any(r.loc['p'] < 0))
print(r.to_latex(bold_rows=True, decimal=',', column_format='|l|c|c|c|c|c|'))

with open('table1.tex', 'w') as tf:
    tf.write(r.to_latex())

print(X, p)

plt.vlines(X, 0, p, colors='red', lw=5, alpha=0.5)
plt.axis([-11, 10, 0, 0.5])
plt.savefig('xprob.png')

plt.plot(X, p, '--* ', color='red')

plt.show()

print("Математическое ожидание, дисперсия и другие характеристики случайных величин")

ex = np.dot(X, p)
print('Математическое ожидание случайной величины X: ', ex)

dx = np.dot(X**2, p) - np.dot(X, p)**2
print('Дисперсия X: ', dx)

sx = np.sqrt(dx)
print('Стандартное отклонение X: ', sx)

cv = sx / ex
print('Коэффициент вариации: ', cv)


