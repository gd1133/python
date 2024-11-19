def decoradores(fucao):
    def Envelope(*args, kwargs):
        fucao(*args, **kwargs)
        return fucao()
    return Envelope
    

def Primir(nome, idade):  
    print(f'todos juntos! {nome} e {idade}')  
pri = Primir('dine', 23)

