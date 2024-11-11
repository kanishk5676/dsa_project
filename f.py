import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, name, hours=None):
        self.name = name           # Name of the module, topic, or subtopic
        self.hours = hours          # Duration in hours (optional for each node)
        self.resources = {}         # HashMap for additional resources
        self.children = []          # List of child TreeNode instances
        self.questions_map = {}     # HashMap for storing questions related to the topic

    def add_child(self, child_node):
        """Add a child node to this node."""
        self.children.append(child_node)

    def add_resource(self, key, url):
        """Add a resource link to the resources hashmap."""
        self.resources[key] = url

    def add_questions(self, topic, questions):
        """Store questions for a specific topic in the hashmap."""
        self.questions_map[topic] = questions

    def display_tree(self, level=0):
        """Recursively display the tree structure."""
        indent = "  " * level
        hours_info = f" ({self.hours} hours)" if self.hours else ""
        print(f"{indent}- {self.name}{hours_info}")
        for key, url in self.resources.items():
            print(f"{indent}    {key}: {url}")
            self.display_questions()  # Print questions right after the resource
        for child in self.children:
            child.display_tree(level + 1)

    def display_questions(self):
        """Print questions for the current node topic."""
        if self.name in self.questions_map:
            print("    Questions:")
            for question in self.questions_map[self.name]:
                print(f"        - {question}")

