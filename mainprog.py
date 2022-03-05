#Trabalho covid
#!!!!!Usando tabela temporaria pq arquivo ta muito grande heuheueh

def arquivoLista():
    lines = []
    with open("tabelatemp.txt",'r') as file:
        for line in file: 
            
            lines.append(line) #storing everything in memory!
    return lines
        
print(arquivoLista())

