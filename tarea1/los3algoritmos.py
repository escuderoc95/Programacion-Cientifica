import numpy as np
import matplotlib.pyplot as plt

# Variables del convertidor
R = 6 #
L = 100e-6
C = 50e-6
Vg = 12
V = 6
D = V / Vg
Il = V / R
Fsw = 50e3
Tsw = 1 / Fsw
dt = 1e-7
Tmax = 20e-3
t = np.arange(0, Tmax, dt)
imax = len(t)

# Inicializar vectores para almacenar resultados
iL_sw = np.zeros(imax)
vC_sw = np.zeros(imax)
d_sw = np.zeros(imax)
u_sw = np.zeros(imax)

#inicializar duty y tiempo del pwm
D0 = 0.5
t_pwm = 0

u_sw[0] = 1
diL_dt_sw = 0
dVc_dt_sw = 0
iL_sw[0] = 0
vC_sw[0] = 0


# Ciclo principal
for i in range(imax):
    # Calcular duty cycle
    d_sw[i] = D0
    if t[i] >= 12e-3:
        d_sw[i] = D0 + 1 / 100

    # PWM
    if t_pwm >= Tsw:
        t_pwm = 0

    if t_pwm <= d_sw[i] * Tsw:
        u_sw[i] = 1

    t_pwm += dt
#algorimo 1
for i in range(1,imax):
    diL_dt_sw = (Vg * u_sw[i] - vC_sw[i - 1]) / L
    dVc_dt_sw = (iL_sw[i - 1] - vC_sw[i - 1] / R) / C
    iL_sw[i] = diL_dt_sw * dt + iL_sw[i - 1]
    vC_sw[i] = dVc_dt_sw * dt + vC_sw[i - 1]

        # Acción del diodo
    if iL_sw[i] < 0:
        iL_sw[i] = 0

#algorimo 2
# Cálculo de potencia instantánea
potencia_salida = vC_sw * iL_sw
# Cálculo de la potencia promedio utilizando ciclos for

suma_potencia = 0
for potencia_instantanea in potencia_salida:
    suma_potencia += potencia_instantanea

potencia_promedio = suma_potencia / len(potencia_salida)

# Imprimir la potencia promedio de salida
print("Potencia promedio de salida:", potencia_promedio)
#algorimo 3
# Encontrar cruces por cero
zero_crossings = np.where(np.diff(np.sign(iL_sw)))[0]

# Calcular periodo
periodo = np.mean(np.diff(t[zero_crossings]))

print("El periodo de la señal iL_sw es:", periodo)
