import json, os
def salvar_dados(lista_produtos):
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_produtos, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    if not os.path.exists("estoque.json"):
        return [] 
    
    with open("estoque.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def listar_produtos(produtos):
    print("-" * 50)
    print(f"{'ID':<4} | {'Nome':<15} | {'Preço':>10} | {'Qtd':>5}")
    print("-" * 50)
    
    for i in produtos:
        print(f"{i['id']:<4} | {i['nome']:<15} | R${i['preco']:>8.2f} | {i['quantidade']:>5}")
    print("-" * 50)

def adicionar_produto(produtos):
    """
    Adicionando um novo produto a lista..
    """
    try:
        id = max(produto["id"] for produto in produtos) + 1
    except:
        id = 1
    
    nome = input("Insira o nome do Produto: ")
    preco = float(input("Insira o preço do Produto: "))
    quantidade = int(input("Forneça a quantidade do Produto: "))
    novo_produto = {"id": id, "nome": nome, "preco": preco, "quantidade": quantidade }
    produtos.append(novo_produto)  

def remover_produto(produtos):
    """
    Remover produto da lista. (ID)
    """
    listar_produtos(produtos)
    id_produto = int(input("Insira o (ID) do Produto que deseja remover: "))
    encontrado = False
    for i in produtos:
        if i['id'] == id_produto:
            print(f"O Produto {i['nome']} foi removido com sucesso.")
            produtos.remove(i)
            encontrado = True
            break
    if not encontrado:
        print(f"Não encontrei o Produto com o ID: {id_produto}.") 
