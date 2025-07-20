import math

def encontrar_soma_maxima_cruzando_meio(lista: list[int], inicio: int, meio: int, fim: int) -> int:
    """
    Encontra a soma máxima de uma subseção que OBRIGATORIAMENTE cruza o meio da lista.
    Complexidade: O(n)
    """
    soma_atual = 0
    soma_maxima_esquerda = -math.inf

    for i in range(meio, inicio - 1, -1):
        soma_atual += lista[i]
        if soma_atual > soma_maxima_esquerda:
            soma_maxima_esquerda = soma_atual

    soma_atual = 0
    soma_maxima_direita = -math.inf

    for i in range(meio + 1, fim + 1):
        soma_atual += lista[i]
        if soma_atual > soma_maxima_direita:
            soma_maxima_direita = soma_atual

    return soma_maxima_esquerda + soma_maxima_direita

def _encontrar_soma_maxima_recursivo(lista: list[int], inicio: int, fim: int) -> int:
    """Função auxiliar recursiva que implementa a lógica de Divisão e Conquista."""

    if inicio == fim:
        return lista[inicio]

    meio = (inicio + fim) // 2

    soma_maxima_esquerda = _encontrar_soma_maxima_recursivo(lista, inicio, meio)

    soma_maxima_direita = _encontrar_soma_maxima_recursivo(lista, meio + 1, fim)

    soma_maxima_cruzada = encontrar_soma_maxima_cruzando_meio(lista, inicio, meio, fim)

    return max(soma_maxima_esquerda, soma_maxima_direita, soma_maxima_cruzada)


def resolver_soma_maxima(lista: list[int]) -> int:
    """
    Função principal para resolver o Problema da Subseção de Soma Máxima
    usando o paradigma de Divisão e Conquista.

    Args:
        lista (list[int]): Uma lista de inteiros (positivos e/ou negativos).

    Returns:
        int: O valor da soma da subseção contígua de maior valor.
    """
    if not lista:
        return 0

    return _encontrar_soma_maxima_recursivo(lista, 0, len(lista) - 1)

if __name__ == "__main__":
    print("🧪 Iniciando testes do algoritmo de Soma Máxima de Subseção...")

    lista_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"\nLista: {lista_1}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_1)} (Esperado: 6)")
    print("-" * 40)

    lista_2 = [-10, -1, -5, -2, -8]
    print(f"Lista: {lista_2}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_2)} (Esperado: -1)")
    print("-" * 40)
    
    lista_3 = [1, 2, 3, 4, 5]
    print(f"Lista: {lista_3}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_3)} (Esperado: 15)")
    print("-" * 40)
    
    lista_4 = []
    print(f"Lista: {lista_4}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_4)} (Esperado: 0)")
    print("-" * 40)

    print("✅ Testes concluídos.")