#Trabalho covid
#!!!!!Usando tabela temporaria pq arquivo ta muito grande heuheueh

def arvivoLista():
    list = []
    arquivo = open('tabelatemp.txt', 'r')
    for line in arquivo:
        list.append(line)