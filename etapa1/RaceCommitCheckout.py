from this import d
from traceback import print_tb
from git import Repo
import os 
import Validator


url_project = "https://github.com/velosofelipe64/race"
name_folder = url_project.split("/")[-1]

if not Validator.validRepo(name_folder):
    os.system("git clone" + url_project)


path_project = "/Users/felipeveloso/projetos/" + name_folder

repo = Repo(os.path.join(path_project))
repoGit = repo.git

commit1  = repo.commit("248a2c52cff287239abe0e547b9309617436dfd8")
commit2 = repo.commit("5b13067ea902916265379203c2fe118c42545e99")

errorPath = "race/src/main/java/org/example/App.java"
pomPath = "/Users/felipeveloso/projetos/race/race"

repoGit.checkout("248a2c52cff287239abe0e547b9309617436dfd8")
os.system("cd " + pomPath + "&& mvn compile > logMaven.txt")



# for diff in diff_index:
#     print(diff)
#     print(diff.change_type)
#     print(f"{diff.a_path} -> {diff.b_path}")



