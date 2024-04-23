# Sua tarefa é: sabendo que a nave de Skywalker está equipada com um dróide capaz de sondar todo o quadrante, diga quantas naves inimigas há.

# A entrada é composta por cinco inteiros, “A”, “B”, “C”, “D’ e “E”,

# A = o total de naves sondadas no quadrante
# B = o total de naves amigas detectadas a frente de Skywalker
# C =  o total de naves amigas a direita
# D = o total de naves amigas a esquerda
# E = o total de naves amigas atrás da nave de Skywalker

# A saída será composta por apenas um número inteiro, ou seja, o total de naves inimigas no quadrante em que Skywalker se encontra.

a = int(input("Total de naves sondadas no quadrante: "))
b = int(input("Total de naves amigas detectadas a frente de Skywalker: "))
c = int(input("Total de naves amigas a direita: "))
d = int(input("Total de naves amigas a esquerda: "))
e = int(input("Total de naves amigas atrás da nave de Skywalker: "))

navesAliadas = b + c + d + e 

print(f"Skywalker tem {navesAliadas} naves aliadas contra {a} naves do império")