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
                return False
            elif tabela[i][j] == '.':
                continue
            else:
                valores.add(tabela[i][j])
        valores.clear()
    
    # Análise das colunas
    for i in range(9):
        for j in range(9):
            if tabela[j][i] in valores:
                return False
            elif tabela[j][i] == '.':
                continue
            else:
                valores.add(tabela[j][i])
        valores.clear()
    
    return True


board1 = [["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
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

board3 = [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".","x","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".","=","6"]
   ,[".","6","o"," ",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]

if validaTabela(board1):
    print(validaSudoku(board1)) # saída: True - é uma tabela válida

if validaTabela(board2):
    print(validaSudoku(board2)) # saída: False - possui números iguais em uma coluna

if validaTabela(board3):
    print(validaSudoku(board3)) # saída: nenhuma - não entra no 'if'
