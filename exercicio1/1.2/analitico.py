import math
import matplotlib.pyplot as plt


def disponibilidade(n, k, p):
    total = 0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


lista_n = [1, 3, 5, 7, 9, 11]
lista_p = [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]

resultados = []
for n in lista_n:
    k_consulta = 1
    k_quorum = math.ceil(n / 2)
    k_atualizacao = n

    for p in lista_p:
        resultados.append([n, k_consulta, "consulta (k=1)", p, disponibilidade(n, k_consulta, p)])
        resultados.append([n, k_quorum, "quorum (k=n/2)", p, disponibilidade(n, k_quorum, p)])
        resultados.append([n, k_atualizacao, "atualizacao (k=n)", p, disponibilidade(n, k_atualizacao, p)])

print(f"{'n':>3} {'k':>3} {'caso':<20} {'p':>6} {'disponibilidade':>16}")
for n, k, caso, p, disp in resultados:
    print(f"{n:>3} {k:>3} {caso:<20} {p:>6} {disp:>16.5f}")

plt.figure()
for caso in ["consulta (k=1)", "quorum (k=n/2)", "atualizacao (k=n)"]:
    xs = [linha[3] for linha in resultados if linha[0] == 7 and linha[2] == caso]
    ys = [linha[4] for linha in resultados if linha[0] == 7 and linha[2] == caso]
    plt.plot(xs, ys, marker="o", label=caso)

plt.xlabel("p (chance de cada servidor estar no ar)")
plt.ylabel("disponibilidade do servico")
plt.title("Disponibilidade x p, com n = 7 servidores")
plt.legend()
plt.grid(True)
plt.savefig("exercicio1/1.2/resultados/grafico_disponibilidade_vs_p.png")

plt.figure()
for caso in ["consulta (k=1)", "quorum (k=n/2)", "atualizacao (k=n)"]:
    xs = [linha[0] for linha in resultados if linha[3] == 0.9 and linha[2] == caso]
    ys = [linha[4] for linha in resultados if linha[3] == 0.9 and linha[2] == caso]
    plt.plot(xs, ys, marker="o", label=caso)

plt.xlabel("n (numero de servidores)")
plt.ylabel("disponibilidade do servico")
plt.title("Disponibilidade x n, com p = 0.9")
plt.legend()
plt.grid(True)
plt.savefig("exercicio1/1.2/resultados/grafico_disponibilidade_vs_n.png")

print("graficos salvos em exercicio1/1.2/resultados/")
