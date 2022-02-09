class Node{
    constructor(val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}


class DoublyLinkedList {
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val){
        var newNode = new Node(val);
        if(this.length === 0){
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }
    shift (){
        if (this.length === 0) return undefined;
        if (this.length === 1){
            this.head = null
            this.tail = null
            this.length = 0
        }
        let oldHead = this.head
        this.head = oldHead.next
        this.head.previous = null
        oldHead.next = null
        this.length--
        return oldHead
    }

}
        




