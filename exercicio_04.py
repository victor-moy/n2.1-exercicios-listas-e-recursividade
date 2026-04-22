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

    def inverter(self):
        anterior = None
        atual = self.cabeca
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.cabeca = anterior


if __name__ == "__main__":
    lista = ListaEncadeada()
    for valor in [1, 2, 3, 4]:
        lista.inserir_final(valor)

    lista.imprimir()  # 1 → 2 → 3 → 4 → None
    lista.inverter()
    lista.imprimir()  # 4 → 3 → 2 → 1 → None
