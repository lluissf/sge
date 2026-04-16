"""
    Sistema de Gestão de Estoque.
    Desenvolvido por: @lluissf
"""

from functions import listar_produtos, adicionar_produto, remover_produto, carregar_dados, salvar_dados
# Criando os produtos
produtos = carregar_dados()

# Criando o Menu.
while True:
    print(f"===================\n")
    print(f"1. Listar Produtos.\n")
    print(f"2. Adicionar Produto.\n")
    print(f"3. Remover Produto.\n")
    print(f"\n0. Sair do Programa.\n")
    print(f"===================\n")

    opcao = int(input("Insira o número: "))

    match opcao:
        case 0:
            break
        case 1:
            listar_produtos(produtos)
        case 2:
            adicionar_produto(produtos)
            salvar_dados(produtos)
        case 3:
            remover_produto(produtos)
            salvar_dados(produtos)
        case _:
            print("Opção inválida!")

print(f"Programa Encerrado.")