def factorial(n):
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= n
        n -= 1
    return n_factorial


def P(n):
    P = factorial(n)
    return P


def C(n, k):
    C = factorial(n) / (factorial(k) * factorial(n - k))
    return C


def notC(n, k):
    C = factorial(n + k - 1) / (factorial(k) * factorial(n - 1))
    return C


def A(n, k):
    A = factorial(n) / factorial(n - k)
    return A


def notA(n, k):
    A = n ** k
    return A


def Pn(n, k, p):
    P_n = C(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return P_n


def left_k_right(n, p):
    q = 1 - p
    list_k = []
    left = int(((n * p) - q) // 1)
    right = int(((n * p) + p) // 1)
    for k in range(left, right + 1):
        list_k.append(k)
    return list_k


def P_nk(n, p, k):
    e = 2.718281828459045
    liambda = n * p
    return ((liambda ** k) * (e ** (-liambda))) / factorial(k)


def Pn_k(n, p, k):
    q = 1 - p
    x = (k - n * p) / ((n * p * q) ** 0.5)
    pi = 3.141592653589793
    e = 2.718281828459045
    f_x = (1 / (2 * pi) ** 0.5) * (e ** -((x ** 2) / 2))
    P = f_x / ((n * p * q) ** 0.5)
    return P
