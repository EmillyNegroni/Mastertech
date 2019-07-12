
//const aleatorio = function (min,max){
    //return Math.floor(Math.random() * (max - min + 1)) + 1;
//}

//============================EXERCICIO COM FUNCAO====================================================//

function criterios(idade,valorEmp,salario){
    if (idade < 22 || idade > 55 ||  valorEmp < 1000 || valorEmp > salario * 15 || qtdparcelas < 3 || qtdparcelas >20){
        console.log ("NÃO ACEITO");
    }
    else{
        console.log ("ACEITO!");
        let  montante;
        montante = valorEmp * (1 + 0.09) ** qtdparcelas;
        let parcela = montante/qtdparcelas;
        console.log( `O valor total do emprestimo é de ${montante} e o valor da parcela  é de ${parcela}`)
    }
}
//============================ EXERCICIO COM LISTA E FUNCAO====================================================//
let filmes = [
    {titulo : ' Harry Potter', classificacao : 12},
    {titulo : 'As branquelas', classificacao : 16},
    {titulo : 'Rei Leão' , classificacao : 10},
    {titulo : 'Interestelar', classificacao : 10} ,
    {titulo : ' Ninja Assasino' , classificacao : 18},
    {titulo : ' John Wick' , classificacao : 16},
    {titulo : 'Velozes e furiosos' , classificacao: 14}
]
// finalizar exercicio 
function cinema(idade){
    for (i = 0; i >= 6; i++){
        console.log([i]);
    }
}