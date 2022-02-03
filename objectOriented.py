class TreeNode(object):
        def __init__(self, val=0, left = None, right = None):
            self.val = val
            self.left = left
            self.right = right

x = TreeNode(1)
y = TreeNode(2)
z = TreeNode(3)

x.left = y
x.right = z



class Solution:

    def invertTree(self, root):
       
        if root == None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left) 
        
        root.left = r
        root.right = l
        
        return root
        

solution = Solution()
print(solution.invertTree(x).right.val)

# reverse a linked list
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head
