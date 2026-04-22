def hanoi(n, origem, destino, auxiliar, contador=[0]):
    #caso base: apenas 1 disco, move diretamente da origem para o destino
    if n == 1:
        contador[0] += 1
        print(f"Mover disco 1 de {origem} → {destino}")
        return

    #chamada recursiva 1: move os (n-1) discos do topo para o auxiliar
    hanoi(n - 1, origem, auxiliar, destino, contador)

    #move o disco maior (n) da origem para o destino
    contador[0] += 1
    print(f"Mover disco {n} de {origem} → {destino}")

    #chamada recursiva 2: move os (n-1) discos do auxiliar para o destino
    hanoi(n - 1, auxiliar, destino, origem, contador)


#teste com 3 discos
contador = [0]
hanoi(3, 'A', 'C', 'B', contador)
print(f"\nTotal de movimentos: {contador[0]}")

#análise de complexidade
#fórmula: número de movimentos = 2^n - 1
#fara n=3: 2^3 - 1 = 7 movimentos - ok
#
#demonstração:
#   seja T(n) o número de movimentos para n discos.
#   T(1) = 1                        
#   T(n) = 2 * T(n-1) + 1           
#
#expandindo:
#   T(n) = 2*(2*T(n-2)+1) + 1 = 4*T(n-2) + 3
#   T(n) = 2^k * T(n-k) + (2^k - 1)
#   quando k = n-1: T(n) = 2^(n-1)*T(1) + 2^(n-1) - 1
#                        = 2^(n-1) + 2^(n-1) - 1
#                        = 2^n - 1
#
#   como 2^n - 1 = O(2^n), a complexidade é O(2^n).