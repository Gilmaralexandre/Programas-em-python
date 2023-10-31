class Filme():
    def __init__(self, nome:str, ano:str, duração:int):
        self.nome = nome
        self.ano = int(ano)
        self.duração = duração
        
class Serie():
    def __init__(self, nome:str, ano:str, temporadas:int, episodios:int):
        self.nome = nome
        self.ano = int(ano)
        self.temporadas = temporadas
        self.episodios = episodios

Avengers = Filme("Vingadores","2017", 160)
print("nome: ",Avengers.nome)
print("ano: ",Avengers.ano)
print("duração",Avengers.duração)
print("*"*25)
Lupin = Serie("Lupin - ladrão de casaca","2017", 3, 30)
print("nome: ",Lupin.nome)
print("ano: ",Lupin.ano)
print("temporadas",Lupin.temporadas)
print("episódios",Lupin.episodios)
    


