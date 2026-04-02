import re
def censurar_palabras(review, palabras):
    for palabra in palabras:
        palabra = palabra.strip()
        
        patron = re.compile(palabra, re.IGNORECASE)
        review = patron.sub("*"  * len(palabra), review)
    return review