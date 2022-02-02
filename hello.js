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
    insert(node){
        if (!this.root){
            this.root = node
        }
        let iterator = this.root 
        while (iterator.right || iterator.left ){
            if (node.value <= iterator.value){
                iterator = iterator.left
            }
            if (node.value >= iterator.value){
                iterator = iterator.right
            }
        }
        if (node.value < iterator.value){
            iterator.left = node
        }
        if (node.value > iterator.value){
            iterator.right = node
        }
        console.log(this)
        return this
    }
}

let tree = new BST();
// tree.root = new Node(10)
// console.log(tree)


tree.insert(new Node(19))
// console.log(tree)


