# Skript zum Plotten einer 2D-Trajektorie

import matplotlib.pyplot as plt
import numpy as np

# Trajektorie definieren
t = np.linspace(0, 10, 100)


def x(t):
    return 2*t + np.sin(2*t)


def y(t):
    return 3*t


# Plot erstellen
fig, sub = plt.subplots()
X = x(t)
Y = y(t)
sub.plot(X, Y, 'g', label=r'$\vec{r}(t)$')
sub.grid()

# Achsenbeschriftungen, Titel und Legende
sub.set_xlabel(r'$x$')
sub.set_ylabel(r'$y$')
sub.set_title('Trajektorie')
sub.legend()

# Plot anzeigen
plt.show()
