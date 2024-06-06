# Skript zum Plotten einer oder mehrerer 2D-Funktion
# genutzt wird dabei statt pyplot-Standard die mathematische Darstellung
# der Koordinatenachsen mit Ursprung in der Mitte und Achsenkreuz
# zweite Funktion ggf auskommentieren oder weitere analog dazu


# benoetigte Bibliothek importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen

# Definitionsbereich
xmin = -10
xmax = 10
xpunkte = 100
x = np.linspace(xmin, xmax, xpunkte)

# Funktion(en) und Wertebereich definieren
F1 = np.exp(x)
F2 = np.sin(x)
ymin = -10
ymax = 10

# Achsen
achsen = plt.gca()
# Obere und rechte Achse ausblenden
achsen.spines['top'].set_color('none')
achsen.spines['right'].set_color('none')
# untere Achse auf y=0
achsen.xaxis.set_ticks_position('bottom')
achsen.spines['bottom'].set_position(('data', 0))
# linke Achse auf x=0
achsen.yaxis.set_ticks_position('left')
achsen.spines['left'].set_position(('data', 0))
# Achsenausschnitte einstellen
plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])


# Funktion zeichnen
plt.plot(x, F1, 'g', label='$f(x)=e^{x}$')
plt.plot(x, F2, 'r', label='$g(x)=\\sin x$')


# Beschriftungen
achsen.set_xlabel('x', fontsize=12, labelpad=-23, x=1.03)
achsen.set_ylabel('y', fontsize=12, labelpad=-36, y=1.03, rotation=0)
plt.legend(loc='best')
plt.title('Funktionen $e^{x}$ und $\\sin x$', pad=30)

plt.show()
