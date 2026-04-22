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
        while atual:
            print(atual.dado, end=" → ")
            atual = atual.proximo
        print("None")


def existe_rec(no, valor):
    #caso base 1: lista vazia ou chegou ao fim: valor não encontrado
    if no is None:
        return False
    #caso base 2: valor encontrado no nó atual
    if no.dado == valor:
        return True
    #chamada recursiva: verifica o restante da lista
    return existe_rec(no.proximo, valor)


def posicao_rec(no, valor, pos=0):
    #caso base 1: lista vazia ou chegou ao fim: valor não encontrado
    if no is None:
        return -1
    #caso base 2: valor encontrado, retorna o índice atual
    if no.dado == valor:
        return pos
    #chamada recursiva: avança para o próximo nó incrementando a posição
    return posicao_rec(no.proximo, valor, pos + 1)


def maior_rec(no):
    #caso base: lista com um único elemento, ele é o maior
    if no.proximo is None:
        return no.dado
    #chamada recursiva: compara o nó atual com o maior do restante
    maior_restante = maior_rec(no.proximo)
    return no.dado if no.dado > maior_restante else maior_restante


#testes
lista = ListaEncadeada()
for v in [10, 3, 87, 42, 5]:
    lista.inserir_final(v)

lista.imprimir()

print(f"existe_rec(cabeca, 42):  {existe_rec(lista.cabeca, 42)}")  
print(f"existe_rec(cabeca, 99):  {existe_rec(lista.cabeca, 99)}")
print(f"posicao_rec(cabeca, 87): {posicao_rec(lista.cabeca, 87)}")
print(f"posicao_rec(cabeca, 99): {posicao_rec(lista.cabeca, 99)}")  
print(f"maior_rec(cabeca):       {maior_rec(lista.cabeca)}")        