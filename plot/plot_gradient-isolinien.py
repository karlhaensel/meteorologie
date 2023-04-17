# Skript zum Plotten eines 2D-Gradienten samt Isolinien

# Beispiel-Feld hier (fuer z=0): p(x,y) = 1000+(0.1x+0.5)(-0.2y+1.0)
# fuer ein anderes Feld p durch Felddefinition ersetzen und in
# gradient(x,y) xgrad durch x-Komponente des Gradienten ersetzen (genauso y)


# benoetigte Bibliothek importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen
import matplotlib.cm as cm  # fuer die Farblegende


# Definitions- und Wertebereich Graph (jeweils 0 <= x,y <= 10 mit 10x10 Werten)
x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)
X, Y = np.meshgrid(x, y)


# Definition Feld p
p = 1000 + (0.1 * X + 0.5) * (-0.2 * Y + 1.0)


# Definition Gradient-Funktion
def gradient(x, y):
    xgrad = -0.02 * y + 0.1
    ygrad = -0.02 * x - 0.1
    return xgrad, ygrad


# Berechnung Gradient und Betraege
XGRAD, YGRAD = gradient(X, Y)
betraege = np.sqrt(XGRAD**2 + YGRAD**2)


# Gradient-Vektoren zeichnen und nach jeweiligem Betrag faerben
plt.quiver(X, Y, XGRAD, YGRAD, betraege, cmap='coolwarm')

# Isobaren einzeichnen (Variable levels bestimmt Anzahl der Isobaren)
plt.contour(X, Y, p, levels=10, colors='g')

# Beschriftungen
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient mit Isobaren (z=0)')

# Farb-Legende fuer Gradient-Betraege
farbskala = cm.ScalarMappable(cmap='coolwarm')
farbskala.set_array(betraege)
legende = plt.colorbar(farbskala)
legende.set_label('Betrag des Gradienten')

plt.show()
