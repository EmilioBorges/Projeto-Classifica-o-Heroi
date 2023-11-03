nome = ["Emilio", 0]

nivel = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]

while True:
    nome[0] = str(input("Digite o nome do Herói: "))
    nome[1] = int(input('Digite a pontuacão do Herói:')) 
    

    if nome[1] <= 1000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[0]}')
        break
    elif nome[1] >= 1001 and nome[1] <= 2000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[1]}')
        break
    elif nome[1] >= 2001 and nome[1] <= 5000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[3]}')
        break
    elif nome[1] >= 5001 and nome[1] <= 7000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[4]}')
        break
    elif nome[1] >= 7001 and nome[1] <= 8000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[5]}')
        break
    elif nome[1] >= 8001 and nome[1] <= 9000:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[6]}')
        break
    elif nome[1] >= 10001:
        print(f'O Herói de nome {nome[0]} está no nível de {nivel[7]}')
        break
else:
    print("Jogo Finalizado")

        
               
