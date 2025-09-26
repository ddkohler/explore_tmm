"""simple script illustrating the principle of the simulation"""

import matplotlib.pyplot as plt
import numpy as np
import tmm


rp = tmm.dielectrics.rp_n2
air = tmm.dielectrics.n_air
ps = tmm.dielectrics.insulator(n=1.5)  #  close enough?


l_rp_um = 0.3
l_ps_um = 10

eV = np.linspace(1.5, 2.5, 501)


def contrast(sample:tmm.FilmStack, reference:tmm.FilmStack, x):
    r1 = sample.RT(x)[0]
    r2 = reference.RT(x)[0]
    return 0.5 * (r1 - r2) / (r1 + r2)


fig, ax = plt.subplots()

ax.plot(eV, tmm.dielectrics.rp_n2(eV).real)  # n
ax.plot(eV, tmm.dielectrics.rp_n2(eV).imag)  # k

# define a layer stack and try to see reflection
sample = tmm.FilmStack([air, ps, rp, air], [l_ps_um * 1e-4, l_rp_um * 1e-4])
reference = tmm.FilmStack([air, ps, air], [l_ps_um])  # maybe?

fig, ax = plt.subplots()
#  ax.plot(eV, contrast(sample, reference, eV))
ax.plot(eV, sample.RT(eV)[0])

plt.show()
