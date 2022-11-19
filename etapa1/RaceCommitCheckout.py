import os 
from util import Util



def checkout(url, caminho_ospedado):
    # catching name of repository from URL
    name_folder = url.split("/")[-1]
    
    error_exist = True

    # Validation of Git repository
    if not Util.validRepo(name_folder, caminho_ospedado): 
        os.system("cd " + caminho_ospedado + " && git clone " + url)

    # Path where the repository was cloned
    path_project = caminho_ospedado + "/" +name_folder
    pomPath = caminho_ospedado + "/" +name_folder + "/" +name_folder + "/"
    print(pomPath)
    # Compiling .java
    os.system("cd " + pomPath + " && mvn compile > " + caminho_ospedado + "/pyrace/etapa1/logMaven.txt")
    print("cd " + pomPath + " && mvn compile > " + caminho_ospedado + "/pyrace/etapa1/logMaven.txt")
    dados = open(caminho_ospedado + "/pyrace/etapa1/logMaven.txt","r")
    
    for d in dados.readlines():
        if "BUILD SUCCESS" in d:
            error_exist = False
            return path_project, error_exist, pomPath
    return path_project, error_exist, pomPath