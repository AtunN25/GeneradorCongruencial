import numpy as np
from scipy.stats import chisquare

# Parámetros del generador congruencial
a = 121
c = 553
m = 177
semilla = 23

# Generar la serie congruencial
def generar_serie(a, c, m, semilla):
    serie = []
    xi = semilla
    while xi not in serie:
        serie.append(xi)
        xi = (a * xi + c) % m
    return serie

# Calcular el periodo de vida
serie = generar_serie(a, c, m, semilla)
periodo_vida = len(serie)
print("Periodo de vida:", periodo_vida)

# Convertir la serie a una serie de números en (0, 1)
serie_normalizada = np.array(serie) / m

# Prueba de medias usando NumPy
media_observada = np.mean(serie_normalizada)
media_esperada = 0.5  # Media esperada para una distribución uniforme en (0,1)
print("Media observada:", media_observada)
print("Media esperada:", media_esperada)

# Prueba de varianza usando NumPy
varianza_observada = np.var(serie_normalizada)
varianza_esperada = 1 / 12  # Varianza esperada para una distribución uniforme en (0,1)
print("Varianza observada:", varianza_observada)
print("Varianza esperada:", varianza_esperada)

# Calcular el periodo de vida
serie = generar_serie(a, c, m, semilla)
periodo_vida = len(serie)
print("Periodo de vida:", periodo_vida)


# Prueba de uniformidad usando Chi-cuadrado
frecuencia_observada, _ = np.histogram(serie_normalizada, bins=10)
frecuencia_esperada = np.ones(10) * len(serie_normalizada) / 10
chi2, p_value = chisquare(frecuencia_observada, frecuencia_esperada)
print("Chi-cuadrado:", chi2)
print("P-valor:", p_value)
