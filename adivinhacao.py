print("Bem-vindo ao jogo da adivinhação")

numero_magico = 40
chute = -1
total_de_tentativas = 0
rodada = 1
pontos = 1000


nivel = int(input("Qual nível de dificuldade você deseja seguir? 1-fácil, 2-médio, 3-difícil \n"))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
elif(nivel == 3):
    total_de_tentativas = 3
else:
    print("Opção inválida")

for i in range(total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Qual é o seu chute?\n"))
    while True:
        if(chute < 0 or chute > 100):
            print("Você digitou um número inválido. Tente novamente.")
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute = int(input("Qual é o seu chute?\n"))
            continue
        else:
            break

    if (chute == numero_magico):
        print("Você acertou. Jogo finalizado!")
        print("Você ficou com " , pontos , "pontos")
        break
    elif (chute > numero_magico):
        pontos = pontos - abs(chute - numero_magico)
        print("Errou, chutou alto")
        if(rodada == total_de_tentativas):
            print("Jogo finalizado. Você perdeu!")
            print("Você ficou com " , pontos , "pontos")
    else:
        print("Errou, chutou baixo")
        pontos = pontos - abs(chute - numero_magico)
        if(rodada == total_de_tentativas):
            print("Jogo finalizado. Você perdeu!")
            print("Você ficou com " , pontos , "pontos")

    rodada = rodada + 1
