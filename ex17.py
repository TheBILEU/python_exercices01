# Michael comprou alguns litros de polpa de frutas, com o objetivo de doar dois terços a uma instituição de caridade e ficar com um terço. Escreva um programa que leia quantos litros foram comprados. Como saída, apresente a quantidade que ficará com Michael. Arredonde os valores com até 03 casas decimais de precisão.

litrosPolpas = float(input("Quantos litros de polpas de frutas foram compradas: "))
atual = litrosPolpas * 1 / 3
print(f"Michael ficará com {atual:.3f} litros de polpa")