

# Importando a biblioteca pandas
import pandas as pd
import matplotlib.pyplot as plt

# Criando uma tabela com os dados
lojas = {
'roupa':['beruda', 'camisa', 'calça', 'crinelo'],
'quantidade':[345, 345, 256, 351]
}
rb = pd.DataFrame(lojas)
print(rb)

tl = rb['quantidade'].max() 
print(f'maior valor: {tl}')

vl = rb[rb['quantidade'] == tl]['roupa'].values[0]
print(f'o mas vendido foi: {vl}')

plt.bar(rb['roupa'], rb['quantidade'])
plt.table('maior valor')
plt.xlabel('roupa')
plt.ylabel('quantidade')
plt.show()