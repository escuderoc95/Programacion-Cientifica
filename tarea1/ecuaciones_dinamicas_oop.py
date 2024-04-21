import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
class ConvertidorDCDC:
    def __init__(self, R, L, C, Vg, V, D0=0.5):
        self.R = R
        self.L = L
        self.C = C
        self.Vg = Vg
        self.V = V
        self.D0 = D0
        self.Fsw = 50e3
        self.Tsw = 1 / self.Fsw
        self.dt = 1e-7
        self.Tmax = 20e-3
        self.t = np.arange(0, self.Tmax, self.dt)
        self.imax = len(self.t)
        self.iL_sw = np.zeros(self.imax)
        self.vC_sw = np.zeros(self.imax)
        self.d_sw = np.zeros(self.imax)
        self.u_sw = np.zeros(self.imax)

    def calcular(self):
        t_pwm = 0
        for i in range(self.imax):
            self.d_sw[i] = self.D0
            if self.t[i] >= 12e-3:
                self.d_sw[i] = self.D0 + 1 / 100

            if t_pwm >= self.Tsw:
                t_pwm = 0

            if t_pwm <= self.d_sw[i] * self.Tsw:
                self.u_sw[i] = 1
            else:
                self.u_sw[i] = 0

            t_pwm += self.dt

            if i == 1:
                self.u_sw[i] = 1
                diL_dt_sw = (self.Vg * self.u_sw[i] - 0) / self.L
                dVc_dt_sw = (0 - 0 / self.R) / self.C
                self.iL_sw[i] = 0
                self.vC_sw[i] = 0
            else:
                diL_dt_sw = (self.Vg * self.u_sw[i] - self.vC_sw[i - 1]) / self.L
                dVc_dt_sw = (self.iL_sw[i - 1] - self.vC_sw[i - 1] / self.R) / self.C
                self.iL_sw[i] = diL_dt_sw * self.dt + self.iL_sw[i - 1]
                self.vC_sw[i] = dVc_dt_sw * self.dt + self.vC_sw[i - 1]

                if self.iL_sw[i] < 0:
                    self.iL_sw[i] = 0

    def graficar(self):
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        plt.plot(self.t, self.vC_sw, '-r', linewidth=1)
        plt.xlim([10e-3, 20e-3])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Vc_sw (V)')
        plt.title('Voltaje en el condensador')

        plt.subplot(2, 1, 2)
        plt.plot(self.t, self.iL_sw, '-b', linewidth=1)
        plt.xlim([10e-3, 20e-3])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('iL_sw (A)')
        plt.title('Corriente en el inductor')

        plt.tight_layout()
        #plt.show()

# Uso de la clase
convertidor = ConvertidorDCDC(R=6, L=100e-6, C=50e-6, Vg=12, V=6)
convertidor.calcular()
convertidor.graficar()
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")