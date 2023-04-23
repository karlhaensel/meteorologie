# benoetigte Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# Definitions- und Wertebereich Graph
X = np.linspace(0, 1, 100)
Y = X
x, t = np.meshgrid(X, Y)

# Definition Feld T
T = np.exp(-25*(x-t)**2)

# Feld plotten und nach Hoehe des Wertes faerben
plt.contourf(x, t, T, cmap='coolwarm', levels=np.linspace(0, 1, 11))
plt.colorbar(label='Temperatur T(x,t)')

# Punkt markieren und beschriften
plt.plot(
    0.6, 0.75, 'x',
    markerfacecolor='black', markeredgecolor='black', markersize=7)
plt.text(
    0.6, 0.79, '(0.6, 0.75)',
    color='black', fontsize=10, ha='center', va='center')

# Beschriftungen
plt.xlabel('Weg x')
plt.ylabel('Zeit t')
plt.title('Temperaturverlauf im x-t-Diagramm')

# Grafik ggf. speichern und anzeigen
# plt.savefig('feld.png')
plt.show()
