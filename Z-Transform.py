# Firstly Find the original Ewuation:

#  Y[n]=x[n]+ay[n-1]
yn = 0
a = 0.02
for i in range(0, 56): # This is for getting A vaue at index 11, calculating 
    # From zero to 11.
    y = a*i +(1-a)*yn
    yn = y
    print(y)
    print(f'Your answer is at y[{i}] = {y}')

# print(f'Your answer is at y[11] = {y}')