# Escreva um programa que leia as seguintes informações:
# 1. Pontos de vida iniciais de um monstro antes de uma batalha de RPG (Role Playing Game).
# 2. Os valores sorteados no lançamento de dois dados de vinte faces (D1 e D2)
# 3. Como resultado, determine os pontos de vida RESTANTES do monstro após a aplicação do
# golpe. O dano causado pelo golpe corresponde à parte inteira do resultado da seguinte fórmula
# 𝑑𝑎𝑛𝑜 = ⌊raiz(5 × 𝐷1) + π(𝐷2/3)⌋
# Onde D1 e D2 são os valores sorteados pelos dados, na ordem informada.

vidaMonstro = int(input("Vida do monstro: "))
d1 = int(input("Resultado do primeiro dado lançado (de 1 á 20) = "))
d2 = int(input("Resultado do segundo dado lançado (de 1 á 20) = "))

dano = (5 * d1 **(1 / 2)) + (3.14 **(d2 / 3))
print(f"O dano causado ao monstro será: {dano:.0f} de dano")

vidaMonstroFinal = vidaMonstro - dano
print(f"O monstro está agora com {vidaMonstroFinal:.0f} de vida")