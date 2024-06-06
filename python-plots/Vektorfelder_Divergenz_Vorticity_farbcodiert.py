# benoetigte Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# Definitionsbereich
f = np.linspace(-5, 5, 9)
g = np.linspace(-5, 5, 10)
h = np.linspace(-np.pi, np.pi, 20)
X_f, Y_f = np.meshgrid(f, f)
X_g, Y_g = np.meshgrid(g, g)
X_h, Y_h = np.meshgrid(h, h)

# Feldkomponenten definieren
F_x = X_f
F_y = Y_f
G_x = -Y_g
G_y = X_g
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
    sub.set_title('Vektorfeld $\\vec{ F }$')
    sub.set_xlabel('$x$')
    sub.set_xticks(np.linspace(-5, 5, 11))
    sub.set_ylabel('$y$')
    sub.set_yticks(np.linspace(-5, 5, 11))
for sub in subs2:
    sub.set_title('Vektorfeld $\\vec{ G }$')
    sub.set_xlabel('$x$')
    sub.set_xticks(np.linspace(-5, 5, 11))
    sub.set_ylabel('$y$')
    sub.set_yticks(np.linspace(-5, 5, 11))
for sub in subs3:
    sub.set_title('Vektorfeld $\\vec{ H }$')
    sub.set_xlabel('$-\\pi<x<\\pi$')
    sub.set_xticks(
        [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        ('$-\\pi$', '$-\\frac{\\pi}{2}$', '$0$', '$\\frac{\\pi}{2}$', '$\\pi$')
    )
    sub.set_ylabel('$-\\pi<x<\\pi$')
    sub.set_yticks(
        [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        ('$-\\pi$', '$-\\frac{\\pi}{2}$', '$0$', '$\\frac{\\pi}{2}$', '$\\pi$')
    )

# Subplots: Divergenz und Rotation/Vorticity einfaerben
farben = ['blue', 'green', 'red']
grenzen = [-10, -0.000001, 0.000001, 10]  # fuer 0 nicht elegant, aber effektiv
sub11.contourf(
    X_f, Y_f, Div_F, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)
sub12.contourf(
    X_g, Y_g, Div_G, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)
sub13.contourf(
    X_h, Y_h, Div_H, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)
sub21.contourf(
    X_f, Y_f, Vor_F, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)
sub22.contourf(
    X_g, Y_g, Vor_G, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)
sub23.contourf(
    X_h, Y_h, Vor_H, cmap=plt.cm.colors.ListedColormap(farben), levels=grenzen)

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

# Graphen speichern (ohne zusaetzlichen Rand) und anzeigen
fig1.savefig('Plot3', bbox_inches='tight', pad_inches=0)
fig2.savefig('Plot4', bbox_inches='tight', pad_inches=0)
plt.show()
