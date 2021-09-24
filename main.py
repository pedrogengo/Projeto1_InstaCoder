from utils import open_csv
from grafo import Grafo

conexoes = open_csv('conexoes.csv')
usuarios = open_csv('usuarios.csv')

instacoder = Grafo()
for usuario in usuarios:
    instacoder.adiciona(usuario[1])

for conexao in conexoes:
    instacoder.conecta(conexao[0], conexao[1], int(conexao[2]))

print(f"Seguidores da Helena: {instacoder.quantidade_seguidores('helena42')}")
print(f"Pessoas que a Helena segue: {instacoder.quantidade_seguindo('helena42')}")
print(f"Ordem dos stories da Helena: {instacoder.stories('helena42')}")
print(f"Top influences: {instacoder.top_influencers(5)}")
print(f"Caminho de Helena até Isadora: {instacoder.encontra_caminho('helena42', 'isadora45')}")