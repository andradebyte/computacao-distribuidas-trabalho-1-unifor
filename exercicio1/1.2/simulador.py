import math
import random
import matplotlib.pyplot as plt


def disponibilidade_analitica(n, k, p):
    total = 0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


def simula(n, k, p, rodadas):
    sucessos = 0
    for _ in range(rodadas):
        disponiveis = 0
        for _ in range(n):
            sorteio = random.random()
            if sorteio <= p:
                disponiveis += 1
        if disponiveis >= k:
            sucessos += 1
    return sucessos / rodadas


lista_n = [1, 3, 5, 7, 9, 11]
lista_p = [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]
rodadas = 10000

random.seed(42)

resultados = []
for n in lista_n:
    k_consulta = 1
    k_quorum = math.ceil(n / 2)
    k_atualizacao = n

    for p in lista_p:
        for caso, k in [
            ("consulta (k=1)", k_consulta),
            ("quorum (k=n/2)", k_quorum),
            ("atualizacao (k=n)", k_atualizacao),
        ]:
            analitico = disponibilidade_analitica(n, k, p)
            experimental = simula(n, k, p, rodadas)
            erro = abs(analitico - experimental)
            resultados.append([n, k, caso, p, rodadas, analitico, experimental, erro])

print(f"{'n':>3} {'k':>3} {'caso':<20} {'p':>6} {'analitico':>11} {'experimental':>13} {'erro':>9}")
for n, k, caso, p, rodadas_, analitico, experimental, erro in resultados:
    print(f"{n:>3} {k:>3} {caso:<20} {p:>6} {analitico:>11.5f} {experimental:>13.5f} {erro:>9.5f}")

erros = [linha[7] for linha in resultados]
print(f"\nerro medio: {sum(erros) / len(erros):.5f}")
print(f"erro maximo: {max(erros):.5f}")

plt.figure()
cores = {"consulta (k=1)": "tab:blue", "quorum (k=n/2)": "tab:green", "atualizacao (k=n)": "tab:orange"}
for caso in cores:
    xs = [linha[3] for linha in resultados if linha[0] == 7 and linha[2] == caso]
    y_analitico = [linha[5] for linha in resultados if linha[0] == 7 and linha[2] == caso]
    y_experimental = [linha[6] for linha in resultados if linha[0] == 7 and linha[2] == caso]
    plt.plot(xs, y_analitico, marker="o", color=cores[caso], label=f"{caso} - analitico")
    plt.plot(xs, y_experimental, marker="x", linestyle="--", color=cores[caso], label=f"{caso} - simulado")

plt.xlabel("p")
plt.ylabel("disponibilidade")
plt.title(f"Analitico x simulado (n=7, {rodadas} rodadas por ponto)")
plt.legend(fontsize=8)
plt.grid(True)
plt.savefig("exercicio1/1.2/resultados/grafico_comparacao_n7.png")

print("grafico salvo em exercicio1/1.2/resultados/grafico_comparacao_n7.png")
