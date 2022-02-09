







function shift (list){
    if (list.head === null) return null;
    let oldHead = list.head
    this.head = list.head.next
    list.head.next = null


    return oldHead

}