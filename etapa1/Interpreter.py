import re


def interpreter():
    dados = open("/Users/felipeveloso/projetos/TCC/pyrace/etapa1/logMaven.txt","r")

    error = ""
    error_inline = ""
    for i in dados.readlines():
        if "[ERROR]" in i:
            
            error_inline = error_inline + " " + str(i.strip())
        if "[ERROR] /" in i:
            error = i

    type_error = -1
    if "cannot find symbol" in error:
        type_error = 1
        x = re.search(r"(?<=symbol:).*?(?=[ERROR])", error_inline)
        y = re.search("[ERROR](.*?)cannot find symbol", error)
        symbol = x[0].replace("[", "").strip()

        error_file, position = y.group(1).replace("RROR] ","").split(":")
        return error_file, position, type_error, symbol


