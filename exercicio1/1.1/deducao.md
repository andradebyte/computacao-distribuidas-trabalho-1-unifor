# Exercicio 1.1 - deducao da formula

Ideia: tenho n servidores, cada um ta disponivel (independente dos outros)
com probabilidade p. O servico so funciona se pelo menos k desses n
estiverem disponiveis no mesmo instante.

Isso e basicamente uma distribuicao binomial: cada servidor e um "sucesso"
(disponivel) com chance p, "falha" com chance (1-p). Quero a chance de ter
k ou mais sucessos em n tentativas.

Probabilidade de exatamente i servidores disponiveis:

    P(X = i) = C(n,i) * p^i * (1-p)^(n-i)

(C(n,i) e a combinacao "n escolhe i")

Como quero "pelo menos k", somo de i=k ate i=n:

    A(n,k,p) = SOMA (i=k ate n) de C(n,i) * p^i * (1-p)^(n-i)

Essa e a formula geral.

## Caso k = 1 (so precisa de 1 servidor no ar, tipo uma leitura)

Mais facil pensar no complemento: o servico so falha se TODOS os
servidores estiverem fora do ar, ou seja (1-p)^n. Entao:

    A(n,1,p) = 1 - (1-p)^n

Faz sentido: quanto mais servidor eu adiciono, mais dificil todo mundo
cair ao mesmo tempo, entao disponibilidade sobe com n.

## Caso k = n (precisa de TODOS, tipo escrita/atualizacao que exige todo mundo sincronizado)

Aqui e direto, os n servidores tem que estar disponiveis ao mesmo tempo,
e como sao independentes so multiplico:

    A(n,n,p) = p^n

Esse caso e o oposto: quanto mais servidor eu boto, MAIS dificil ficar
disponivel (basta um cair e already era), entao disponibilidade cai com n.

## Caso do meio, k = maioria (quorum, tipo n/2 arredondado pra cima)

Nao tem forma fechada bonitinha, e o mesmo somatorio binomial la de cima
mas com k = ceil(n/2). Da pra calcular, so nao simplifica em algo tipo
"1 - alguma coisa".

Resumo pra lembrar:
- k=1 -> disponibilidade sobe com n (bom pra leitura/consulta)
- k=n -> disponibilidade cai com n (ruim, exige tudo no ar)
- k=quorum -> fica no meio, depende de p ser > 0.5 ou < 0.5
