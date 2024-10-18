import sympy as sm
# 0.529
t = sm.Symbol('t')
s = sm.Symbol('s')
omega = 2*sm.pi*6
u = sm.Heaviside
y = 64*sm.cos((5*sm.pi)*t)*(u(t+0.3)- u(t-0.3))
# print(lp)
F = sm.fourier_transform(y,t,s)
print(sm.Function('F')(s),sm.Abs(F.subs(s, omega)))
# sm.plot(y, (t, -0.5, 0.5))
