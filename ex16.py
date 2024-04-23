# Desenvolva um programa que lê um número inteiro de quatro dígitos a partir do teclado e exibe
# a soma dos dígitos do número. Por exemplo, se o usuário digitar 3141, o programa deve exibir
# o resultado da soma 3 + 1 + 4 + 1 = 9.

numero = input("Digite um número inteiro de quatro dígitos: ")
soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])
print(f"A soma da sequência {numero} é {soma}")