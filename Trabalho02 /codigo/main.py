
from lista_estendida import ListaEncadeadaEstendida

if __name__ == "__main__":
    
    lista = ListaEncadeadaEstendida(capacidade_por_no=8)
    vals_no_1 = [3, 7, 9, 11, 18, 20, 21, 27]
    for v in vals_no_1:
        lista.insere_ordenado(v)
    vals_no_2 = [34, 35, 38, 42, 50, 51, 56]
    for v in vals_no_2:
        lista.insere_ordenado(v)
    
    print("\nLista ANTES de inserir 25")
    lista.imprimir_estrutura()
    
    print(f"\nInserindo o 25, isto força o split do nó 0")
    lista.insere_ordenado(25) 
    
    print(f"\nLista APÓS inserir 25")
    lista.imprimir_estrutura()
    

    print("\nTestes dos métodos")
    
    print(f"ListarDados(): {lista.listar_dados()}")
    print(f"Total: {lista.total()}") 
    
    print(f"Acessa posição 0: {lista.acessa_posicao(0)}")
    print(f"Acessa posição 7: {lista.acessa_posicao(7)}")
    print(f"Acessa posição 10: {lista.acessa_posicao(10)}")
    
    print(f"Busca 25: {lista.busca(25)}")
    print(f"Busca 99: {lista.busca(99)}")
    print(f"Busca 26: {lista.busca(26)}")

    print(f"Posição de 3:   {lista.posicao_de(3)}")
    print(f"Posição de 35: {lista.posicao_de(35)}")
    print(f"Posição de 99: {lista.posicao_de(99)}")

    print("\nTeste de Exclusão") 
    print(f"Excluindo pos 7")
    lista.exclui_da_posicao(7) 
    print(f"Após excluir pos 7:")
    lista.imprimir_estrutura()
    
    print(f"Excluindo pos 0")
    lista.exclui_da_posicao(0) 
    print(f"Após excluir pos 0:")
    lista.imprimir_estrutura()
    print(f"Total após exclusões: {lista.total()}")