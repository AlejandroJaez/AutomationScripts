text = """
este es el titulo
esta es una entrada de 1 ejemplo de blog donde hablamos de #programacion
pero tambien de #python
"""

def hashtags(text):
    return list(filter(lambda token: token.startswith('#'), text.split()))


print(hashtags(text))