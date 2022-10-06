from this import d
from traceback import print_tb
from git import Repo
import os 
import Validator
import Interpreter
import time

def checkout(url):
    name_folder = url.split("/")[-1]

    if not Validator.validRepo(name_folder):
        print(name_folder)
        os.system("")
        os.system("cd /Users/felipeveloso/projetos/ && git clone " + url)


    path_project = "/Users/felipeveloso/projetos/" + name_folder

    repo = Repo(os.path.join(path_project))
    repoGit = repo.git

    commit1  = repo.commit("248a2c52cff287239abe0e547b9309617436dfd8") #error
    commit2 = repo.commit("5b13067ea902916265379203c2fe118c42545e99") #no error

    errorPath = "race/src/main/java/org/example/App.java"
    pomPath = "/Users/felipeveloso/projetos/race/race"

    repoGit.checkout("248a2c52cff287239abe0e547b9309617436dfd8")
    os.system("cd " + pomPath + "&& mvn compile > /Users/felipeveloso/projetos/TCC/pyrace/etapa1/logMaven.txt")
    error_file, position, type_error, symbol = Interpreter.interpreter()

    repoGit.checkout(commit2)

    javaFile = open(os.path.join(error_file),"r")

    print(javaFile.read())



