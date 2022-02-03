// console.log('hello world')


// let x = "boring"

// console.log(`javascript is ${x}`)


// function myfunc(x) {
//     console.log(`javascript is ${x}`)
// }


// myfunc(x)

for (let i = 0; i < 3; i++){
    console.log('simcha')
}
console.log(i)

for (var i = 0; i < 3; i++){
    console.log('simcha')
}
console.log(i)


hello = () => {
    var x = "simcha"
    return (`hello ${x}`)
}

console.log(hello())