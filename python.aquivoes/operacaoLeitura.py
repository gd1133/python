aquivo = open("python.aquivoes\lorem.txt", "r")

print(aquivo.readlines())
print(aquivo.read()) 
print(aquivo.readline())

#while len(linha := aquivo.readline()):
#  print(linha)
aquivo.close()
