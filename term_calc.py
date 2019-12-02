### Constantes circuito ###
V_res = 5.0/(pow(2,8) - 1)
Av = 10.0/4.7 ## Rf / R3
R = 10.0e3 ## R wheatstone
E = 5.0
E1 = 2.5
### Puntos sensor ###
x1 = 75.10
y1 = 385.10
x2 = 26.25
y2 = 9330
### Ecuación sensor ###
m = (y2 - y1)/(x2 - x1)

def get_temp(adc_val):
    e2 = E2(V_in(adc_val))
    r_sen = RSen(dR(e2))
    return temp(r_sen)
def V_in(adc_val):
    return V_res * adc_val
def E2(v_in):
    return (Av*E1 - v_in)/Av
def dR(E2):
    return (R * (E - 2*E2))/(E - E2)
def RSen(dr):
    return R - dr
def temp(r_sen):
    return (r_sen - y1)/m+x1
