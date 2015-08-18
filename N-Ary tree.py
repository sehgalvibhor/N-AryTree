class Node(object):
    # Class for N-Ary tree
    def __init__(self,name,value):
        self.value = value
        self.name = name
        self.children = []

    def add_child(self, obj):
        # Adding child to the Node
        self.children.append(obj)

def inorder(tree,thresh,ans):
    # Traversing all the possible nodes of the tree
    for x in tree.children:
        if x.value>thresh:
            # Comparing with the threshold value and adding if greater
            ans.append(x.name)
        inorder(x,thresh,ans)
            
    return ans

if __name__ == '__main__':
    ans=[] #List to store the final answer
    # Creating individual nodes of the tree, supposing the values and name to be same.
    root = Node('1',1)
    b = Node('2',2)
    c = Node('3',3)
    d = Node('4',4)
    e = Node('5',5)
    f = Node('6',6)
    g = Node('7',7)
    h = Node('8',8)
    i = Node('9',9)
    j = Node('10',10)
    k = Node('11',11)
    l = Node('12',12)
    m = Node('13',13)
    o = Node('14',14)
    
    # Creating the Tree by adding the child to each node
    root.add_child(b)
    root.add_child(c)
    root.add_child(f)
    b.add_child(d)
    b.add_child(e)
    d.add_child(h)
    e.add_child(i)
    i.add_child(l)
    i.add_child(m)
    i.add_child(o)
    c.add_child(g)
    g.add_child(j)
    g.add_child(k)
    thresh=input("Enter the threshold value \n")
    inorder(root,thresh,ans)
    if len(ans)==0:
        print "No value greater than threshold"
    else:
        print "Values greater than threshold are",ans


