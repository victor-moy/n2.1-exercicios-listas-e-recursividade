class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_final(self, dado):
        novo = No(dado)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def imprimir(self):
        atual = self.cabeca
        resultado = ""
        while atual:
            resultado += str(atual.dado) + " → "
            atual = atual.proximo
        resultado += "None"
        print(resultado)


if __name__ == "__main__":
    lista = ListaEncadeada()
    for valor in [10, 20, 30]:
        lista.inserir_final(valor)
    lista.imprimir()  # 10 → 20 → 30 → None
