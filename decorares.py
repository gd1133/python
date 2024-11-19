def tempo(repete):
    def mover():
        print('ola mundando de rota ')
        repete()
        print('vamos todos')

    return mover
@tempo
def retono():
    print('decoradores sao ')
retono()