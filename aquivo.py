
# 1. Escrever no arquivo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, Python!")

# 2. Ler o conteúdo do arquivo
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# 3. Adicionar mais conteúdo
with open("exemplo.txt", "a") as arquivo:
    arquivo.write("\nAprendendo a manipular arquivos em Python.")

# 4. Ler novamente para verificar a adição
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

