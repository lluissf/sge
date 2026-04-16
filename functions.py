def listar_produtos(produtos):
    """
    Estamos listando somente o nome do produto por enquanto.
    """
    for i in produtos:
        print(f"{i["nome"]}")
