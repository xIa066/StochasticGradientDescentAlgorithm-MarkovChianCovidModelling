import matplotlib.pyplot as plt
import numpy as np

def simProcess(l, p, a, N, T, x0, H):
    t_n = 0
    t_h = 0
    i = x0

    t = [0]
    x = [x0]

    while i > 0 and i < N and t_n < T:
        q_plus = l*p*2*i*(N-i)/(N*(N-1))
        q_minus = a*i
        v_i = q_plus + q_minus

        t_i = np.random.exponential(v_i)
        jump = np.random.binomial(n=1, p = (q_plus/v_i))
        t_n += t_i

        if t_n < T:
            if jump == 1:
                i += 1
            else:
                i -= 1

            if i > H:
                t_h += t_i

            if i == 0:
                i = 1

            t.append(t_n)
            x.append(i)
        
        if t_n > T and i > H:
            t_h += T - t[-1]

    return (i, t_h, t, x)

l = 0.1
a = 0
b = 0.05
pr = 0
p = 0.9
N = 4e6
T = 14
x0 = 10
H = 2e4
eps = [0.01, 2e-10]
x = []
t = []
t_n = 0
t_h = 0
i = 0
all_l = []
all_a = []
l_i = []
a_i = []

while i < 100 and x0 > 0:
    x0, t_h_temp, t_temp, x_temp = simProcess(l, p, a, N, T, x0, H)
    t += [t1 + T*i for t1 in t_temp]
    t_n += T
    t_h += t_h_temp
    x += x_temp

    pr = t_h/t_n
    print(pr)

    l -= eps[0]*(pr - b)
    if l < 0.001:
        l = 0.001
    all_l.append(l)
    l_i.append(len(all_l))

    a += eps[1]*(pr - b)
    if a < 0:
        a = 0
    elif a > 1e-7:
        a = 1e-7
    all_a.append(a)
    a_i.append(len(all_a))

    i += 1
