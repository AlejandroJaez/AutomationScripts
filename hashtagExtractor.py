text = """
este es el titulo
esta es una entrada de 1 ejemplo de blog donde hablamos de #programación
pero tambien de #python
"""


def hashtags(text):
    return list(map(lambda word: word.lstrip('#'), filter(lambda word: word.startswith('#'), text.split())))


print(hashtags(text))
