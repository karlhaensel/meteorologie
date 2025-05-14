import numpy as np
from scipy.optimize import curve_fit


def windprofil_hellmann(v_1: float, h_1: float, h_2: float, alpha: float = 0.4) -> float:
    """
    Berechnung Windgeschwindigkeit v_2 auf Höhe h_2 nach Hellmann-Formel
    unter Nutzung von gemessener Windgeschwindigkeit v_1 auf Höhe h_1
    und gemäß Höhenkoeffizient alpha (abgeleitet von Rauigkeitshöhe z_0)
    typische Werte für alpha:
    Hohe See 0.1
    Flaches Land 0.16
    Wald 0.28
    Städtische Bebauung 0.4
    """
    return v_1 * (h_2/h_1)**alpha


def windprofil_logarithmisch(v_r: float, h_r: float, h: float, z_0: float) -> float:
    """
    Berechnung Windgeschwindigkeit v auf Höhe h nach logarithmischen Windprofil (Prandtl)
    unter Nutzung von gemessener Referenzgeschwindigkeit v_r auf Referenzhöhe h_r
    sowie Rauigkeitslänge z_0
    typische Werte für z_0:
    Offshore (v_10 = 5 m/s) 0.0001
    Vorstädte 0.5
    Wald 0.8
    Größere Städte mit hohen Gebäuden 1.0
    Großstädte mit hohen Gebäuden und Wolkenkratzern 1.6
    """
    return v_r * np.log(h/z_0)/np.log(h_r/z_0)


def windprofil_logarithmisch_fit(hs: tuple[float], vs: tuple[float]):
    """
    Fittet vertikales Windprofil als logarithmischen, um Rauigkeitslänge z_0 zu ermitteln,
    unter Nutzung gemessener Höhen hs in m 
    und gemessener Windgeschwindigkeiten vs in m/s auf diesen Höhen 
    gunter Nutzung Referenzwerte h_r und v_r (rster Wert der Datenreihe)
    """
    # Annahme
    h_r=hs[0]
    v_r=vs[0]
    # Funktion zum Fitten
    def profil_fit(h, z_0):
        return windprofil_logarithmisch(v_r, h_r, h, z_0)
    
    # Fitten
    parameter, _ = curve_fit(profil_fit, hs, vs, bounds=(0.0001, 2))
    
    return parameter[0] # z_0
    

if __name__ == '__main__':
    # Beispiel Hamburg (z_0 = 0.9 -> alpha = 0.34), Messung 4.4 m/s in h = 10 m
    Z_0 = 0.9
    ALPHA = 0.33
    for h in (50, 120, 180, 220, 250, 280):
        print(
            f'{h:3} m: {windprofil_logarithmisch(4.4, 10, h, Z_0):6.2f} m/s (logarithmisch), '
            f'{windprofil_hellmann(4.4, 10, h, ALPHA):6.2f} m/s (Hellmann)'
        )
    # Beispiel Stuttgart Umland (z_0 = 0.7), Messung 2.6 m/s in h = 7 m
    print(f'80 m Nabenhöhe: {windprofil_logarithmisch(2.6, 7, 80, 0.7):.2f} m/s')
    # Beispiel gemessenes Windprofil, Annahme logarithmisch
    hoehen = (10, 50, 120, 180, 220, 250, 280)
    windgeschwindigkeiten = (3.4, 4.5, 5.7, 6.4, 6.8, 7.2, 7.5)
    z_0 = windprofil_logarithmisch_fit(hoehen, windgeschwindigkeiten)
    print(f'{z_0=:.2f} m')
    print('Gegenprobe:')
    for h in (50, 120, 180, 220, 250, 280):
        print(
            f'{h:3} m: {windprofil_logarithmisch(3.4, 10, h, z_0):6.2f} m/s (logarithmisch)'
        )
