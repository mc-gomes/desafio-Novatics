def validaTabela(tabela):
    # Analisa se é uma tabela de tamanho 9x9
    
    valoresValidos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '', ' ']
    # os valores '.', '', ' ' indicam espaços não preenchidos, por isso são válidos

    if len(tabela) != 9:
        return False
    else:
        for i in range(len(tabela)):
            if len(tabela[i]) != 9:
                return False

    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            if tabela[i][j] not in valoresValidos:
                return False

    return True

def validaSudoku(tabela):
    # Verifica se há algum valor repetido nas linhas e colunas

    valores = set()
    
    # Análise das linhas
    for i in range(9):
        for j in range(9):
            if tabela[i][j] in valores:
                print('linha')
                return False
            elif tabela[i][j] in ['.', '', ' ']:
                continue
            else:
                valores.add(tabela[i][j])
        valores.clear()
    
    # Análise das colunas
    for i in range(9):
        for j in range(9):
            if tabela[j][i] in valores:
                return False
            elif tabela[j][i] in ['.', '', ' ']:
                continue
            else:
                valores.add(tabela[j][i])
        valores.clear()
    
    # Análise das mini-tabelas 3x3
    combinacoes = [range(0,3), range(3,6), range(6,9)]
    coorden = []

    for x in combinacoes:
        for y in combinacoes:
            coorden.append([x,y])

    for (linhaMiniTabela, colMiniTabela) in coorden:
        for i in linhaMiniTabela:
            for j in colMiniTabela:              
                if tabela[i][j] in valores:
                    return False
                elif tabela[i][j] in ['.', '', ' ']:
                    continue
                else:
                    valores.add(tabela[i][j])
        valores.clear()

    return True


board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6","."," ",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

board3 = [["8","3",".",".","",".",".",".","."]
         ,["6",".",".",".","",".",".",".","."]
         ,[".","9","8",".",".",".",".","","."]
         ,[".",".",".",".",".",".",".",".",""]
         ,[".",".",".","",".","",".",".","."]
         ,[".",".",".",".","",".",".",".",""]
         ,[".","",".",".",".",".","","","."]
         ,[".",".",".","","",".",".",".",""]
         ,[".",".",".",".","",".",".","","."]]

board4 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".","x","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".","/","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".","=","6"]
         ,[".","6","o"," ",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]


if validaTabela(board1):
    print(validaSudoku(board1)) # saída: True - é uma tabela válida

if validaTabela(board2):
    print(validaSudoku(board2)) # saída: False - possui números iguais em uma coluna

if validaTabela(board3):
    print(validaSudoku(board3)) # saída: False - uma tabela 3x3 possui números repetidos

if validaTabela(board4):
    print(validaSudoku(board4)) # saída: nenhuma - não entra no 'if' pois possui valores inválidos
