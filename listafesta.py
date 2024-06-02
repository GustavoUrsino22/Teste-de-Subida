
qtd_pessoas = int(input("Número de pessoas na festa: "))

while (qtd_pessoas < 0 or qtd_pessoas >25):
    if qtd_pessoas < 0 :
        print("Valor inválido")
    elif qtd_pessoas > 25 :
        print("Número de Pessoas ultrapassou 25")
    qtd_pessoas = int(input("Número de pessoas na festa: "))

if qtd_pessoas == 0 :
        print("Nenhuma pessoa na lista")
else:
    lista_festa = []

    for pessoa in range(0,qtd_pessoas):
        nome_convidado = input(f"Digite o nome do convidado {pessoa+1}: ").upper()
        lista_festa.append(nome_convidado)

    
    if "João" not in lista_festa:
        if len(lista_festa) < 25:
            lista_festa.append("João")
            print("João foi adicionado à lista de convidados.")
        else:
            # Remover um convidado aleatório para fazer espaço para João
            import random
            indice_remover = random.randint(0, len(lista_festa) - 1)
            convidado_removido = lista_festa.pop(indice_remover)
            print(f"{convidado_removido} foi removido da lista para adicionar João.")
            lista_festa.append("João")
    
    print("Lista de convidados:")
    for convidado in lista_festa:
        print(convidado)