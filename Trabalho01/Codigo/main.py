from lista_duplamente_encadeada import ListaDuplamenteEncadeada

if __name__ == "__main__":
    
    # Teste 1: Inserções básicas e visualização
    print("\n--- Inserindo no início e no fim ---")
    lista1 = ListaDuplamenteEncadeada()
    lista1.inserirComoPrimeiro(10)
    lista1.inserirComoUltimo(20)
    lista1.inserirComoUltimo(30)
    print(f"Lista inicial: {lista1}")
    print(f"Tamanho: {lista1.tamanho}")

    # Teste 2: Inserir antes e depois do cursor
    print("\n--- Inserindo antes e depois do cursor ---")
    lista1.irParaPrimeiro()
    lista1.avancarKPosicoes(1) # move o cursor para '20'
    print(f"Cursor antes da inserção: {lista1.acessarAtual()}")
    lista1.InserirAntesDoAtual(15)
    lista1.InserirAposAtual(25)
    print(f"Lista após inserções: {lista1}")
    print(f"Tamanho: {lista1.tamanho}")

    # Teste 3: Exclusões
    print("\n--- Excluindo elementos ---")
    lista1.irParaPrimeiro()
    lista1.avancarKPosicoes(2) # move o cursor para '20'
    print(f"Cursor antes da exclusão: {lista1.acessarAtual()}")
    lista1.ExcluirAtual()
    print(f"Lista após excluir o elemento 20: {lista1}")
    print(f"Tamanho: {lista1.tamanho}")

    # Teste 4: Busca
    print("\n--- Buscando um elemento e movendo o cursor ---")
    encontrado = lista1.Buscar(25)
    print(f"Elemento 25 foi encontrado? {encontrado}")
    print(f"Cursor após a busca: {lista1.acessarAtual()}")
    print(f"Posição do elemento 25: {lista1.posicaoDe(25)}")

    # Teste 5: Casos de Borda (Excluir primeiro/último e lista vazia)
    print("\n--- Excluindo primeiro e último elementos ---")
    lista1.ExcluirPrim()
    print(f"Lista após excluir o primeiro: {lista1}")
    lista1.ExcluirUlt()
    print(f"Lista após excluir o último: {lista1}")
    print(f"Tamanho: {lista1.tamanho}")

    # Teste 6: Inserindo em posição específica
    print("\n--- Inserindo na posição 1 ---")
    lista1.inserirComoPrimeiro(5)
    lista1.inserirComoUltimo(10)
    print(f"Lista atual: {lista1}")
    lista1.inserirNaPosicao(1, 15)
    print(f"Lista após inserir 15 na posição 1: {lista1}")
    print(f"Tamanho: {lista1.tamanho}")
    
    lista1.imprimir()