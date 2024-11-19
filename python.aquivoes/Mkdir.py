import os
import shutil
from pathlib import Path

#os.mkdir('novo-diratorio')
#print(__file__)
root_path = Path(__file__).parent

#os.mkdir(root_path / "")

#aquivo = open('novo.txt', 'w')
shutil.move(root_path / 'novo.txt', root_path / 'novo-diretorio'/ 'novo.txt')





#aquivo.close()
#pasta = open(root_path/"aquinovo.txt", 'w')

#pasta.close()

#os.rename(root_path/"aquinovo.txt", root_path/"alterado.txt")


#os.remove(root_path / "alterado.txt")