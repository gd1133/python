def decoradores(fucao):
    def Envelope(*args, kwargs):
        fucao(*args, **kwargs)
        
    return Envelope
    

def Primir(nome, idade):  
    print(f'todos juntos! {nome} e {idade}')  

Primir('dine', 45)