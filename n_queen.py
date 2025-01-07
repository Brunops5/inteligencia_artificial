# Tabu Search aplicado ao problema de N rainhas
# Bruno Augusto de Oliveira


import time
import random
from collections import deque

start_time = time.time()


n = 50  # quantidade da rainhas
max_it = 500
tam_tabu = 8  # lista tabu
null = None


solution = random.sample(range(1, n + 1), n)


def calc_fitness(solution):
    ataques = 0
    n = len(solution)
    dp = [0] * (2 * n)  # Diagonal positiva
    dn = [0] * (2 * n)  # Diagonal negativa

    for i in range(n):
        k_pos = i - solution[i] + (n - 1)
        k_neg = i + solution[i]

        ataques += dp[k_pos]
        dp[k_pos] += 1

        ataques += dn[k_neg]
        dn[k_neg] += 1

    return ataques


def gerar_vizinhos(solution):
    vizinhos = []
    n = len(solution)

    for i in range(n):
        for j in range(i + 1, n):
            vizinho = solution[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos


def busca_tabu(solution, max_int, tamanho_tabu):
    solucao_atual = solution[:]
    melhor_solucao = solution[:]
    melhor_fitness = calc_fitness(solution)

    lista_tabu = deque(maxlen=tamanho_tabu)

    for iteracao in range(max_int):
        vizinhos = gerar_vizinhos(solucao_atual)
        melhor_vizinho = null
        melhor_vizinho_fitness = float("inf")

        for vizinho in vizinhos:
            movimento = (solucao_atual.index(vizinho[0]), vizinho.index(vizinho[0]))
            if movimento not in lista_tabu or calc_fitness(vizinho) < melhor_fitness:
                fitness_vizinho = calc_fitness(vizinho)

                if fitness_vizinho < melhor_vizinho_fitness:
                    melhor_vizinho = vizinho
                    melhor_vizinho_fitness = fitness_vizinho

        if melhor_vizinho is null:
            continue

        solucao_atual = melhor_vizinho[:]

        if melhor_vizinho_fitness < melhor_fitness:
            melhor_solucao = melhor_vizinho[:]
            melhor_fitness = melhor_vizinho_fitness

        movimento = (
            solucao_atual.index(melhor_vizinho[0]),
            melhor_vizinho.index(melhor_vizinho[0]),
        )
        lista_tabu.append(movimento)

        if melhor_fitness == 0:
            break

    return melhor_fitness, melhor_solucao


melhor_fitness, melhor_solucao = busca_tabu(solution, max_it, tam_tabu)

execution_time = time.time() - start_time

print("Melhor Solução: ", melhor_solucao)
print("Melhor Fitness: ", melhor_fitness)
print("Tempo de execução: ", execution_time)
