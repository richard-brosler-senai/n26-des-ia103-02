// Exemplo de uso do var
if (true) {
    var expulsoDoBloco = "Eu consigo sair daqui!";
    let presoNoBloco = "Eu não consigo sair...";
}

console.log(expulsoDoBloco); // Resultado: Eu consigo sair daqui!
console.log(presoNoBloco);    // Resultado: Uncaught ReferenceError: presoNoBloco is not defined
