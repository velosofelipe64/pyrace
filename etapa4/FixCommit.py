import os 
from etapa2 import Interpreter



def new_commit(pomPath, project_path, url, error_file, cwd):

    # Compiling .java
    os.system("cd " + pomPath + "&& mvn compile -l "+ cwd +"/etapa1/logMaven.txt")
    dados = open(cwd + "/etapa1/logMaven.txt","r")
    
    for d in dados.readlines():
        if "BUILD SUCCESS" in d:
            os.system("cd " + project_path + " && git add . && git commit -m 'Fix for the error cannot find symbol'")
            return True, "not the same"
    
    error_file, position, type_error, symbol = Interpreter.interpreter(cwd)
    if type_error == 1:
        return False, "same"
    

    os.system("cd " + project_path + " && git restore " + error_file)
    return False, "not the same"