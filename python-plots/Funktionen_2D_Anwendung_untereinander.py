# benoetigte Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# Definitionsbereich
xmin, xmax, xpunkte = 0, 1, 100
x = np.linspace(xmin, xmax, xpunkte)

# Funktion definieren und zeichnen
y1 = np.exp(-25*(x-0.75)**2)
y2 = np.exp(-25*(0.5-x)**2)

# Figur samt Subplots erstellen und zeichnen (Bildgroesse figsize)
fig1, (sub1, sub2) = plt.subplots(2, 1, figsize=(5, 10))
sub1.plot(x, y1, 'g', label='$T(x)=e^{-25(x-0.75)^2}$')
sub2.plot(x, y2, 'r', label='$T(t)=e^{-25(0.5-t)^2}$')

# Beschriftungen hinzufuegen und Achsen einstellen
sub1.set_title('Temperaturverlauf um 18 Uhr ($t=0.75$)')
sub1.legend(loc='best')
sub1.grid(True)
sub1.set_xlabel('x')
sub1.set_xticks(np.linspace(0, 1, 11))
sub1.set_ylabel('$T(x, t=0.75)$')
sub1.set_yticks(np.linspace(0, 1, 11))
sub2.set_title('Temperaturverlauf auf der Mitte des Weges ($x=0.5$)')
sub2.legend(loc='best')
sub2.grid(True)
sub2.set_xlabel('t')
sub2.set_xticks(np.linspace(0, 1, 11))
sub2.set_ylabel('$T(x=0.5, t)$')
sub2.set_yticks(np.linspace(0, 1, 11))

# Graph anzeigen
fig1.show()
plt.show()
