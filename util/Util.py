import os
from weakref import ref
import git 


def validRepo(name_folder):

    projetos_git = "/Users/felipeveloso/projetos/"
    os.system("cd " + projetos_git + name_folder + "/ && ls -la > /Users/felipeveloso/projetos/TCC/pyrace/util/repo_validator.txt")
    ref_arquivo = open("/Users/felipeveloso/projetos/TCC/pyrace/util/repo_validator.txt","r")
    dados = ref_arquivo.read()
    
    try:
        if ".git" in dados:
            print(os.system("cd " + projetos_git + name_folder + "/ && ls -la"))
            return True
            ref_arquivo.truncate()
        else:
            return False
            ref_arquivo.truncate()
    except Exception:
        return False

class GitTools:

    repo = git.Repo()
    repoGit = repo.git