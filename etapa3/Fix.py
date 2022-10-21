import os
import git 
import re

# def fix(error_file, position, type_error, symbol, path_of_project):
error_file = "App.java"
path_of_project = "/Users/felipeveloso/projetos/race"


repository = git.Repo(os.path.join(path_of_project))
# repoGit = repository.git()
# commits = list(repo.iter_commits(repository))
print(repository.head)

# for c in commits:
#     # print(c)
#     files = os.system("cd "+ path_of_project+ " && git diff-tree --no-commit-id --name-only -r " + str(c))

    # if error_file in files:
        
    # if type_error == 1:

    #     Util.repoGit.checkout()

    #     if "method" in symbol:
    #         symbol = symbol.replace("method ","").strip()



        
    # javaFile = open(os.path.join(error_file),"r")

    # print(javaFile.read())

def isMethod(sign):
    if "(" in sign and ")" in sign and "{" in sign:
        return True
    else:
        return False

def pre_fix(project_path, error_file, symbol): 

    head_commit = "HEAD"
    git_diff_inline = ""
    git_diff = ""
  
    os.system('cd ' + project_path + ' && git log --pretty=%P -n 1 "' + head_commit + '" > /Users/felipeveloso/projetos/TCC/pyrace/etapa3/id_commit.txt')

    id_commit = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/id_commit.txt", "r").readline()

    array_commits = []
    if "," in id_commit:
        array_commits = id_commit.split(",")
    else:
        array_commits.append(id_commit)

    for i in array_commits:

        # Teoriacamente isso deveria funcionar
        # os.system('cd '+ project_path +' && git diff ' + str(i) + '/Users/felipeveloso/projetos/race/race/src/main/java/org/example/App.java > /Users/felipeveloso/projetos/TCC/pyrace/etapa3/git_diff.txt')
    
        data = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/git_diff.txt", "r")

        if data.readline() != None:
            break
            
    
    
   
    data = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/git_diff.txt", "r")
    data_array = data.readlines()
    for i in range(len(data_array)-1): 
        if symbol in data_array[i] and (data_array[i][0] + data_array[i][1]) == "- ":
            print(symbol)
            sign = re.search("[(].*?[)]" , data_array[i])
            # sign = re.search(r'(.*)',sign[0])
            print(sign)
        
        # for i in range(len(diff)):
        #     if symbol + "(" in diff[i]:
                # if "+ " in diff[i+1] and isMethod(diff[i+1]):
            # Validar a diferança pela assinatura no metodo (parametros)


            
        # diff = re.findall(" @@ p.*", git_diff_inline)
        # diff = re.findall("- .*?+ ",diff)
        # print(diff)

        # diff = diff.split("+")
        # if (len(diff) <= 1):
        #     # apenas remover o metodo
        


pre_fix("/Users/felipeveloso/projetos/race", "App.java", "plusTen")


