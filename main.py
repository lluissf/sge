"""
    Sistema de Gestão de Estoque.
    Desenvolvido por: @lluissf
"""
from functions import listar_produtos, adicionar_produto
# Criando os produtos
produtos = [
    {"id": 1, "nome": "Teclado Gamer", "preco": 100.29, "quantidade": 1},
    {"id": 2, "nome": "Mouse Gamer", "preco": 76, "quantidade": 2},
    {"id": 3, "nome": "Headset Gamer", "preco": 70.3, "quantidade": 10}
]

# Criando o Menu.
while True:
    print(f"===================\n")
    print(f"1. Listar Produtos.\n")
    print(f"2. Adicionar Produto.\n")
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

print(f"Programa Encerrado.")