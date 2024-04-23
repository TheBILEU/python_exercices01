# Sejam A e B dois pontos sobre plano cartesiano. As coordenadas do ponto M, o ponto médio do segmento de reta formado por A e B
# Elabore um programa que leia, nesta ordem:
# 1. as coordenadas do ponto A
# 2. as coordenadas do ponto B
# Como saída, imprima o valor das coordenadas xM e yM 
# com até uma casa decimal de precisão

xA = int(input("Digite o primeiro valor das coordenadas do ponto A: "))
yA = int(input("Digite o segundo valor das coordenadas do ponto A: "))

xB = int(input("Digite o primeiro valor das coordenadas do ponto B: "))
yB = int(input("Digite o segundo valor das coordenadas do ponto B: "))

xM = (xB + xA) / 2
yM = (yB + yA) / 2

print(f"O ponto médio da coordenada xM é: {xM:.1f}")
print(f"O ponto médio da coordenada xY é: {yM:.1f}")