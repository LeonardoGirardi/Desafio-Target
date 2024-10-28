def verifica_string(string: str, letra: str) -> str:
    
    quantidade = 0
    letra = letra.lower() 
    string = string.lower()  
    
    for char in string:  
        if char == letra:  
            quantidade += 1
    
    if quantidade == 0:
        return "Letra nao encontrada"
    else:
        return f"Resultado: {letra} foi encontrado {quantidade} vez/vezes"

palavra = "Programador"
print(verifica_string(palavra, 'a'))


