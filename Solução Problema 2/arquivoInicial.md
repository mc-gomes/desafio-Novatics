## Problema 2 - Validando Sudoku

Determine se uma tabela de Sudoku está valida, ou seja, os elementos inseridos correspondem as regras do jogo. Essas regras são:

1. Cada linha deve conter dígitos de 1 - 9, SEM repetição;
2. Cada coluna deve conter dígitos de 1 - 9, SEM repetição;
3. Todas as noves mini-tabelas devem conter dígitos de 1 - 9, SEM repetição;

Sudoku válido:

![valid_sudoku](https://user-images.githubusercontent.com/22327574/145793588-5e8d6629-ea0b-4323-b4be-e775729da11f.png)

#### Exemplo de como deve funcionar a solução:

```
board =
   [["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]

   output: true
```

```
board =
   [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]

   output: false
```
