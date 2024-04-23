# A entrada possui dois números inteiros ‘E’ e ‘T’ (1 <= E <= 500) (1 <= T <= 100)
# representando espaço e tempo, respectivamente

# A saída consiste em uma única linha contendo a velocidade alcançada, sendo a
# velocidade calculada da seguinte forma: V = E/T. Sendo V a nossa velocidade desejada e é um número inteiro.

espaco = int(input("Digite o valor do espaço (1 <= E <= 500): "))
tempo = int(input("Digite o valor do tempo (1 <= T <= 100): "))

velocidade = espaco // tempo

print(f"A velocidade desejada para o Flash é de: {velocidade} m/s")

