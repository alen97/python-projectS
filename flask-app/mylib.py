###
### Librería personal con métodos útiles 
###


# Agarra lo que hay despues del ' ? ' en la URL, que serian los parámetros y devuelve el string tipeado
def buscar_parametros(url):
    result = url.find('?', 0, len(url))
    if(result != -1): # Si hay un ? en el texto
        return url[result+1:len(url)] # Retorna el string desde el index de '?' (lo omite) hasta el final de la URL. Después cambiar para que sólo llegue al final del string.
    else:
        return '-1'
