# Grafo

```python
def  GrafoNaoDirigidosConexosAleatorio(grafo, vertice_do_grafo):
    fila = [] # fila da busca, afinal ela eh em largura! .append(elemento) -> adiciona elemento na fila ; .pop(0) -> proximo na fila
    # como os graus de entrada e saida de cada vertice sao iguais em uma busca em largura, chamamos ambos os valores de largura do vertice
    largura = {}
    l = 1 # contador de largura dos vertices na busca
    pai = {} # dicionario com os pais de cada vertice na arvore de busca em largura
    nivel = {} # nivel de cada vertice na arvore de busca em largura
    aresta = {} # classificacao das arestas na arvore de busca em largura do grafo

    # primeira insercao na fila eh o vertice do grafo escolhido arbitrariamente (passado como parametro dessa funcao)
    fila.append(vertice_do_grafo)
    largura[vertice_do_grafo] = l # a largura da raiz da arvore de busca em largura comeca por 1
    pai[vertice_do_grafo] = None # o primeiro vertice a entrar na fila (raiz da arvore de busca em largura) tem pai nulo (None object)
    nivel[vertice_do_grafo] = 1 # o nivel do primeiro vertice a entrar na fila a (raiz da arvore de busca em largura) eh 1

    # enquanto tivermos alguem na fila vamos continuar a busca. Grafos nao-conexos nao estao sendo tratados!
    while len(fila):
        vertice = fila.pop(0) # pega o proximo vertice da fila
        # colocando os vizinhos que ainda naum estavam na fila
        for vizinho in grafo.get(vertice):
            # testando se o vizinho jah foi visitado (se o get retornar None, significa que este vertice nunca entrou na fila)
            if not largura.get(vizinho): # se o vizinho ainda naum foi visitado...
                fila.append(vizinho) # ... colocamos na fila para visita-lo no seu devido momento
                l += 1 # atualizando o contador de largura
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1 # um vizinho estah sempre um nivel abaixo do pai
            # MOMENTO PARA VISITAR A ARESTA vertice -> vizinho
            # (descomente os codigos abaixo para ver a ordem em que as arestas sao visitadas e suas respectivas classificacoes)
            # print('%s -> %s:' % (str(vertice), str(vizinho)))
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                # print('aresta de arvore')
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                    # print('aresta irma')
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    # print('aresta primo')
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                    # print('aresta tia')
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    # print('aresta sobrinha')

    return largura, pai, aresta, nivel

largura, pai, aresta, nivel = GrafoNaoDirigidosConexosAleatorio(grafo, 'a') # mude aqui 'a' para "f" ou outra coisa
print("Largura: ",largura)
print()
print("Pai: ",pai)
print()
print("Arestas: ",aresta)
print()
print("nivel: ",nivel)
```
