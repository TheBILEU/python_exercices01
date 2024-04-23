# Seis amigos foram a um restaurante. A conta deu R$250, a ser repartida igualmente para cada um. Escreva um programa que imprima o valor que cada um tem que desembolsar. O resultado deve ser apresentado com, no máximo, duas casas decimais, indicativas dos centavos.

price = 250
slice = price / 6
print(f"O valor a ser desembolsado é de: R$ {slice:.2f}")