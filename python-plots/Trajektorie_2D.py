# Skript zum Plotten einer 2D-Trajektorie
# hier als Beispiel der 2D-Ortsvektor r(t) mit  x = 2t + sin(2t); y = 3t

# benoetigte Bibliotheken importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen

# Zeit t als unabhängige Variable definieren
t = np.linspace(0, 10, 100)


# Trajektorie in Abhaengigkeit von t definieren
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
