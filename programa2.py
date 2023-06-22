print("Bem vindo ao jogo da adivinhação")

numero_secreto = 50

chute = int(input('Digite um número:\n'))

print('Voce digitou: ', chute)

if(numero_secreto == chute):
    print('Você acertou!')
elif(chute > numero_secreto):
    print('Você chutou alto')
else:
    print('Você chutou baixo')