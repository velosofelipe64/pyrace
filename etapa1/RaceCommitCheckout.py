import os 
from util import Util



def checkout(url, pomPath):
    # catching name of repository from URL
    name_folder = url.split("/")[-1]

    # Validation of Git repository
    if not Util.validRepo(name_folder): 
        os.system("cd /Users/felipeveloso/projetos/ && git clone " + url)

    # Path where the repository was cloned
    path_project = "/Users/felipeveloso/projetos/" + name_folder
    
    # pomPath of Maven 
    pomPath = "/Users/felipeveloso/projetos/race/race"

    # Compiling .java
    os.system("cd " + pomPath + "&& mvn compile > /Users/felipeveloso/projetos/TCC/pyrace/logMaven.txt")
    return path_project