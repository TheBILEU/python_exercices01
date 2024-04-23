# Um cliente deseja sacar uma quantia no caixa eletrônico. Apenas as notas de R$100, R$ 50 e R$ 10 estão disponíveis na máquina.
# Escreva um programa que leia o valor que o cliente quer sacar. Como saída, determine e imprima quantas notas de cada tipo devem ser entregues ao cliente. Por simplicidade, considere que:
# 1. O cliente sempre pede uma quantia maior que zero e múltipla de dez;
# 2. O cliente tem saldo suficiente no banco; e
# 3. O caixa eletrônico tem uma quantidade INFINITA de notas de cada tipo

print("Notas disponíveis no caixa eletrônica: \nR$100\nR$50\nR$10\n")

clienteSaque = float(input("Quanto você deseja sacar?"))

notasDe100 = clienteSaque // 100
resto = clienteSaque % 100 
notasDe50 = resto // 50 
resto2 = resto % 50
notasDe10 = resto2 // 10

print(f"quantidade de notas de 100: {notasDe100:.0f}, quantidade de notas de 50: {notasDe50:.0f}, quantidade de notas de 10: {notasDe10:.0f}")
