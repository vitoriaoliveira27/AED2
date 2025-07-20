import math

def encontrar_soma_maxima_cruzando_meio(lista: list[int], inicio: int, meio: int, fim: int) -> int:
    """
    Encontra a soma máxima de uma subseção que OBRIGATORIAMENTE cruza o meio da lista.
    Complexidade: O(n)
    """
    # --- Parte Esquerda (do meio para o início) ---
    soma_atual = 0
    soma_maxima_esquerda = -math.inf  # Inicia com "infinito negativo"

    # Itera do meio para trás, encontrando a maior soma possível
    for i in range(meio, inicio - 1, -1):
        soma_atual += lista[i]
        if soma_atual > soma_maxima_esquerda:
            soma_maxima_esquerda = soma_atual

    # --- Parte Direita (do meio+1 para o fim) ---
    soma_atual = 0
    soma_maxima_direita = -math.inf  # Inicia com "infinito negativo"

    # Itera do meio+1 para frente, encontrando a maior soma possível
    for i in range(meio + 1, fim + 1):
        soma_atual += lista[i]
        if soma_atual > soma_maxima_direita:
            soma_maxima_direita = soma_atual

    # A soma máxima cruzando o meio é a junção das duas melhores partes
    return soma_maxima_esquerda + soma_maxima_direita


def _encontrar_soma_maxima_recursivo(lista: list[int], inicio: int, fim: int) -> int:
    """Função auxiliar recursiva que implementa a lógica de Divisão e Conquista."""
    
    # --- PASSO DE CONQUISTA (CASO BASE) ---
    # Se há apenas um elemento, a soma máxima é o próprio elemento.
    if inicio == fim:
        return lista[inicio]

    # --- PASSO DE DIVISÃO ---
    # Encontra o ponto médio para dividir a lista
    meio = (inicio + fim) // 2

    # --- PASSO DE CONQUISTA (CHAMADAS RECURSIVAS) ---
    # 1. Encontra a soma máxima na subseção da esquerda.
    soma_maxima_esquerda = _encontrar_soma_maxima_recursivo(lista, inicio, meio)
    
    # 2. Encontra a soma máxima na subseção da direita.
    soma_maxima_direita = _encontrar_soma_maxima_recursivo(lista, meio + 1, fim)

    # 3. Encontra a soma máxima de uma subseção que cruza o meio.
    soma_maxima_cruzada = encontrar_soma_maxima_cruzando_meio(lista, inicio, meio, fim)

    # --- PASSO DE COMBINAÇÃO ---
    # O resultado final é o maior valor entre as três possibilidades.
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
        return 0 # Ou pode lançar uma exceção, dependendo do requisito.

    return _encontrar_soma_maxima_recursivo(lista, 0, len(lista) - 1)


# --- SEÇÃO PARA TESTE LOCAL ---
# O código dentro deste bloco só será executado quando o script
# for rodado diretamente.
if __name__ == "__main__":
    print("🧪 Iniciando testes do algoritmo de Soma Máxima de Subseção...")

    # Exemplo 1: O caso clássico
    lista_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Subseção de soma máxima é [4, -1, 2, 1], com soma 6
    print(f"\nLista: {lista_1}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_1)} (Esperado: 6)")
    print("-" * 40)

    # Exemplo 2: Todos os números são negativos
    lista_2 = [-10, -1, -5, -2, -8]
    # Subseção de soma máxima é [-1], com soma -1 (o menor prejuízo)
    print(f"Lista: {lista_2}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_2)} (Esperado: -1)")
    print("-" * 40)
    
    # Exemplo 3: Todos os números são positivos
    lista_3 = [1, 2, 3, 4, 5]
    # Subseção de soma máxima é a própria lista, com soma 15
    print(f"Lista: {lista_3}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_3)} (Esperado: 15)")
    print("-" * 40)
    
    # Exemplo 4: Lista vazia
    lista_4 = []
    print(f"Lista: {lista_4}")
    print(f"Soma máxima encontrada: {resolver_soma_maxima(lista_4)} (Esperado: 0)")
    print("-" * 40)

    print("✅ Testes concluídos.")