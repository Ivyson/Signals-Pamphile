yn=0
print('y[n] = ax[n] +(1-a)y[n-1]\nWhereby a = 0.02, x[n]=n')
for i in range(0, 44):
    y = 0.02*i +(1-0.02)*yn
    yn = y
    print(f'y[{i}] = {y}')
    print(y)