def build_syllabus_tree():
    # Root node: Syllabus
    syllabus = TreeNode("Data Structures and Algorithms Syllabus")

    # Module 1: Algorithm Analysis
    module1 = TreeNode("Module 1: Algorithm Analysis", 8)
    module1.add_child(TreeNode("Importance of algorithms and data structures"))
    module1.add_child(TreeNode("Fundamentals of algorithm analysis"))
    module1.add_child(TreeNode("Space and time complexity"))
    module1.add_child(TreeNode("Asymptotic notations and orders of growth"))
    module1.add_child(TreeNode("Algorithm efficiency: best, worst, and average case"))
    module1.add_child(TreeNode("Analysis of non-recursive and recursive algorithms"))
    asymptotic_analysis = TreeNode("Asymptotic analysis for recurrence relations")
    asymptotic_analysis.add_resource("Recurrence Relations Explained", "https://youtu.be/4V30R3I1vLI?si=ofK-lcoxqETjhM3W")
    asymptotic_analysis.add_questions("Asymptotic analysis for recurrence relations", [
        "What is the difference between best, worst, and average case analysis?",
        "Explain asymptotic notations like Big O, Omega, and Theta."
    ])
    module1.add_child(asymptotic_analysis)
    syllabus.add_child(module1)

    # Module 2: Linear Data Structures
    module2 = TreeNode("Module 2: Linear Data Structures", 7)
    arrays = TreeNode("Arrays: 1D and 2D array")
    arrays.add_resource("Arrays in Data Structures", "https://youtu.be/p5TDnxAYAZY?si=iHCmbu7WHYuZUjjN")
    arrays.add_questions("Arrays: 1D and 2D array", [
        "What is the difference between a 1D and 2D array?",
        "How do you access elements in a 2D array?"
    ])
    module2.add_child(arrays)

    stack = TreeNode("Stack and its Applications")
    stack.add_resource("Introduction to Stacks", "https://youtu.be/bxRVz8zklWM?si=bXFDAA3eSPPEZmnu")
    stack.add_questions("Stack and its Applications", [
        "What are the operations of a stack?",
        "How is a stack used in expression evaluation?"
    ])
    module2.add_child(stack)

    queue = TreeNode("Queue and its Applications")
    queue.add_resource("Introduction to Queues", "https://youtu.be/zp6pBNbUB2U?si=CP6TzGfTkqAsHf-p")
    queue.add_questions("Queue and its Applications", [
        "What is the difference between a queue and a stack?",
        "Explain the concept of circular queue."
    ])
    module2.add_child(queue)

    linked_list = TreeNode("List: Singly, Doubly, Circular linked lists")
    linked_list.add_resource("Singly Linked List Explanation", "https://youtu.be/dmb1i4oN5oE?si=-VREz3hZhB7lKPd2")
    linked_list.add_questions("List: Singly, Doubly, Circular linked lists", [
        "What is the difference between singly and doubly linked lists?",
        "Explain the advantages of circular linked lists."
    ])
    module2.add_child(linked_list)

    syllabus.add_child(module2)

    # Module 3: Searching and Sorting
    module3 = TreeNode("Module 3: Searching and Sorting", 7)
    searching = TreeNode("Searching: Linear Search, Binary Search")
    searching.add_resource("Binary Search Algorithm", "https://www.youtube.com/watch?v=V_T5NuccwRA&t=2s")
    searching.add_questions("Searching: Linear Search, Binary Search", [
        "What is the time complexity of binary search?",
        "Explain how linear search differs from binary search."
    ])
    module3.add_child(searching)

    sorting = TreeNode("Sorting: Insertion, Selection, Bubble, Counting, Quick, Merge sort")
    sorting.add_resource("Quick Sort Explained", "https://www.youtube.com/watch?v=HGk_ypEuS24")
    sorting.add_questions("Sorting: Insertion, Selection, Bubble, Counting, Quick, Merge sort", [
        "What is the worst-case time complexity of Quick Sort?",
        "Explain how merge sort works."
    ])
    module3.add_child(sorting)

    syllabus.add_child(module3)

    module4 = TreeNode("Module 4: Trees", 6)
    binary_tree = TreeNode("Binary Tree: Definition and Properties")
    binary_tree.add_resource("Binary Trees for Beginners", "https://youtu.be/-b2lciNd2L4?si=DmoaRD7WU64pexIR")
    binary_tree.add_questions("Binary Tree: Definition and Properties", [
        "What are the properties of a binary tree?",
        "How do you traverse a binary tree?"
    ])
    module4.add_child(binary_tree)
    
    tree_traversal = TreeNode("Tree Traversals")
    tree_traversal.add_resource("Tree Traversal Techniques", "https://www.youtube.com/watch?v=xo41NfT8218")
    tree_traversal.add_questions("Tree Traversals", [
        "What are the different types of tree traversal?",
        "Explain in-order, pre-order, and post-order traversal."
    ])
    module4.add_child(tree_traversal)
    
    bst = TreeNode("Binary Search Trees (BST)")
    bst.add_resource("BST Operations", "https://www.youtube.com/watch?v=cySVml6e_Fc")
    bst.add_questions("Binary Search Trees (BST)", [
        "How do you perform insert and delete operations in a BST?",
        "What are the advantages of using a BST?"
    ])
    module4.add_child(bst)
    
    syllabus.add_child(module4)

    # Module 5: Graphs
    module5 = TreeNode("Module 5: Graphs", 6)
    graph_traversal = TreeNode("Graph Traversal: BFS and DFS")
    graph_traversal.add_resource("Breadth First Search", "https://youtu.be/5hPfm_uqXmw?si=5THw2enJdVKGxrM1")
    graph_traversal.add_resource("Depth First Search", "https://youtu.be/vf-cxgUXcMk?si=4wFfht2pgU-30z8-")
    graph_traversal.add_questions("Graph Traversal: BFS and DFS", [
        "What is the difference between BFS and DFS?",
        "How do BFS and DFS differ in terms of implementation?"
    ])
    module5.add_child(graph_traversal)
    
    mst = TreeNode("Minimum Spanning Tree: Prim's and Kruskal's")
    mst.add_resource("Prim's Algorithm", "https://www.youtube.com/watch?v=QRS678")
    mst.add_resource("Kruskal's Algorithm", "https://www.youtube.com/watch?v=TUV901")
    mst.add_questions("Minimum Spanning Tree: Prim's and Kruskal's", [
        "What is a minimum spanning tree?",
        "Explain Prim's and Kruskal's algorithms."
    ])
    module5.add_child(mst)
    
    syllabus.add_child(module5)
    
    # Module 6: Hashing
    module6 = TreeNode("Module 6: Hashing", 4)
    hashing_methods = TreeNode("Hash functions and Open Hashing")
    hashing_methods.add_resource("Introduction to Hashing", "https://www.youtube.com/watch?v=WXY234")
    hashing_methods.add_questions("Hash functions and Open Hashing", [
        "What is a hash function?",
        "Explain the concept of open hashing."
    ])
    module6.add_child(hashing_methods)
    
    syllabus.add_child(module6)
    
    # Module 7: Heaps and AVL Trees
    module7 = TreeNode("Module 7: Heaps and AVL Trees", 5)
    heaps = TreeNode("Heaps and Heap sort")
    heaps.add_resource("Heap Sort Algorithm", "https://www.youtube.com/watch?v=XYZ678")
    heaps.add_questions("Heaps and Heap sort", [
        "What are heaps, and how are they used in heap sort?",
        "What is the time complexity of heap sort?"
    ])
    module7.add_child(heaps)

    avl_tree = TreeNode("AVL Trees: Balanced Binary Search Tree")
    avl_tree.add_resource("AVL Trees Overview", "https://www.youtube.com/watch?v=ZZZ789")
    avl_tree.add_questions("AVL Trees: Balanced Binary Search Tree", [
        "What are AVL trees?",
        "Explain how balancing is done in AVL trees."
    ])
    module7.add_child(avl_tree)

    syllabus.add_child(module7)

    # Printing syllabus with resources and questions
    print("DSA Syllabus Tree Structure with Resources:")
    syllabus.display_tree()

    return syllabus

# Call the function
syllabus_tree = build_syllabus_tree()  # Build and display the syllabus tree with resources and questions
