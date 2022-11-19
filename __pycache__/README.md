<h1 align="center"> RACE: Ferramenta de Resolução Automática de Erros de Compilação  </h1>


RACE é uma ferramenta de reparo automática de erros de build. 
Foi pensada para solucionar quebras de processos de build causadas por erros de compilação.


<h5 align="center"> 
     Projeto em construção  
</h5>


### Requisitos técnicos para execução do projeto:

- `Python3` (https://www.python.org/)
- `Maven` (https://maven.apache.org/)
- `GitPython(Biblioteca Python)`: (https://gitpython.readthedocs.io/en/stable/intro.html)

### Como usar a ferramenta:
- Primeiramente deve-se ter a ferramenta RACE clonada localmente e todos os requisitos técnicos instalados.

- Obter um repositório que apresente o error de quebra de build `cannot find symbol (method)`

- Para executar deve-se estar no diretório raiz do projeto e utilizando a comando python3 Main.py, passando como parâmetro o link do repositório GitHub do projeto que apresenta erro.

````
$ python3 Main.py https://github.com/usertest/test
