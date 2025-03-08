def exibir_lista(lista):
    print('Lista de compras:')
    for i, item in enumerate(lista, 1):
        print(f'{i}. {item}')
    print()
    
def adicionar_item(lista):
    item = input('Digite o item que deseja adicionar: ') 
    lista.append(item)
    print(f"O item'{item}' foi adicionado a lista.")

def remover_item(lista):
    exibir_lista(lista)
    try:
        indice = int(input("Digite o número do item que deseja remover: "))
        item_removido = lista.pop(indice - 1)
        print(f"'{item_removido}' foi removido da lista.")
    except (ValueError, IndexError):
        print("Número inválido. Tente novamente.")

def menu():
    lista_de_compras = []
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Exibir lista")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_item(lista_de_compras)
        elif escolha == "2":
            remover_item(lista_de_compras)
        elif escolha == "3":
            exibir_lista(lista_de_compras)
        elif escolha == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu()
    
    