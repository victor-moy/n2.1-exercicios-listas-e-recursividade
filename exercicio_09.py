def tem_ciclo(cabeca):
    lento = cabeca
    rapido = cabeca
    while rapido and rapido.proximo:
        lento  = lento.proximo
        rapido = rapido.proximo.proximo
        if lento == rapido:
            return True
    return False

def inicio_ciclo(cabeca):
    lento = cabeca
    rapido = cabeca

    # Fase 1: detectar o encontro
    encontrou = False
    while rapido and rapido.proximo:
        lento  = lento.proximo
        rapido = rapido.proximo.proximo
        if lento == rapido:
            encontrou = True
            break

    if not encontrou:
        return None  # sem ciclo

    lento = cabeca
    while lento != rapido:
        lento  = lento.proximo
        rapido = rapido.proximo

    return lento  # nó onde o ciclo começa

no1 = No(1); no2 = No(2); no3 = No(3); no4 = No(4)
no1.proximo = no2; no2.proximo = no3
no3.proximo = no4; no4.proximo = no2  # ciclo em no2

print(tem_ciclo(no1))           # True
print(inicio_ciclo(no1).dado)   # 2