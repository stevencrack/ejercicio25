import numpy as np
import matplotlib.pyplot as plt

#constantes

const_helio = 1.33e20
masa_tierra = 5.972e24
masa_sol = 332950* masa_tierra
ua = 1.496e+11

#Venus
Xven =-3.41E-01*ua
Yven = 6.38E-01*ua
Zven = 2.83E-02*ua

r_ven = np.sqrt(Xven**2+Yven**2+Zven**2)
print r_ven

#tierra

Xtierra =-6.86E-01*ua
Ytierra =-7.33E-01*ua
Ztierra =-6.64E-05*ua

r_earth = np.sqrt(Xtierra**2+Ytierra**2+Ztierra**2)
print r_earth

#Mercurio

Xmercurio = 2.88E+01*ua
Ymercurio =-8.20E+00*ua
Zmercurio =-4.95E-01*ua

r_merc = np.sqrt(Xmercurio**2+Ymercurio**2+Zmercurio**2)
print r_merc

alpha = np.random.random_sample()*4
print alpha


