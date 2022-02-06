function ordenaNumeros(a, b) {
    return a - b
}

function removeRepetido(lista) {
    return lista.filter(function (valor, pos, array) {
        return !pos || valor != array[pos - 1]
    })
}

function manipulacao(lista) {
    var listaNumAux = []
    var listaSemRep = []

    console.log("\nExemplo:")
    console.log("Antes: ", lista)

    listaNumAux = lista.sort(ordenaNumeros)
    listaSemRep = removeRepetido(listaNumAux)

    console.log("Depois: ", listaSemRep)
}

console.log("--- Manipulando listas --- ")

var lista1 = [12, 5, 1, 4, 7, 0, 12, 35, 21, 150, 10, 4]
manipulacao(lista1)

var lista2 = [8, 5, 10, 5, 2, 4, 4, 3]
manipulacao(lista2)

var lista3 = [8, 8, 7, 7, 1, 6, 5, 5, 3, 1]
manipulacao(lista3)
