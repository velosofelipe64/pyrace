from etapa1 import RaceCommitCheckout
from etapa2 import Interpreter
from etapa3 import Fix
from etapa4 import FixCommit
logMaven = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa1/logMaven.txt", "a")



pomPath = "/Users/felipeveloso/projetos/race/race"
url = "https://github.com/velosofelipe64/race"
def main(pomPath, url):
    path_project = RaceCommitCheckout.checkout(url, pomPath)

    error_file, position, type_error, symbol = Interpreter.interpreter()

    Fix.fix(path_project, error_file, symbol, position, type_error)

    was_fixed, is_same = FixCommit.new_commit(pomPath, path_project, url, error_file)

    if is_same == "same":
        main(pomPath, url)
    else:
        return was_fixed

        
print(main(pomPath, url))