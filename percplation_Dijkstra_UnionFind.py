#!/usr/bin/env python
# coding: utf-8

# In[67]:


import heapq #importation du package heapq qui permet d'affecter une valeur(poids à chaque noeud)
#import random #generer des valeurs aléatoires
import numpy as np #pour generer des valeurs aléatoires
class GraphPercolation: #Creation de la class 
    def __init__(self, graph): # initialisation
        self.graph = graph

    def dijkstra(self, source): # la fonction dijkstra va nous permettre d'avoir la distance minimale de chaque noeud par rapport à la source

        distances = {noeud: float('infinity') for noeud in self.graph} # tout noeud est à distance infini de son voisin
        distances[source] = 0 # la source est à distance 0 d' elle  meme
        #la variable distances nous permet de stocker toutes les distances des neouds 

        a_traiter = [(0, source)] # une liste de noeuds à traiter, initié à la source

        while a_traiter: # tant qu'il existe un noeud à traiter dans la liste
            
            dist_noeud, noeud = a_traiter.pop(0)#on récupère le dernier élément de la liste a_traiter
            print(dist_noeud, noeud)
            

            if dist_noeud > distances[noeud]: # si la distance du noeud actuel est superieur à la distance quelquonque, 
                print(distances)
                # continue
          
                continue

            for voisin, dist_voisin in self.graph[noeud].items(): #parcours des noeuds voisins
                distance = dist_noeud + dist_voisin
                print(dist_voisin)


                if distance < distances[voisin]:
                    distances[voisin] = distance
                    a_traiter.append((distance, voisin))

        return distances # on recupère toutes les distances minimales

    def percolation(self, source, threshold, probability):# la fonction percolation prende en argument la source du graph,
        #le seuil de percolation possible et la probabilité 
        if probability == 1: # il y'a jamais de percolation
            return False
        if probability ==0: #il y' a toujpurs percolation
            return True
        else : # si la probabilité est comprise entre 1 et 0, on entre dans la logique de percolation
            distances = self.dijkstra(source)
            noeuds_percoles = [noeud for noeud, distance in distances.items() if distance <= threshold]#creation d'une liste de noeud percolés
            # sachant qu'il faut que la disatance minimale du noeud en question par rapport à la source soit inférieur au seuil de percolation
    
            return np.random.choice([0,1]) <= probability and bool(noeuds_percoles)# puis on génère des nombre aléatoirs
            

# Exemple de graphe pondéré (représenté sous forme de dictionnaire)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Création d'une instance de la classe GraphPercolation
graph_percolation = GraphPercolation(graph)

# Nœud de départ
source = 'A'

# Seuil de percolation
percolation_threshold = 5

# Probabilité de percolation
percolation_probability = 0.2
 
# Appel de la fonction de percolation avec probabilité
result = graph_percolation.percolation(source, percolation_threshold, percolation_probability)
if result:
    print("Il y a percolation avec la probabilité de ",percolation_probability)
else:
    print("Il n'y a pas de percolation avec une probabilité : ",percolation_probability)


# In[ ]:





# In[60]:


graph


# In[11]:


class UnionFind():
    def __init__(self,n):
        self.parent = [i for i in range(n)] #chaque element est parent de lui meme
        self.rank = [0]*n # le rang de chaque element est initialement null
        
    def find(self,x):
        if self.parent[x] != x :
            #si x n'est pas egale à sa racine
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        #print(root_x)
        #print(root_y)
        
        if root_x != root_y : # cas de non connexe
            
            if self.rank[root_x] > self.rank[root_y]: 
                root_x = self.parent[root_y]
            elif self.rank[root_x] < self.rank[root_y]: 
                root_y = self.parent[root_x]
            else :
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class GraphPercolationUnionFind:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)
        self.union_find = UnionFind(self.num_nodes)

    def percolation(self, source, threshold):
        for node in self.graph:
            for voisin, largeur in self.graph[node].items():
                if largeur <= threshold:
                    self.union_find.union(int(node), int(voisin ))

        # Vérifier si le nœud de départ et le dernier nœud sont dans la même composante connexe
        return self.union_find.find(int(source)) == self.union_find.find(self.num_nodes - 1)

# Exemple de graphe pondéré (représenté sous forme de dictionnaire)

graph = {
    '0': {'1': 1, '2': 4},
    '1': {'0': 0, '2': 0, '3': 5},
    '2': {'0': 4, '1': 8, '3': 1},
    '3': {'1': 6, '2': 6}
}

# Création d'une instance de la classe GraphPercolationUnionFind
graph_percolation_union_find = GraphPercolationUnionFind(graph)

# Nœud de départ
source = '0'

#Seuil de percolation
percolation_threshold = 5

# Appel de la fonction de percolation avec Union-Find
result = graph_percolation_union_find.percolation(source, percolation_threshold)
print(f"Percolation result: {result}")


# In[ ]:




