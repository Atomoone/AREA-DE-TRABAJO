# recommendation_system.py
# Sistema de recomendación básico generado con GitHub Copilot

import math

# Productos disponibles
productos = {
    "iPhone 15 Pro": [5, 3, 0, 0],
    "Samsung Galaxy S23": [4, 5, 0, 0],
    "Xiaomi 13": [0, 2, 5, 3],
    "Huawei P60": [0, 0, 4, 4],
}

# Perfil de un usuario (gustos simulados)
usuario = [5, 4, 0, 0]


def similitud_coseno(v1, v2):
    """Calcula la similitud del coseno entre dos vectores"""
    numerador = sum(a * b for a, b in zip(v1, v2))
    denominador = math.sqrt(sum([a**2 for a in v1])) * math.sqrt(sum([b**2 for b in v2]))
    if denominador == 0:
        return 0
    return numerador / denominador


# Calcular recomendaciones
recomendaciones = {}
for producto, vector in productos.items():
    score = similitud_coseno(usuario, vector)
    recomendaciones[producto] = score

# Ordenar recomendaciones de mayor a menor
ordenadas = sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)

print("=== Sistema de Recomendación Básico ===")
print("Recomendaciones para el usuario:\n")
for prod, score in ordenadas:
    print(f"{prod}: {score:.2f}")
