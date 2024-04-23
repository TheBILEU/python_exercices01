# Um grupo de três guerreiros derrotou um monstro que escondia 50 moedas de ouro. Cada um vai receber a mesma quantia de moedas e o restante será pago a um informante que indicou o caminho até o covil do monstro.

# Escreva um programa que determine:
# 1. Quantas moedas de ouro cada guerreiro receberá?
# 2. Quantas moedas de ouro serão pagas ao informante?

warriors = 3
gold = 50
slice = gold // warriors

print(f"Cada guerreiro receberá: {slice} moedas de ouro")
print(f"O informante receberá: {gold % warriors}")


