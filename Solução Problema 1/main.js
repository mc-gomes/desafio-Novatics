function ordenaNumeros(a, b) {
    return a - b
}

function removeRepetido(lista) {
    return lista.filter(function(valor, pos, array) {
        return !pos || valor != array[pos - 1]
    })
}


console.log("--- Manipulando listas --- \n")

var listaNumeros = [12, 5, 1, 4, 7, 0, 12, 35, 21, 150, 10, 4]
console.log("Antes: ", listaNumeros)

var listaNumAux = listaNumeros.sort(ordenaNumeros)

var listaSemRep = removeRepetido(listaNumAux)
console.log("Depois: ", listaSemRep)
