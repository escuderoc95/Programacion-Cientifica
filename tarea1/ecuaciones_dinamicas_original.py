# Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
# Definir parámetros
R = 6
L = 100e-6
C = 50e-6
Vg = 12
V = 6
D = V / Vg
Il= V/R
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

D0 = 0.5
t_pwm = 0

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
    else:
        u_sw[i] = 0

    t_pwm += dt

    # Ecuaciones diferenciales
    if i == 1:
        u_sw[i] = 1
        diL_dt_sw = (Vg * u_sw[i] - 0) / L
        dVc_dt_sw = (0 - 0 / R) / C
        iL_sw[i] = 0
        vC_sw[i] = 0
    else:
        diL_dt_sw = (Vg * u_sw[i] - vC_sw[i - 1]) / L
        dVc_dt_sw = (iL_sw[i - 1] - vC_sw[i - 1] / R) / C
        iL_sw[i] = diL_dt_sw * dt + iL_sw[i - 1]
        vC_sw[i] = dVc_dt_sw * dt + vC_sw[i - 1]

        # Acción del diodo
        if iL_sw[i] < 0:
            iL_sw[i] = 0

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, vC_sw, '-r', linewidth=1)
plt.xlim([10e-3, 20e-3])
plt.xlabel('Tiempo (s)')
plt.ylabel('Vc_sw (V)')
plt.title('Voltaje a la salida')

plt.subplot(2, 1, 2)
plt.plot(t, iL_sw, '-b', linewidth=1)
plt.xlim([10e-3, 20e-3])
plt.xlabel('Tiempo (s)')
plt.ylabel('iL_sw (A)')
plt.title('Corriente en el inductor')

plt.tight_layout()
#plt.show()
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")