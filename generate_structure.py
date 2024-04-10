def string_to_list(text):
    # Elimino caracteres indeseados y saltos de linea del String
    characters = (",","'")
    for character in characters:
        text = text.replace(character,'')
    text = text.replace("\n"," ")
    # Genero una lista separando los elementos por los espacios
    names = text.split(' ')
    # Si queda un "" como elemento (por haber dos espacios consecutivos) los elimino
    for element in names:
        if element == '':
            names.remove(element)
    return names

# Creacion del diccionario
def create_structure(names,goals,goals_avoided,assists):
    players = {}
    for n,g,ga,a in zip(names,goals,goals_avoided,assists):
        players[n]=[g,ga,a]
    return players