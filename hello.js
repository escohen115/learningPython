console.log('hello world')


let x = "boring"

console.log(`javascript is ${x}`)


function myfunc(x) {
    console.log(`javascript is ${x}`)
}


myfunc(x)



class Node{
    constructor(value){
        this.value = value
        this.left = null
        this.right = null
    }
}

class BST{
    constructor(){
        this.root = null
    }
}

let tree = new BST();
tree.root = new Node(10)
