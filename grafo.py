from utils import merge_sort


class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self._quantidade_seguidores = {}
        self.melhores_amigos = {}
        self.amigos = {}

    def adiciona(self, username):
        self.adjacencia[username] = {}
        self._quantidade_seguidores[username] = 0
        self.melhores_amigos[username] = []
        self.amigos[username] = []

    def conecta(self, origem, destino, peso=1):
        self.adjacencia[origem][destino] = peso
        if peso == 1:
            self.amigos[origem].append(destino)
        elif peso == 2:
            self.melhores_amigos[origem].append(destino)
        self._quantidade_seguidores[destino] += 1

    def quantidade_seguidores(self, username):
        return self._quantidade_seguidores[username]
    
    def quantidade_seguindo(self, username):
        return len(self.adjacencia[username])
    
    def top_influencers(self, k):
        return dict(merge_sort(list(self._quantidade_seguidores.items()), is_tuple=True)[-k:][::-1])
    
    def _ordena_stories(self, lista_amigos):
        return merge_sort(lista_amigos)

    def stories(self, username):
        melhores_amigos = self.melhores_amigos[username][:]
        amigos = self.amigos[username][:]
        self._ordena_stories(melhores_amigos)
        self._ordena_stories(amigos)
        return melhores_amigos + amigos
    
    def _busca_largura_exibe_caminho(self, origem, destino):
        fila = [origem]
        visitados = []
        predecessor = {origem: None}
        
        # enquanto tiver elementos na minha fila
        while len(fila) > 0:
            primeiro_elemento = fila[0]
            fila = fila[1:]
            visitados.append(primeiro_elemento)
            for adjacente in self.adjacencia[primeiro_elemento].keys():
                
                # se achou, monta o caminho
                if adjacente == destino:
                    pred = primeiro_elemento
                    caminho_invertido = [destino]
                    while pred is not None:
                        caminho_invertido.append(pred)
                        pred = predecessor[pred]
                    
                    caminho = ''
                    for no in caminho_invertido[::-1]:
                        caminho += f'{no} -> '
                    return caminho[:-3]
                
                if adjacente not in fila and adjacente not in visitados:
                    predecessor[adjacente] = primeiro_elemento
                    fila.append(adjacente)
        return False
    
    def encontra_caminho(self, origem, destino):
        caminho = self._busca_largura_exibe_caminho(origem, destino)
        if not caminho:
            return "Nao ha caminho."
        return caminho
