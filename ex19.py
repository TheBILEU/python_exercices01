# Elabore um programa que leia as coordenadas
# e imprima no console o valor da distância entre eles com até três casas
# decimais de precisão.

xA = int(input("Digite o primeiro valor das coordenadas do ponto A: "))
yA = int(input("Digite o segundo valor das coordenadas do ponto A: "))

xB = int(input("Digite o primeiro valor das coordenadas do ponto B: "))
yB = int(input("Digite o segundo valor das coordenadas do ponto B: "))

dAB = (((xB - xA)**2) + ((yB - yA)**2)) ** (1 / 2)

print(f"A distância entre os pontos A e B é de: {dAB:.3f}")
