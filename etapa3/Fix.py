from hashlib import new
import os
import git 
import re
import subprocess


def fix(project_path, error_file, symbol, position, type_error):
    # fix for cannot find symbol
    if type_error == 1:
        return fix_type_one(project_path, error_file, symbol, position)

def fix_type_one(project_path, error_file, symbol, position):
    if "method" in symbol:

        symbol_sign = symbol.replace("method ", "")
        symbol = re.sub("[(].*?[)]","",symbol_sign)
        
        head_commit = "HEAD"

        os.system('cd ' + project_path + ' && git log --pretty=%P -n 1 "' + head_commit + '" > /Users/felipeveloso/projetos/TCC/pyrace/etapa3/id_commit.txt')

        id_commit = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/id_commit.txt", "r").readline()

        array_commits = []
        if " " in id_commit.strip():
            array_commits = id_commit.split(" ")
        else:
            array_commits.append(id_commit)

        for i in array_commits:

            
            bash = "sh /Users/felipeveloso/projetos/TCC/pyrace/etapa3/bash_git_diff.sh " + project_path + " " + str(i).strip() + " " + error_file.replace(project_path+"/","")
            subprocess.call(bash, shell=True)
        
            data = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/git_diff.txt", "r")

            if data.readline() != None:
                break
                    
    
        data = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa3/git_diff.txt", "r")
        data_array = data.readlines()

        count_adds = 0
        for i in range(len(data_array)-1):
            if len(data_array[i]) >= 2:
                if (data_array[i][0] + data_array[i][1]) == "+ ":
                    count_adds = count_adds + 1

        if count_adds == 0:
            # Não ouve adição de um novo methodo, apenas remoção
            # Remover metodo
            with open(error_file, "r") as f:
                lines = f.readlines()
            with open(error_file, "w") as f:
                for line in lines:
                    if symbol not in line.strip("\n"):
                        f.write(line)

        new_name = ""
        test = open(error_file,"r")
        print(test.readlines()[14])
        for i in range(len(data_array)-1):    
            if symbol in data_array[i] and (data_array[i][0] + data_array[i][1]) == "- ":
                sign = re.search("[(].*?[)]" , data_array[i])
                
                if sign[0] in data_array[i+1] and (data_array[i+1][0] + data_array[i+1][1]) == "+ ":
                    # Extrair novo nome  fazer correção
                    new_name = data_array[i+1].replace("public","").replace("static","").replace("void","").replace("+","").strip()
                    new_name = re.findall(" (.*?)[(]",new_name)
                    
                    with open(error_file, "r") as f:
                        lines = f.readlines()
                    with open(error_file, "w") as f:
                        for line in lines:
                            if symbol in line.strip("\n"):
                                line = line.replace(symbol, new_name[0])
                                f.write(line)
                            else:
                                f.write(line)





