import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def calcul_symb():
    x, phi, dx, dphi, d2x, d2phi, g, l, m, M, F = \
        sp.symbols('x, phi, x^(1}, phi^(1), x^(2), phi^(2), g, l, m, M, F')
    EQP = d2x*sp.cos(phi)+l*d2phi+g*sp.sin(phi)
    EQC = -F + (m+M)*d2x+m*l*sp.cos(phi)*d2phi-m*l*sp.sin(phi) * dphi**2
    Sol = sp.solve([EQP, EQC], [d2x, d2phi])
    D2X = Sol[d2x].simplify()
    D2PHI = Sol[d2phi].simplify()
    D2X_F = sp.lambdify([phi, dx, dphi, F, g, l, m, M], D2X, 'numpy')
    D2PHI_F = sp.lambdify([phi, dx, dphi, F, g, l, m, M], D2PHI, 'numpy')

    return D2X_F, D2PHI_F


def calcul_nume(D2X_F, D2PHI_F):
    def f(y, F, m, M, g, l):
        phi, dx, dphi = y[1], y[2], y[3]
        d2x = D2X_F(phi, dx, dphi, F, g, l, m, M)
        d2phi = D2PHI_F(phi, dx, dphi, F, g, l, m, M)
        return [dx, dphi, d2x, d2phi]

    def F(t):
        return 0

    M, m, l, g = 1, 0.1, 0.5, 9.81
    angleinit = 180.0-10.0
    x0, phi0, dx0, dphi0 = 0.0, angleinit*np.pi/180.0, 0.0, 0.0
    t_start, t_final = 0, 10
    y0 = [x0, phi0, dx0, dphi0]
    sol = solve_ivp(lambda t, y: f(y, F(t), m, M, g, l),
                    [t_start, t_final], y0, rtol=1e-10, atol=1e-10)
    t = sol.t.T
    y = sol.y.T

    plt.figure()
    plt.plot(t, y[:, 0], label='$x_c$')
    plt.grid('on')
    plt.xlim(t_start, t_final)
    plt.xlabel('temps (en s)')
    plt.ylabel('position du chariot (en m)')
    plt.legend()

    plt.figure()
    plt.plot(t, 180.0*y[:, 1]/np.pi, label='$\\phi$')
    plt.grid('on')
    plt.xlim(t_start, t_final)
    plt.xlabel('temps (en s)')
    plt.ylabel('angle du pendule (en degré)')
    plt.legend()

    plt.show()


D2X_F, D2PHI_F = calcul_symb()
calcul_nume(D2X_F, D2PHI_F)
