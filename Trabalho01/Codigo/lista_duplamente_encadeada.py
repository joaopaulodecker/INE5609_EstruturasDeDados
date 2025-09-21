from no import No

class ListaDuplamenteEncadeada:
   
    """Implementa uma lista duplamente encadeada com um cursor."""
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self): 
        return self.__ultimo
    
    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def cursor(self):
        return self.__cursor

    def vazia(self):
        """(boolean) Verifica se a lista está vazia"""
        return self.__tamanho == 0

    def cheia(self):
        """(boolean) Verifica se a lista está cheia"""
        return False

    def posicaoDe(self, chave):
        """
        (int) Informa a posição sequencial do elemento com aquela chave, contado desde o primeiro.
        Retorna -1 se a chave não for encontrada.
        """
        if self.vazia():
            return -1
        
        posicao = 0
        atual = self.__primeiro
        while atual is not None:
            if atual.dado == chave:
                return posicao
            atual = atual.prox
            posicao += 1
        return -1
    
    def acessarAtual(self):
        """(devolve elemento) Retorna o dado do elemento na posição do cursor"""
        if self.__cursor is not None:
            return self.__cursor.dado
        return None

    def irParaPrimeiro(self):
        """(não devolve nada) Move o cursor para o primeiro elemento da lista"""
        self.__cursor = self.__primeiro

    def irParaUltimo(self):
        """(não devolve nada) Move o cursor para o último elemento da lista"""
        self.__cursor = self.__ultimo
    
    def avancarKPosicoes(self, k):
        """(não devolve nada) Avança o cursor K posições para frente"""
        if self.__cursor is None or k <= 0:
            return

        for _ in range(k):
            if self.__cursor.prox is None:
                break
            self.__cursor = self.__cursor.prox
            
    def retrocederKPosicoes(self, k):
        """(não devolve nada) Retrocede o cursor K posições para trás"""
        if self.__cursor is None or k <= 0:
            return

        for _ in range(k):
            if self.__cursor.ant is None:
                break
            self.__cursor = self.__cursor.ant

    def inserirComoPrimeiro(self, elemento):
        """(não devolve nada) Insere um novo elemento no início da lista"""
        novo_no = No(elemento)
        
        if self.vazia():
            self.__primeiro = novo_no
            self.__ultimo = novo_no
            self.__cursor = novo_no
        else:
            self.__primeiro.ant = novo_no
            novo_no.prox = self.__primeiro
            self.__primeiro = novo_no
        self.__tamanho += 1

    def inserirComoUltimo(self, elemento):
        """(não devolve nada) Insere um novo elemento no final da lista"""
        novo_no = No(elemento)
        
        if self.vazia():
            self.__primeiro = novo_no
            self.__ultimo = novo_no
            self.__cursor = novo_no
        else:
            self.__ultimo.prox = novo_no
            novo_no.ant = self.__ultimo
            self.__ultimo = novo_no
        self.__tamanho += 1

    def InserirAntesDoAtual(self, elemento):
        """(não devolve nada) Insere um novo elemento antes da posição do cursor"""
        if self.vazia():
            self.inserirComoPrimeiro(elemento)
            return
        
        if self.__cursor == self.__primeiro:
            self.inserirComoPrimeiro(elemento)
        else:
            novo_no = No(elemento)
            antigo_ant = self.__cursor.ant
            
            novo_no.prox = self.__cursor
            novo_no.ant = antigo_ant
            antigo_ant.prox = novo_no
            self.__cursor.ant = novo_no
            
            self.__tamanho += 1

    def InserirAposAtual(self, elemento):
        """(não devolve nada) Insere um novo elemento após a posição do cursor"""
        if self.vazia():
            self.inserirComoUltimo(elemento)
            return
            
        if self.__cursor == self.__ultimo:
            self.inserirComoUltimo(elemento)
        else:
            novo_no = No(elemento)
            antigo_prox = self.__cursor.prox
            
            novo_no.ant = self.__cursor
            novo_no.prox = antigo_prox
            antigo_prox.ant = novo_no
            self.__cursor.prox = novo_no
            
            self.__tamanho += 1

    def inserirNaPosicao(self, k, novo):
        """(não devolve nada) Insere um novo elemento na posição k"""
        if k < 1 or k > self.__tamanho + 1:
            print("Posição de inserção inválida.")
            return
        
        #move o cursor para a posição k e insere o novo nó antes dele
        self.irParaPrimeiro()
        self.avancarKPosicoes(k - 1)
        self.InserirAntesDoAtual(novo)
        
    def ExcluirPrim(self):
        """(não devolve nada) Exclui o primeiro elemento da lista"""
        if self.vazia():
            return
        
        if self.__primeiro == self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
            self.__cursor = None
        else:
            self.__primeiro = self.__primeiro.prox
            self.__primeiro.ant = None
        self.__tamanho -= 1

    def ExcluirUlt(self):
        """(não devolve nada) Exclui o último elemento da lista"""
        if self.vazia():
            return

        if self.__ultimo == self.__primeiro:
            self.__primeiro = None
            self.__ultimo = None
            self.__cursor = None
        else:
            self.__ultimo = self.__ultimo.ant
            self.__ultimo.prox = None
        self.__tamanho -= 1
        
    def ExcluirAtual(self):
        """(não devolve nada) Exclui o elemento na posição do cursor"""
        if self.vazia() or self.__cursor is None:
            return

        if self.__cursor == self.__primeiro and self.__cursor == self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
            self.__cursor = None
        elif self.__cursor == self.__primeiro:
            self.ExcluirPrim()
            self.__cursor = self.__primeiro
        elif self.__cursor == self.__ultimo:
            self.ExcluirUlt()
            self.__cursor = self.__ultimo
        else:
            proximo_node = self.__cursor.prox
            anterior_node = self.__cursor.ant
            
            anterior_node.prox = proximo_node
            proximo_node.ant = anterior_node
            
            self.__cursor = proximo_node
        self.__tamanho -= 1
    
    def Buscar(self, chave):
        """
        (boolean) Busca um elemento e move o cursor para ele se encontrado.
        """
        self.irParaPrimeiro()
        while self.__cursor is not None:
            if self.__cursor.dado == chave:
                return True
            self.avancarKPosicoes(1)
            
        return False
    
    def __str__(self):
        """ representação em string da lista"""
        if self.vazia():
            return "[]"
        
        elementos = []
        atual = self.__primeiro
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.prox
        
        cursor_data = self.acessarAtual() if self.acessarAtual() is not None else "N/A"
        return f"Lista: " + " <-> ".join(elementos) + f" (Cursor: {cursor_data})"

    def imprimir(self):
        """Imprime a lista"""
        print(self.__str__())