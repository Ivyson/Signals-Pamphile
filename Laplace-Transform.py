import sympy as sm
## The input function is a unit ramp.. therefore..
u = sm.Heaviside
t = sm.Symbol('t')
s = sm.Symbol('s')
Vin = t*u(t)
# From The KVL We get the  equation :
# Vin = V_r + Vc -> tµ(t)=i(t)R+(1/C)∫i(tau)dtau=i(t)+(1/5)∫i(t)
# 1/s^2 = I(s)+(1/5s)I(s)
# 1/s^2 = I(s) [1+1/5s]
# 1/s^2[1+1/5s]=I(s)
r,c = 4, 0.5
I = 8/((r+1/(c*s))*(s+0.4))

print(sm.apart(I))
# The `i` is the actual equation of the current
i = sm.inverse_laplace_transform(I,s,t)
print(i)

# Because the voltage drop across a capacitor is Vout = (1/5)∫_0^2.8 (i(t))
# Vout = sm.integrate(i, (t,0, 2.8))/5
# print(Vout)