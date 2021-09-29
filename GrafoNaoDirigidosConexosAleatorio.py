grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

def  GrafoNaoDirigidosConexosAleatorio(grafo, vertice_do_grafo):
    fila = [] 
    largura = {}
    l = 1 
    pai = {} 
    nivel = {} 
    aresta = {} 

    
    fila.append(vertice_do_grafo)
    largura[vertice_do_grafo] = l 
    pai[vertice_do_grafo] = None 
    nivel[vertice_do_grafo] = 1
    
    while len(fila):
        vertice = fila.pop(0) 
      
        for vizinho in grafo.get(vertice):
           
            if not largura.get(vizinho): 
                fila.append(vizinho) 
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1 
            
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                   
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                  
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    

    return largura, pai, aresta, nivel

largura, pai, aresta, nivel = GrafoNaoDirigidosConexosAleatorio(grafo, 'a') # mude aqui 'a' para "f" ou outra coisa
print("Largura: ",largura)
print()
print("Pai: ",pai)
print()
print("Arestas: ",aresta)
print()
print("nivel: ",nivel)
