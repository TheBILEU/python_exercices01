# Escreva um programa que leia o valor de um raio r, inserido a partir do teclado. O programa deverá mostrar a área de um círculo com o raio r e o volume de uma esfera com raio r com duas casas decimais. Use a constante pi do módulo math em seus cálculos.
# V = 4/3 π r³
# A = π r²
import math

r = int(input("Valor do raio da esfera: "))
v = (4/3) * math.pi * (r**3) 
a = math.pi * (r**2)

print(f"O valor do volume é: {v:.2f}")
print(f"O valor da área é: {a:.2f}")
