import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

# Задача 6
n, p = 5, 0.6
x = st.binom(n, p)

print('Вероятность того, что среди этих детей есть не менее двух девочек = ', x.pmf(2) + x.pmf(3) + x.pmf(4) + x.pmf(5))

x = np.arange(0, n + 1)
prob = st.binom.pmf(x, n, p)
plt.vlines(x, 0, prob, colors='red', lw=50, alpha=0.7)

plt.show()

# Задача 9
n, p = 6, 0.8
x = st.binom(n, p)

print('Вероятность того, что к обеденному перерыву перегреются 4 мотора = ', x.pmf(4))

x = np.arange(0, n + 1)
prob = st.binom.pmf(x, n, p)
plt.vlines(x, 0, prob, colors='purple', lw=50, alpha=0.7)

plt.show()
