# Skript zum Plotten eines Skalarfeldes samt zeitlicher Aenderung
# mit Farbcodierung und Punktmarkierung

# Beispiel-Feld hier (fuer z=0): p(x,y) = 1000+(0.1x+0.5)(-0.2y+1.0)
# fuer ein anderes Feld p durch Felddefinition ersetzen und ggf. umbenennen

# benoetigte Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# Definitions- und Wertebereich Graph
X = np.linspace(0, 1, 100)
Y = X
x, t = np.meshgrid(X, Y)

# Definition Feld T
T = np.exp(-25*(x-t)**2)

# Plot vorbereiten
fig, ax = plt.subplots()

# Feld plotten und nach Hoehe des Wertes faerben
contour = ax.contourf(x, t, T, cmap='coolwarm', levels=np.linspace(0, 1, 11))
fig.colorbar(contour, ax=ax, label='Temperatur T(x,t)')  # ergaenzt Farblegende

# Punkt markieren und beschriften
ax.plot(
    0.6, 0.75, 'x',
    markerfacecolor='black', markeredgecolor='black', markersize=7)
ax.text(
    0.6, 0.79, '(0.6, 0.75)',
    color='black', fontsize=10, ha='center', va='center')

# Beschriftungen
ax.set_xlabel('Weg x')
ax.set_ylabel('Zeit t')
ax.set_title('Temperaturverlauf im x-t-Diagramm')

# Grafik ggf. speichern und anzeigen
# plt.savefig('feld.png')
plt.show()
