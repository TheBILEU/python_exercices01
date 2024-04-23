# converta o tempo em segundos, que ele calculou, para horas, minutos e segundos.

# Será dado um número inteiro N (1 <= N <= 100000000) que representa o tempo do evento em segundos.
# Contém o tempo dado em segundos convertido para horas, minutos e segundos.

n = int(input("Digite quantos segundos se passou até então: "))

horas = n / 3600 
minutos = n / 60

print(f"Em {n} segundos, já se passou {horas:.3f} horas e {minutos:.3f} minutos")