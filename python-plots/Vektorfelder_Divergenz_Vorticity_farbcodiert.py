# benoetigte Bibliothek importieren
import numpy as np  # fuer Zahlenmengen sowie ggf. math. Funktionen
import matplotlib.pyplot as plt  # fuer das Zeichnen von Graphen
from matplotlib.colors import ListedColormap  # fuer das Einfaerben
from matplotlib.patches import Patch  # fuer die Legenden

# Definitionsbereich
f = np.linspace(-5, 5, 9)
g = np.linspace(-5, 5, 10)
h = np.linspace(-np.pi, np.pi, 20)
X_f, Y_f = np.meshgrid(f, f)
X_g, Y_g = np.meshgrid(g, g)
X_h, Y_h = np.meshgrid(h, h)

# Feldkomponenten definieren
# Vektorfeld F(x,y) mit F_x=x; F_y=y
F_x = X_f
F_y = Y_f
# Vektorfeld G(x,y) mit F_x=-y; F_y=x
G_x = -Y_g
G_y = X_g
# Vektorfeld H(x,y) mit H_x = -sin(x) + cos(y); H_y = sin(x) + cox(y)
H_x = -np.sin(X_h) + np.cos(Y_h)
H_y = np.sin(X_h) + np.cos(Y_h)

# Divergenzen (Angabe von 0x und 0y fuer korrektes Einfaerben noetig)
Div_F = 0*X_f + 0*Y_f + 2
Div_G = 0*X_g + 0*Y_g + 0
Div_H = (-1)*np.cos(X_h) - np.sin(Y_h)

# Vorticity (Angabe von 0x und 0y fuer korrektes Einfaerben noetig)
Vor_F = 0*X_f + 0*Y_f + 0
Vor_G = 0*X_g + 0*Y_g + 2
Vor_H = np.cos(X_h) + np.sin(Y_h)

# Figuren samt Subplots erstellen und beschriften
fig1, (sub11, sub12, sub13) = plt.subplots(1, 3, figsize=(15, 5))
fig1.suptitle('DIVERGENZ')
fig2, (sub21, sub22, sub23) = plt.subplots(1, 3, figsize=(15, 5))
fig2.suptitle('VORTICITY')
subs1 = [sub11, sub21]
subs2 = [sub12, sub22]
subs3 = [sub13, sub23]
for sub in subs1:
    sub.set_title(r'Vektorfeld $\vec{ F }$')
    sub.set_xlabel(r'$x$')
    sub.set_xticks(np.linspace(-5, 5, 11))
    sub.set_ylabel(r'$y$')
    sub.set_yticks(np.linspace(-5, 5, 11))
for sub in subs2:
    sub.set_title(r'Vektorfeld $\vec{ G }$')
    sub.set_xlabel(r'$x$')
    sub.set_xticks(np.linspace(-5, 5, 11))
    sub.set_ylabel(r'$y$')
    sub.set_yticks(np.linspace(-5, 5, 11))
for sub in subs3:
    sub.set_title(r'Vektorfeld $\vec{ H }$')
    sub.set_xlabel(r'$-\pi<x<\pi$')
    sub.set_xticks(
        [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        (r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$')
    )
    sub.set_ylabel(r'$-\pi<x<\pi$')
    sub.set_yticks(
        [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        (r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$')
    )

# Subplots: Divergenz und Rotation/Vorticity einfaerben
farben = ['blue', 'green', 'red']
grenzen = [-10, -0.000001, 0.000001, 10]  # fuer 0 nicht elegant, aber effektiv
subs = [sub11, sub12, sub13, sub21, sub22, sub23]
xs = [X_f, X_g, X_h, X_f, X_g, X_h]
ys = [Y_f, Y_g, Y_h, Y_f, Y_g, Y_h]
vars = [Div_F, Div_G, Div_H, Vor_F, Vor_G, Vor_H]
for sub, x, y, var in zip(subs, xs, ys, vars):
    sub.contourf(x, y, var, cmap=ListedColormap(farben), levels=grenzen)

# Subplots: Vektorfelder zeichnen
for sub in subs1:
    sub.quiver(X_f, Y_f, F_x, F_y)
for sub in subs2:
    sub.quiver(X_g, Y_g, G_x, G_y)
for sub in subs3:
    sub.quiver(X_h, Y_h, H_x, H_y)

# horizontale Abstaende subplots einstellen
fig1.subplots_adjust(hspace=0.2)
fig2.subplots_adjust(hspace=0.2)

# Legenden hinzufügen
legend_elements_fig1 = [Patch(facecolor='blue', label='Konvergenz'),
                        Patch(facecolor='green', label='neutral'),
                        Patch(facecolor='red', label='Divergenz')]
fig1.legend(handles=legend_elements_fig1, loc='upper right')

legend_elements_fig2 = [Patch(facecolor='blue', label='antizyklonal'),
                        Patch(facecolor='green', label='neutral'),
                        Patch(facecolor='red', label='zyklonal')]
fig2.legend(handles=legend_elements_fig2, loc='upper right')

# Graphen ggf. speichern (ohne zusaetzlichen Rand) und anzeigen
# fig1.savefig('Plot_Divergenz', bbox_inches='tight', pad_inches=0)
# fig2.savefig('Plot_Vorticity', bbox_inches='tight', pad_inches=0)
plt.show()
