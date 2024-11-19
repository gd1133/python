def gerador(limite):# gerador recebe parametro com limite
    valor = 0 #variaves valor recebe 0
    while valor < limite: # valor e menor q limite
        yield valor  # Pausa aqui e retorna o valor

        valor +=1 # valor recebe valor + 1
for nomero in gerador(9):
    print(nomero)        