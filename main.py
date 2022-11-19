from etapa1 import RaceCommitCheckout
from etapa2 import Interpreter
from etapa3 import Fix
from etapa4 import FixCommit
import sys
import os

cwd = os.getcwd()

caminho_ospedado = cwd.replace('/pyrace', '')

# logMaven = open(cwd + "/etapa1/logMaven.txt", "a")



# pomPath = sys.argv[1] #"/Users/felipeveloso/projetos/race/race"
url = sys.argv[1] #"https://github.com/velosofelipe64/race"

def main(url, caminho_ospedado, cwd):
    path_project, error_exist, pomPath = RaceCommitCheckout.checkout(url, caminho_ospedado)
    
    if error_exist == False:
        print("Nenhum erro encontrado!")
        return True
    
    error_file, position, type_error, symbol = Interpreter.interpreter(cwd)
    
    if error_file == None or symbol == None:
        print("########################################")
        print("###### Algo inesperado aconteceu  ######")
        print("########################################")
        
        return False

    Fix.fix(path_project, error_file, symbol, position, type_error)

    was_fixed, is_same = FixCommit.new_commit(pomPath, path_project, url, error_file, cwd)
    
    if is_same == "same":
        main(pomPath, url, caminho_ospedado, cwd)
    else:
        return was_fixed

        
print(main(url, caminho_ospedado, cwd))