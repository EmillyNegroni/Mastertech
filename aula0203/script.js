//let degrau = '#';
//for (let i=0; i<5; i++){
    //console.log(degrau);
   // degrau+= '#';
//}

//function somar (a,b) {
    //return a + b 
//}
//console.log(somar(2,4))
//
//---------------- ------------------exercicio escada--------------------------------------------//
function fazerEscada (material,degrau){
    let escada = material;
    for (let  i = 0; i < degrau; i++){
        console.log (escada)
        escada += material;
    }
}
//---------------------------- ------Par ou impar-------------------------------------------//
function parOuImpar (a){
    if (a % 2 == 0){
        return 'É par';
    }
    else{
        return 'É impar';
    }
}
//----------------------- ------Numeros aleatorios -------------------------------------------//
//---------------- ------e numeros inteiros math.floor() -------------------------------------------//
const aleatorio = function (min,max){
    //return Math.floor(Math.random() * 100); // de 0 á 100 intervalo de cem numbers
    return Math.floor(Math.random() * (max - min) ) + min ; // numeros onde eu tenha que estipular o valor do meu intervalo p ex 5,10
}
