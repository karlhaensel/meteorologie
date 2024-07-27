# Skript zum Plotten eines 2D-Gradienten samt Isolinien

# Beispiel-Feld hier (fuer z=0): p(x,y) = 1000+(0.1x+0.5)(-0.2y+1.0)
# fuer ein anderes Feld p ggf. umbenennen durch Felddefinition ersetzen und in
# gradient(x,y) xgrad durch x-Komponente des Gradienten ersetzen (ebenso ygrad)


# benoetigte Bibliothek importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen
import matplotlib.cm as cm  # fuer die Farblegende


# Definitions- und Wertebereich Graph (jeweils 0 <= x,y <= 10 mit 10x10 Werten)
x = np.linspace(0, 10, 11)  # 11 nicht dabei
y = np.linspace(0, 10, 11)  # 11 nicht dabei
X, Y = np.meshgrid(x, y)  # 10x10 Grid von x- und y-Werten

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

# Plot vorbereiten
fig, ax = plt.subplots()

# Gradient-Vektoren zeichnen und nach jeweiligem Betrag faerben
ax.quiver(X, Y, XGRAD, YGRAD, betraege, cmap='coolwarm')

# Isolinien fuer p (alos hier Isobaren) einzeichnen
ax.contour(X, Y, p, levels=10, colors='g')  # levels bestimmt Anzahl Isolinien

# Beschriftungen
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Gradient mit Isolinien (z=0)')  # bzw. hier konkret Isobaren

# Farb-Legende fuer Gradient-Betraege
farbskala = cm.ScalarMappable(cmap='coolwarm')
farbskala.set_array(betraege)
legende = plt.colorbar(farbskala, ax=ax)
legende.set_label('Betrag des Gradienten')

plt.show()
