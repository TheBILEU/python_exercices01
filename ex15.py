# O custo total da pintura de um muro é a soma de duas parcelas:
# 1. Custo do serviço por m² multiplicado pela área do muro.
# 2. Custo fixo com material de pintura.
# Um muro tem 12m de comprimento e 3m de altura. O material de pintura (galão de tinta, lixa, rolo, etc.) tem um custo fixo de R$ 100.
# Escreva um programa que leia o custo do serviço de pintura por m². Como saída, imprima o custo total da pintura do muro.


muroComprimento = 12
muroAltura = 3 
custoFixo = 100

custoM = float(input("Custo por serviço: "))
custoServico = (muroComprimento * muroAltura) * custoM 

custoTotal = custoFixo + custoServico

print(f"O valor total para a pintura do muro é de: R${custoTotal}")