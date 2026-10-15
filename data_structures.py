### listas ###
# uma lista é ordenada
# uma lista é mutável

lista = []  # declarando uma lista vazia

lista = [1, "Python", 2]  # atribuindo valores à lista

lista[0]  # acessando um valor da lista pelo seu índice

lista[0] = (
    "JavaScript is better"  # alterando um valor de um elemento pelo seu índice (index)
)

lista.append("Java")  # adicionando um novo elemento ao final da lista (list)

lista.insert(
    1, "C#"
)  # adicionando um elemento em um índice específico. Caso haja um elemento nesse índice, ele será empurrado para frente

favorite_movies = ["Batman", "Coringa", "Mud runner", "jonh wick"]

### tupla ###
# uma tupla é ordenada
# uma tupla é imutável (seus valores não podem ser modificados)

tupla = 123, 345, "Hello my friend"  # declarando uma tupla

tl = ("hello my friend", "leave me her", "you understand, right?"), [1, 2, 3, 4]

data_movies = ('01/05/2026', '03/07/2026', '13/01/2026', '15/05/2026')

### dicionário ###
# um dicionário não é ordenado
# um dicionário é mutável
# 'chave':'value: str' or value: int

ages = {'lucas':18, 'isa':18, 'emilly':18,'bianca':22, 'xavier':18, 'gaby':18, 'rayssa':18} # declarando um dicionário (key:value)

ages['isa'] = 19 # acesando um valor pela chave

movies = {
  'John Wick':2023,
  'Jumper':2008,
  'SkyFall':2005,
  'Sexta Feira 13':2013
}