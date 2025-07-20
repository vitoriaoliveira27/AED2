import math

def _explorar_a_partir_de(indice_atual: int, soma_atual: int, lista: list[int], soma_maxima_container: list[float]):
    """
    Função recursiva que explora todas as subseções que começam em um determinado ponto.
    Esta é a essência do "backtracking" para este problema.

    Args:
        indice_atual (int): O índice do elemento que estamos adicionando à subseção.
        soma_atual (int): A soma da subseção construída até o passo anterior.
        lista (list[int]): A lista original completa.
        soma_maxima_container (list[float]): Um container mutável para guardar a maior soma encontrada globalmente.
    """
    if indice_atual >= len(lista):
        return
    nova_soma_subsecao = soma_atual + lista[indice_atual]

    soma_maxima_container[0] = max(soma_maxima_container[0], nova_soma_subsecao)

    _explorar_a_partir_de(indice_atual + 1, nova_soma_subsecao, lista, soma_maxima_container)

def resolver_soma_maxima_backtracking(lista: list[int]) -> int:
    """
    Função principal para resolver o Problema da Subseção de Soma Máxima
    usando o paradigma de Backtracking (busca exaustiva recursiva).

    Args:
        lista (list[int]): Uma lista de inteiros.

    Returns:
        int: O valor da soma da subseção contígua de maior valor.
    """
    if not lista:
        return 0

    soma_maxima_container = [-math.inf]

    for i in range(len(lista)):
        _explorar_a_partir_de(i, 0, lista, soma_maxima_container)

    return int(soma_maxima_container[0])

if __name__ == "__main__":
    print("🧪 Iniciando testes do algoritmo de Soma Máxima com Backtracking...")
    lista_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"\nLista: {lista_1}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_1)} (Esperado: 6)")
    print("-" * 40)

    lista_2 = [-10, -1, -5, -2, -8]
    print(f"Lista: {lista_2}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_2)} (Esperado: -1)")
    print("-" * 40)
    
    lista_3 = [1, 2, 3, 4, 5]
    print(f"Lista: {lista_3}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_3)} (Esperado: 15)")
    print("-" * 40)
    
    lista_4 = []
    print(f"Lista: {lista_4}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_4)} (Esperado: 0)")
    print("-" * 40)

    print("✅ Testes concluídos.")