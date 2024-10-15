import sympy as sm

t = sm.Symbol('t')
y = 64*sm.cos((5*sm.pi)*t)
sm.plot(y, (t, -0.5, 0.5))