def menu():
    while True:
        print("==== Sistema de Gerenciamento de Estoque ===")
        print("1. Cadastrar Produto")
        print("2. Consultar Produto")
        print("3. Atualizar Estoque")
        print("4. Rastrear Localização")
        print("5. Gerar Relatórios")
        print("6. Listar Todos os Produtos")
        print("7. Sair")
        opcao = input("Escolha uma opcção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produto()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "4":
            rastrear_localizacao()
        elif opcao == "5":
            gerar_relatorios()
        elif opcao == "6":
            listar_produtos()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

estoque = []

def cadastrar_produto():
    nome = input("Nome do Produto: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print(f"O produto '{nome}' já está cadastrado. Tente novamente com um nome diferente.\n")
            return
    categoria = input("Categoria do Produto: ").lower()
    quantidade = int(input("Quantidade em Estoque: "))
    preco = float(input("Preço do Produto: "))
    localizacao = input("Localização no Depósito: ").lower()
    
    produto = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "localizacao": localizacao,
    }
    estoque.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso.\n")

def consultar_produto():
    nome = input("Nome do produto a consultar: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print("Produto econtrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Quantidade em Estoque: {produto['quantidade']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print(f"Localização: {produto['localizacao']}\n")
            return
        print("Produto não encontrado.\n")

def atualizar_estoque():
    nome = input("Nome do produto para atualizar estoque: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            quantidade = int(input("Quantidade a adicionar (ou negativa para remover): "))
            produto["quantidade"] += quantidade
            print(f"Estoque atualizado: {produto['nome']} agora possui {produto['quantidade']} unidades.\n")
            return
        print("Produto não encontrado.\n")

def rastrear_localizacao():
    nome = input("Nome do produto para rastrear: ")  
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print(f"O produto '{produto['nome']}' está localizado em: {produto['localizacao']}\n")
            return
        print("Produto não encontrado.\n")

def gerar_relatorios():
    print("Relatório de Estoque:")
    estoque_baixo = [produto["nome"] for produto in estoque if produto["quantidade"] < 5]
    excesso_estoque = [produto["nome"] for produto in estoque if produto["quantidade"] > 100]

    if estoque_baixo:
        print("Produtos com estoque baixo:")
        for nome, quantidade in estoque_baixo:
            print(f"- {nome}: {quantidade} unidades")
    else:
        print("Nenhum produto com estoque baixo.")

    if excesso_estoque:
        print("Produtos com excesso de estoque:", ", ".join(excesso_estoque))
    else:
        print("Nenhum produto com excesso de estoque.")
        
    print("")

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.\n")
        return

    print("Produtos Cadastrados:")
    for produto in estoque:
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade em Estoque: {produto['quantidade']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Localização: {produto['localizacao']}\n")

menu()