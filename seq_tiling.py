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

                    t.append(t_n)
                    x.append(i)
            
            if t_n > T and i > H:
                t_i += 14 - t[-1]

    if t_n != 0:
        return (i, t_h/t_n)

count = 0
l = 0.1
a = 0
b = 0.05
pr = 0
p = 0.9
N = 4e6
T = 14
x0 = 10
H = 2e4
eps = [0.005, 2e-9]

while abs(pr - b) > 0.01 and x0 > 0:
    x0, pr = simProcess(l, p, a, N, T, x0, H)
    print(pr)

    if count == 0:
        l = l - eps[0]*(pr - b)
        if l < 0.05:
            l = 0.05
        count = 1
    else:
        a = a + eps[1]*(pr - b)
        if a < 0:
            a = 0
        elif a > 1e-7:
            a = 1e-7
        count = 1
