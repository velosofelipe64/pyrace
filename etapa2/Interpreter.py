import re


def interpreter():
    dados = open("/Users/felipeveloso/projetos/TCC/pyrace/logMaven.txt","r")

    type_error = -1
    error = ""
    error_inline = ""

    for i in dados.readlines():
        # Only the errors line
        if "[ERROR]" in i:
            
            error_inline = error_inline + " " + str(i.strip())
        # Only the error line with information
        if "[ERROR] /" in i:
            error = i
    # No errors
    if error_inline == "":
        type_error = 0
        return None, None, type_error, None
    # Type error equals 1
    if "cannot find symbol" in error:
        type_error = 1

        symbol_regex = re.search(r"(?<=symbol:).*?(?=[ERROR])", error_inline)
        errorLine_regex = re.search("[ERROR](.*?)cannot find symbol", error)
        symbol = symbol_regex[0].replace("[", "").strip()

        error_file, position = errorLine_regex.group(1).replace("RROR] ","").split(":")
        return error_file, position, type_error, symbol


