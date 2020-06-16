import matplotlib.pyplot as plt
import numpy as np

def simProcess(l, p, a, N, T, x0, H):
    t_n = 0
    i = x0

    t = [0]
    x = [x0]

    while i > 0 and i < N and t_n < T:
        q_plus = l*p*2*i*(N-i)/(N*(N-1))
        q_minus = a*i
        v_i = q_plus + q_minus

        t_i = np.random.exponential(v_i)
        jump = np.random.binomial(n=1, p = (q_plus/v_i))
        if jump == 1:
            i += 1
        else:
            i -= 1

        # 
        t_n += t_i
        
        t.append(t_n)
        x.append(i)
        
        # exceeds capacity
        if i > H:
            return (t, x, 1)
            
    return (t, x, 0)

count = 0
l = 0.1
a = 1e-8
b = 0.05
pr = 1    # probability of exceeding capacity, inital values for lambda and alpha are set so pr = 1 is true
p = 0.9
N = 4e6
T = 100
x0 = 10
H = 2e4   # hospital capacity

# stepsize
#eps[0] - < 0.005 too slow, do not exceed 0.05 
#eps[1] - < 1e-9 too slow, > 5e-9 keeps pr at 0 
# step stepsize below
eps = [0.01, 2e-9]

while abs(pr - b) > 0.01:
    all_ind = []

    for i in range(0,100):
        _, _, ind = simProcess(l, p, a, N, T, x0, H)
        all_ind.append(ind)

    pr = np.mean(all_ind)
    print(pr)

    if count == 0:
        l = l - eps[0]*(pr - b)
        if l < 0:
            l = 0
        count = 1
    else:
        a = a + eps[1]*(pr - b)
        if a < 0:
            a = 0
        # no recoveries if too high
        elif a > 1e-7:
            a = 1e-7
        count = 0
