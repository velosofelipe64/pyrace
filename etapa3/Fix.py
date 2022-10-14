import os
from util import Util

def fix(error_file, position, type_error, symbol):

    
    # COLOCAR EM UM METODO SEPARADO
    if type_error == 1:

        Util.repoGit.checkout()

        if "method" in symbol:
            symbol = symbol.replace("method ","").strip()

        print(symbol)
    javaFile = open(os.path.join(error_file),"r")

    print(javaFile.read())