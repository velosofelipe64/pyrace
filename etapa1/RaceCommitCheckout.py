from this import d
from traceback import print_tb
from git import Repo
import os 

repo = Repo(os.path.join("/Users/felipeveloso/projetos/race"))
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



