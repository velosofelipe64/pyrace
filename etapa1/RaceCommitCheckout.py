import os 
from util import Util
from etapa2 import Interpreter



def checkout(url):
    # Init of Git fields
    repo = Util.repo
    repoGit = Util.repoGit

    # catching name of repository from URL
    name_folder = url.split("/")[-1]

    # Validation of Git repository
    if not Util.validRepo(name_folder): 
        os.system("cd /Users/felipeveloso/projetos/ && git clone " + url)
    # Path where the repository was cloned
    path_project = "/Users/felipeveloso/projetos/" + name_folder

    # Init repository
    repository = repo(os.path.join(path_project))
    commit1  = repository.commit("248a2c52cff287239abe0e547b9309617436dfd8") #error
    commit2 = repository.commit("5b13067ea902916265379203c2fe118c42545e99") #no error
    
    # pomPath of Maven 
    pomPath = "/Users/felipeveloso/projetos/race/race"

    repoGit.checkout(commit1)
    
    # Compiling .java
    os.system("cd " + pomPath + "&& mvn compile > /Users/felipeveloso/projetos/TCC/pyrace/logMaven.txt")





