# Firstly Find the original Ewuation:

#  Y[n]=x[n]+ay[n-1]
yn = 0
a = 0.75
for i in range(0, 12): # This is for getting A vaue at index 11, calculating 
    # From zero to 11.
    y = i*0.8**i +yn
    yn = y*a
    print(y)

print(f'Your answer is at y[11] = {y}')