# -*- coding: utf-8 -*-
# PN: 16 lesson python - sin cos, Created Mar, 2017
# Version 1.0
# KW: numpy, matplotlib
# Link: 
# --------------------------------------------------- lib import
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------- x, y setting
x = np.arange(0, 360)
y = np.sin(2 * x * np.pi / 180.0)
z = np.cos(x * np.pi / 180.0)
# --------------------------------------------------- plotting, generate -> x, y scale setting -> show
plt.plot(x, y, color = 'blue', label = "Sin(2X)")
plt.plot(x, z, color = 'red', label = "Cos(X)")
plt.xlim(0, 360)
plt.ylim(-1.2, 1.2)

plt.xlabel("Degree")
plt.ylabel("Range")

plt.title("Sin & Cos function")
plt.legend()	# fetch label elements

plt.show()

