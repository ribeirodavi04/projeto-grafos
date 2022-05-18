import numpy as np
from statistics import mode
from collections import Counter

texto = open('Grafo.txt')  # Lê um arquivo txt
grafo = texto.readlines()  # readLijnes tranforma cada linha em uma lista
linhasGrafo = len(grafo)  # retorna o indice maximo
# print(grafo)
# print(type(grafo))



#  A. Numero de vertices
def n_vertice():
    numeroVertice = (grafo[0])
    return numeroVertice
print("O numero de vertives é: ", n_vertice())


#  B. Numero de arestas
def n_arestas() :
    return len(grafo) - 1
print("O número de arestas é: ", n_arestas())


#  C. grau Maximo
def grau_maximo():
    nums = []
    #Adiciona todos os numeros separadamente num vetor
    for i in range(1, len(grafo)):
        nums.append(grafo[i][0:1])
        nums.append(grafo[i][2:3])


    #Pega o numero mais frequente no vetor
    return mode(nums)
print("Vétice com grau Maximo: ", grau_maximo())

def numsvet():
    nums = []
    # Adiciona todos os numeros separadamente num vetor
    for i in range(1, len(grafo)):
        nums.append(grafo[i][0:3])
    return  nums

print(numsvet())


def matriz_adj():
    ma = np.full((int(n_vertice()), int(n_vertice())), 0)
    a = []
    for i in range(int(n_arestas())):
        l = int(numsvet()[i][0:1])-1
        c = int(numsvet()[i][2:3])-1

        ma[l, c] = 1

    return ma

print("Matriz de Adjacencia: \n", matriz_adj())



#print(grafo[2])
''''
def grau_max():
    i = 1
    j = 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    grauVet = [4]
    grauMax = int

    for i in range(n_arestas()):  # definindo o vetor
        grauVet.append(0)


    for i  in range(5):
        for j in range (2):
            if j > 2:
                j = 0
                if grafo[1][0] == grafo[i][j]:
                    n1 = n1 + 1
                    grauVet.pop(0)
                    grauVet.insert(0, n1)
            else:
                if grafo[1][0] == grafo[i][j]:
                    n1 = n1 + 1
                    grauVet.pop(0)
                    grauVet.insert(0, n1)

            j = j + 2
        i = i + 1


    return(max(grauVet)) , grauVet


print("Grau Maximo: ", grau_max())
# comprar o 1 de 1 2 com todo o resto, e fazer isso com tudo







#  D. grau Maximo

#  E. Representação
n = 0
i = 0
j = 0
compVet = []
grafoTrans = [[0, 0], [0, 0], [0, 0], [0, 0]]

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(1, 5):
    for g in range(1,5):
        grafoTrans.insert(l-1, int(grafo[l][0]))

for i in range(0, 4):

    for j in range(0, 4):

        compVet =[i+1, j+1]
        if int (grafoTrans[0]):
            matriz[i][j] = 1


print("=====", grafoTrans)
print(grafo[2][0], grafo[2][2])
# print(compVet)
# print(type(grafo[0]))
print(matriz)
print(grafo[1])


'''



#  F. Informar a saída para busca em largura ou em profundidade

#  G. Informar se existem componentes conexas



