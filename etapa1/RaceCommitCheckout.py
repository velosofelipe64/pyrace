import os 
from util import Util



def checkout(url, pomPath, caminho_ospedado):
    # catching name of repository from URL
    name_folder = url.split("/")[-1]

    # Validation of Git repository
    if not Util.validRepo(name_folder, caminho_ospedado): 
        os.system("cd " + caminho_ospedado + " && git clone " + url)

    # Path where the repository was cloned
    path_project = caminho_ospedado + "/" +name_folder

    # Compiling .java
    os.system("cd " + pomPath + "&& mvn compile > " + caminho_ospedado + "/pyrace")
    return path_project