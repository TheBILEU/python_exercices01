#O custo total de pintura da fachada de um prédio depende de três informações:
#1. Altura da fachada, em metros
#2. Comprimento da fachada, em metros
#3. Valor do serviço da pintura por m²
#Escreva um programa que leia as informações acima, na ordem apresentada. Como saída, determine o custo total da pintura de uma fachada.

a = int(input("Digite uma altura desejável: "))
comprimento = int(input("Digite o comprimento: "))
valorServico = float(input("Valor do serviço da pintura: "))

custoTotal = a * comprimento * valorServico
print(f"Este é o custo total para a pintura: {custoTotal}")