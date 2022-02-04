function ordenaNumeros(a, b) {
    return a - b
}


console.log("--- Manipulando listas --- ")

var listaNumeros = [12, 5, 1, 4, 7, 0, 12, 35, 21, 10, 4]
console.log("Antes: ", listaNumeros)

var listaNumAux = listaNumeros.sort(ordenaNumeros)
console.log("Depois: ", listaNumAux)

