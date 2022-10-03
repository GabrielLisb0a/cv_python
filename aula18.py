from math import radians, sin, tan, cos
an = float(input("Digite o  valor de um ângulo qualquer:"))
seno = sin(radians(an))
print(f"Com o ângulo de {an} tem o seno de {seno:.2f}.")
tangente = tan(radians(an))
print(f"Com o ângulo de {an} tem a tangente de {tangente:.2f}.")
cosseno = cos(radians(an))
print(f"Com o ângulo de {an} tem o cosseno de {cosseno:.2f}.")