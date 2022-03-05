#Trabalho covid
#!!!!!Usando tabela temporaria pq arquivo ta muito grande heuheueh

def arquivoLista():
    lines = []
    with open("tabelatemp.txt") as file:
        for line in file: 
            line = line.strip() #or some other preprocessing
            lines.append(line) #storing everything in memory!
    return lines
        
print(arquivoLista())