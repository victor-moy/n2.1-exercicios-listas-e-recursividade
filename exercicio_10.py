def encontrar_meio(cabeca):
    lento = cabeca
    rapido = cabeca.proximo  # rapido começa um à frente para cortar no meio certo
    while rapido and rapido.proximo:
        lento  = lento.proximo
        rapido = rapido.proximo.proximo
    return lento  # lento para no meio

def mesclar(l1, l2):
    # caso base
    if l1 is None: return l2
    if l2 is None: return l1

    if l1.dado <= l2.dado:
        l1.proximo = mesclar(l1.proximo, l2)
        return l1
    else:
        l2.proximo = mesclar(l2.proximo, l1)
        return l2

def merge_sort(cabeca):
    # caso base: lista vazia ou com 1 nó
    if cabeca is None or cabeca.proximo is None:
        return cabeca

    meio = encontrar_meio(cabeca)
    segunda_metade = meio.proximo
    meio.proximo = None  # corta a lista ao meio

    esquerda = merge_sort(cabeca)
    direita  = merge_sort(segunda_metade)

    return mesclar(esquerda, direita)

# Teste
l = ListaEncadeada()
for v in [5, 1, 4, 2, 8, 3]:
    l.inserir_final(v)
l.cabeca = merge_sort(l.cabeca)
l.imprimir()  # 1 → 2 → 3 → 4 → 5 → 8 → None