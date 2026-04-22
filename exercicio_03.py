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

    def contar(self):
        contagem = 0
        atual = self.cabeca
        while atual:
            contagem += 1
            atual = atual.proximo
        return contagem


def contar_rec(no):
    if no is None:
        return 0
    return 1 + contar_rec(no.proximo)


if __name__ == "__main__":
    lista = ListaEncadeada()
    for valor in [10, 20, 30, 40]:
        lista.inserir_final(valor)

    print(lista.contar())            # 4
    print(contar_rec(lista.cabeca))  # 4
