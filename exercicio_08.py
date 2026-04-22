def remover_duplicatas(self):
    vistos = set()
    atual = self.cabeca
    anterior = None
    while atual:
        if atual.dado in vistos:
            anterior.proximo = atual.proximo  # pula o nó duplicado
        else:
            vistos.add(atual.dado)
            anterior = atual
        atual = atual.proximo

def remover_duplicatas_sem_aux(self):
    atual = self.cabeca
    while atual:
        corredor = atual
        while corredor.proximo:
            if corredor.proximo.dado == atual.dado:
                corredor.proximo = corredor.proximo.proximo  # remove duplicata
            else:
                corredor = corredor.proximo
        atual = atual.proximo