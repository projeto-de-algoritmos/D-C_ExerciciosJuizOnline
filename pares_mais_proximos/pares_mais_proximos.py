import math


pontos = []

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def menor(p1, p2):
    if p1 < p2:
        return p1
    return p2


def distancia_euclidiana(p1, p2):
    distancia = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distancia


def par_mair_proximo(p1, p2):
    if p1 == p2:
        return 9999.99 + 1.0
    elif p2 - p1 == 1:
        return distancia_euclidiana(pontos[p2], pontos[p1])
    else:
        esq = par_mair_proximo(p1, (p1 + p2) // 2)
        dir = par_mair_proximo((p1 + p2) // 2 + 1, p2)
        menor_distancia = menor(esq, dir)
        meio = (p1 + p2) // 2
        mediana = pontos[meio].x

        k = (p1 + p2) // 2 + 1
        while k <= p2 and mediana - pontos[k].x < menor_distancia:
            esq = distancia_euclidiana(pontos[k], pontos[meio])
            menor_distancia = menor(menor_distancia, esq)
            k += 1

        meio -= 1
        while meio >= p1 and mediana - pontos[meio].x < menor_distancia:
            k = (p1 + p2) // 2 + 1
            while k <= p2 and mediana - pontos[k].x < menor_distancia:
                esq = distancia_euclidiana(pontos[k], pontos[meio])
                menor_distancia = menor(menor_distancia, esq)
                k += 1
            meio -= 1

        return menor_distancia


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break

        pontos = []
        for _ in range(N):
            x, y = map(float, input().split())
            pontos.append(Ponto(x, y))

        pontos.sort(key=lambda ponto: (ponto.x, ponto.y))

        dist = par_mair_proximo(0, N - 1)

        if dist > 9999.99:
            print("INFINITY")
        else:
            print("{:.4f}".format(dist))
