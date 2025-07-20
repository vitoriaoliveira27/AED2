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
    # Condição de parada: se o índice está fora da lista, não há mais como explorar.
    if indice_atual >= len(lista):
        return

    # --- Ação no nó atual ---
    # Adiciona o elemento atual à soma da subseção que estamos construindo.
    nova_soma_subsecao = soma_atual + lista[indice_atual]

    # Compara a soma desta nova subseção com a máxima global já encontrada.
    soma_maxima_container[0] = max(soma_maxima_container[0], nova_soma_subsecao)

    # --- Passo recursivo (Explorar) ---
    # Continua a exploração, estendendo a subseção atual com o próximo elemento.
    _explorar_a_partir_de(indice_atual + 1, nova_soma_subsecao, lista, soma_maxima_container)
    
    # Ao retornar da chamada recursiva, o "backtrack" acontece naturalmente, pois a
    # pilha de chamadas volta para a função `resolver_soma_maxima_backtracking`,
    # que então iniciará uma nova exploração a partir do próximo ponto de partida.

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

    # Usamos um container mutável (lista) para que a variável possa ser
    # modificada dentro das funções recursivas por referência.
    # Iniciamos com -infinito para lidar corretamente com listas de negativos.
    soma_maxima_container = [-math.inf]

    # --- Ponto de Partida para o Backtracking ---
    # Este loop define cada ponto de partida possível para uma subseção.
    # Para cada `i`, iniciamos uma nova "árvore de exploração".
    for i in range(len(lista)):
        # A exploração começa no índice `i`. A soma inicial é 0, pois
        # a subseção ainda não foi formada. A função _explorar_a_partir_de
        # irá formar a primeira subseção [lista[i]] e depois estendê-la.
        _explorar_a_partir_de(i, 0, lista, soma_maxima_container)

    return int(soma_maxima_container[0])


# --- SEÇÃO PARA TESTE LOCAL ---
if __name__ == "__main__":
    print("🧪 Iniciando testes do algoritmo de Soma Máxima com Backtracking...")

    # Exemplo 1: O caso clássico
    lista_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Subseção de soma máxima é [4, -1, 2, 1], com soma 6
    print(f"\nLista: {lista_1}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_1)} (Esperado: 6)")
    print("-" * 40)

    # Exemplo 2: Todos os números são negativos
    lista_2 = [-10, -1, -5, -2, -8]
    # Subseção de soma máxima é [-1], com soma -1
    print(f"Lista: {lista_2}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_2)} (Esperado: -1)")
    print("-" * 40)
    
    # Exemplo 3: Todos os números são positivos
    lista_3 = [1, 2, 3, 4, 5]
    # Subseção de soma máxima é a própria lista, com soma 15
    print(f"Lista: {lista_3}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_3)} (Esperado: 15)")
    print("-" * 40)
    
    # Exemplo 4: Lista vazia
    lista_4 = []
    print(f"Lista: {lista_4}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima_backtracking(lista_4)} (Esperado: 0)")
    print("-" * 40)

    print("✅ Testes concluídos.")