# Skript zum Plotten eines 2D-Skalarfeldes mit Farbcodierung

# Beispiel-Feld hier (fuer z=0): p(x,y) = 1000+(0.1x+0.5)(-0.2y+1.0)
# fuer ein anderes Feld p durch Felddefinition ersetzen und ggf. umbenennen

# benoetigte Bibliothek importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen

# Definitions- und Wertebereich Graph (jeweils 0 <= x,y <= 10 mit 10x10 Werten)
x = np.linspace(0, 10, 11)  # 11 nicht dabei
y = np.linspace(0, 10, 11)  # 11 nicht dabei
X, Y = np.meshgrid(x, y)  # 10x10 Grid von x- und y-Werten

# Definition Feld p
p = 1000 + (0.1 * X + 0.5) * (-0.2 * Y + 1.0)

# Plot vorbereiten
fig, ax = plt.subplots()

# Skalarfeld plotten und nach hoehe des Wertes faerben
contour = ax.contourf(X, Y, p, cmap='coolwarm')
fig.colorbar(contour, ax=ax, label='Druck [hPa]')  # ergaenzt Farblegende

# Beschriftungen
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Druckfeld')

plt.show()
