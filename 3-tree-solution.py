class BST:

    class Node:
        def __init__(self, data):      
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)

        else:
            self._insert(data, self.root) 

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)

            else:
                self._insert(data, node.left)

        elif data == node.data:
            return

        else:
            if node.right is None:
                node.right = BST.Node(data)

            else:
                self._insert(data, node.right)

    def __contains__(self, data):
        return self._contains(data, self.root) 

    def _contains(self, data, node):
        if node == None:
            return False

        elif node.data == data:
            return True

        elif data > node.data:
            return self._contains(data, node.right)

        else:
            return self._contains(data, node.left)

    def __iter__(self):
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):
        if self.root is None:
            return 0

        else:
            return self._get_height(self.root) 

    def _get_height(self, node):
        if node is None:
            return 0
            
        return 1 + max(self._get_height(node.left),self._get_height(node.right))

def add_ids_to_bst_from_sorted_list(sorted_list, bst = None):
    if bst:
        _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    else: 
        bst = BST()  # Create an empty BST to start with 
        _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst
    
def _insert_middle(sorted_list, first, last, bst):
    if len(sorted_list) == 0:
        return 
    else:
        middle = (last + first) // 2
        bst.insert(sorted_list[middle])
        if middle != last:
            _insert_middle(sorted_list, middle + 1, last, bst)
        if middle != first:
            _insert_middle(sorted_list, first, middle - 1 , bst)
        
# Create new BST
system = BST()

# Insert ids
system.insert(1314582)
system.insert(3968425)
system.insert(1475434)
system.insert(6761582)
system.insert(9975634)
system.insert(6427145)

for file in system:
    if file == 6427145:
        print(file) # 6427145

print(1475434 in system) # True
print(1475435 in system) # False

for file in system:
    print(file)
"""
6427145
1314582
1475434
3968425
6427145
6761582
9975634
"""

# Add an array of files to the system
add_ids_to_bst_from_sorted_list([1111111,2222222,3333333], system)

# Check the height of the tree
print(system.get_height())
# 5

# Re-origanize the system to a more balanced bst
allFiles = []
for file in system:
    allFiles.append(file)
# allFiles = [1111111, 1314582, 1475434, 2222222, 3333333, 3968425, 6427145, 6761582, 9975634]

system = add_ids_to_bst_from_sorted_list(allFiles)

# Check the height after re-origanization
print(system.get_height())
# 4