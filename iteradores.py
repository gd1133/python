class Cotado:
    def __init__(self, conta):
        self.conta = conta
        self.valor = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.valor < self.conta:
            atua = self.valor
            self.valor +=1
            return atua
        else:
            raise StopIteration
        # Usando o iterador
for numero in Cotado(5):
    print(numero)



     
