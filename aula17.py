"""
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = (ca ** 2 + co ** 2) ** (1/2)
print(f"A hipotenusa deve medir {hi:.2f}")
"""

import math
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = math.hypot(co , ca)
print(f"A hipotenusa deve medir {hi:.2f}.")