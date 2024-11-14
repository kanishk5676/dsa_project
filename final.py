import matplotlib.pyplot as plt
import networkx as nx
import random
import time

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
        for child in self.children:
            child.display_tree(level + 1)

class Node:
    """Class for creating a Node in the linked list."""
    def __init__(self, module_time):
        self.module_time = module_time  # Time for this module (in seconds)
        self.next = None  # Pointer to the next node

class LinkedList:
    """Linked list to store module times."""
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0  # Initialize the counter for the number of nodes

    def append(self, module_time):
        """Append a module time to the linked list."""
        new_node = Node(module_time)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.number_of_nodes += 1  # Increment the number of nodes whenever a new one is added

    def print_times(self):
        """Print all stored module times along with module number."""
        current = self.head
        total_time = 0
        print("\nTime taken for each module:")
        module_number = 1  # Start from module 1
        while current:
            # Convert time to hours, minutes, seconds format
            hours = int(current.module_time // 3600)
            minutes = int((current.module_time % 3600) // 60)
            seconds = int(current.module_time % 60)
            print(f"Module {module_number}: {hours:02}:{minutes:02}:{seconds:02}")
            total_time += current.module_time
            current = current.next
            module_number += 1  # Increment the module number

        # Convert total time to hours, minutes, seconds
        total_hours = int(total_time // 3600)
        total_minutes = int((total_time % 3600) // 60)
        total_seconds = int(total_time % 60)

        print(f"\nTotal time taken for the lesson: {total_hours:02}:{total_minutes:02}:{total_seconds:02}")
        
def build_DSA_syllabus_tree():
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

    # Module 4: Trees
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
        "What are the advantages of using a binary search tree?",
        "How do you balance a binary search tree?"
    ])
    module4.add_child(bst)

    syllabus.add_child(module4)

    # Module 5: Graphs
    module5 = TreeNode("Module 5: Graphs", 6)
    bfs_dfs = TreeNode("Graph Traversals: BFS and DFS")
    bfs_dfs.add_resource("Breadth-First Search (BFS)", "https://www.youtube.com/watch?v=AfSk1vA2j8Y")
    bfs_dfs.add_questions("Graph Traversals: BFS and DFS", [
        "What is the difference between BFS and DFS?",
        "How do BFS and DFS differ in terms of implementation?"
    ])
    module5.add_child(bfs_dfs)

    mst = TreeNode("Minimum Spanning Tree")
    mst.add_resource("Prim's and Kruskal's Algorithm", "https://www.youtube.com/watch?v=lxOnvZPBzEc")
    mst.add_questions("Minimum Spanning Tree", [
        "What is a minimum spanning tree?",
        "What are Prim's and Kruskal's algorithms?"
    ])
    module5.add_child(mst)

    syllabus.add_child(module5)
    
    # Module 6: Hashing
    module6 = TreeNode("Module 6: Hashing", 4)
    hashing_methods = TreeNode("Hash functions and Open Hashing")
    hashing_methods.add_resource("Introduction to Hashing", "https://youtu.be/zeMa9sg-VJM?si=_nyBNPVn1v0Km3wS")
    hashing_methods.add_questions("Hash functions and Open Hashing", [
        "Find First Non-Repeating Character in a String",
        "Explain the concept of open hashing."
    ])
    module6.add_child(hashing_methods)
    
    syllabus.add_child(module6)
    
    # Module 7: Heaps and AVL Trees
    module7 = TreeNode("Module 7: Heaps and AVL Trees", 5)
    heaps = TreeNode("Heaps and Heap sort")
    heaps.add_resource("Heap Sort Algorithm", "https://www.youtube.com/watch?v=XYZ678")
    heaps.add_questions("Heaps and Heap sort", [
        "Kth Largest Element in an Array using Heap Sort",
        "Merge K Sorted Lists"
    ])
    module7.add_child(heaps)
    syllabus.add_child(module7)

    return syllabus
    
def build_digital_system_design_tree():
    # Root node: Digital System Design Syllabus
    syllabus = TreeNode("Digital System Design Syllabus")

    # Module 1: Boolean Algebra and Gate-Level Minimization
    module1 = TreeNode("Module 1: Boolean Algebra and Gate-Level Minimization", 8)
    boolean_algebra = TreeNode("Boolean Algebra: Basic definitions, Theorems, and Properties")
    boolean_algebra.add_resource("Boolean Algebra Fundamentals", "https://youtu.be/xyz123")  # Placeholder link
    boolean_algebra.add_questions("Boolean Algebra", [
        "What is Boolean Algebra and how is it used in digital systems?",
        "Explain the basic theorems and properties of Boolean Algebra."
    ])
    module1.add_child(boolean_algebra)

    gate_level_minimization = TreeNode("Gate-Level Minimization: K-map, NAND, NOR")
    gate_level_minimization.add_resource("K-map Simplification", "https://youtu.be/xyz456")  # Placeholder link
    gate_level_minimization.add_questions("Gate-Level Minimization", [
        "How does the K-map help in gate-level minimization?",
        "Explain the implementation of NAND and NOR gates in digital circuits."
    ])
    module1.add_child(gate_level_minimization)

    syllabus.add_child(module1)

    # Module 2: Verilog HDL
    module2 = TreeNode("Module 2: Verilog HDL", 5)
    verilog_hld = TreeNode("Verilog HDL: Lexical Conventions, Ports, and Modules")
    verilog_hld.add_resource("Verilog Syntax Overview", "https://youtu.be/xyz789")  # Placeholder link
    verilog_hld.add_questions("Verilog HDL", [
        "What are the basic lexical conventions in Verilog?",
        "How do you define ports and modules in Verilog?"
    ])
    module2.add_child(verilog_hld)

    operators_dataflow = TreeNode("Verilog: Operators, Dataflow Modelling, Gate Level Modelling")
    operators_dataflow.add_resource("Verilog Operators and Modelling", "https://youtu.be/xyz012")  # Placeholder link
    operators_dataflow.add_questions("Verilog Operators and Modelling", [
        "What are the different types of operators in Verilog?",
        "Explain dataflow and gate-level modelling in Verilog."
    ])
    module2.add_child(operators_dataflow)

    test_bench = TreeNode("Verilog: Test Bench")
    test_bench.add_resource("Test Bench in Verilog", "https://youtu.be/xyz345")  # Placeholder link
    test_bench.add_questions("Verilog: Test Bench", [
        "What is the purpose of a test bench in Verilog?",
        "How do you write a simple test bench for a digital circuit?"
    ])
    module2.add_child(test_bench)

    syllabus.add_child(module2)

    # Module 3: Design of Combinational Logic Circuits
    module3 = TreeNode("Module 3: Design of Combinational Logic Circuits", 8)
    half_full_adder = TreeNode("Half Adder, Full Adder, Half Subtractor, Full Subtractor")
    half_full_adder.add_resource("Adder and Subtractor Circuits", "https://youtu.be/xyz678")  # Placeholder link
    half_full_adder.add_questions("Half Full Adder", [
        "How does a full adder differ from a half adder?",
        "Explain the working of a half subtractor circuit."
    ])
    module3.add_child(half_full_adder)

    multiplexers_decoders = TreeNode("Decoders, Encoders, Multiplexers, and Demultiplexers")
    multiplexers_decoders.add_resource("Multiplexers and Decoders", "https://youtu.be/xyz901")  # Placeholder link
    multiplexers_decoders.add_questions("Decoders, Encoders, Multiplexers", [
        "What is the difference between a decoder and a multiplexer?",
        "Explain how a demultiplexer is used in digital circuits."
    ])
    module3.add_child(multiplexers_decoders)

    syllabus.add_child(module3)

    # Module 4: Design of Data Path Circuits
    module4 = TreeNode("Module 4: Design of Data Path Circuits", 6)
    parallel_adder_subtractor = TreeNode("N-bit Parallel Adder/Subtractor and Carry Look-Ahead Adder")
    parallel_adder_subtractor.add_resource("Carry Look-Ahead Adder Design", "https://youtu.be/xyz234")  # Placeholder link
    parallel_adder_subtractor.add_questions("Parallel Adder/Subtractor", [
        "What is the advantage of a carry look-ahead adder over a ripple carry adder?",
        "Explain how an N-bit parallel adder works."
    ])
    module4.add_child(parallel_adder_subtractor)

    multiplier = TreeNode("Unsigned Array Multiplier, Booth Multiplier")
    multiplier.add_resource("Booth Multiplier Explanation", "https://youtu.be/xyz567")  # Placeholder link
    multiplier.add_questions("Multiplier Circuits", [
        "What is Booth’s algorithm and how does it improve multiplication?",
        "How does an unsigned array multiplier work?"
    ])
    module4.add_child(multiplier)

    syllabus.add_child(module4)

    # Module 5: Design of Sequential Logic Circuits
    module5 = TreeNode("Module 5: Design of Sequential Logic Circuits", 8)
    flip_flops = TreeNode("Latches, Flip-Flops (SR, D, JK, T), Shift Registers")
    flip_flops.add_resource("Flip-Flop Circuits Overview", "https://youtu.be/xyz890")  # Placeholder link
    flip_flops.add_questions("Flip Flops", [
        "What are the differences between SR, JK, and D flip-flops?",
        "How do shift registers function in digital systems?"
    ])
    module5.add_child(flip_flops)

    counters = TreeNode("Design of Counters: Modulo-n, Johnson, Ring, Up/Down")
    counters.add_resource("Digital Counter Design", "https://youtu.be/xyz012")  # Placeholder link
    counters.add_questions("Counters", [
        "Explain how a modulo-n counter works.",
        "What is a Johnson counter and how is it used?"
    ])
    module5.add_child(counters)

    syllabus.add_child(module5)

    # Module 6: Design of FSM
    module6 = TreeNode("Module 6: Design of FSM", 4)
    fsm = TreeNode("Finite State Machine: Mealy FSM and Moore FSM")
    fsm.add_resource("FSM Design Techniques", "https://youtu.be/xyz345")  # Placeholder link
    fsm.add_questions("FSM Design", [
        "What is the difference between a Mealy and a Moore FSM?",
        "Explain the steps involved in designing a FSM for sequence detection."
    ])
    module6.add_child(fsm)

    syllabus.add_child(module6)

    # Module 7: Programmable Logic Devices
    module7 = TreeNode("Module 7: Programmable Logic Devices", 4)
    plds = TreeNode("Types of PLDs: PLA, PAL, CPLD, FPGA")
    plds.add_resource("PLD Architecture", "https://youtu.be/xyz678")  # Placeholder link
    plds.add_questions("Programmable Logic Devices", [
        "What is the difference between PAL and FPGA?",
        "Explain the architecture of an FPGA."
    ])
    module7.add_child(plds)

    syllabus.add_child(module7)

    return syllabus
    
def build_complex_tree():
    # Root node: Complex Analysis and Linear Algebra
    complex_syllabus = TreeNode("Complex Analysis and Linear Algebra Syllabus")

    # Module 1: Analytic Functions
    module1 = TreeNode("Module 1: Analytic Functions", 7)
    analytic_functions = TreeNode("Complex variable - Analytic functions and Cauchy - Riemann equations")
    analytic_functions.add_resource("Analytic Functions and Cauchy-Riemann Equations", "https://placeholder.com")
    analytic_functions.add_questions("Analytic Functions", [
        "What are the Cauchy-Riemann equations?",
        "How do you prove that a function is analytic?"
    ])
    module1.add_child(analytic_functions)

    laplace_equation = TreeNode("Laplace equation and Harmonic functions")
    laplace_equation.add_resource("Laplace Equation and Harmonic Functions", "https://placeholder.com")
    laplace_equation.add_questions("Laplace Equation", [
        "Explain the Laplace equation in the context of complex analysis.",
        "What are harmonic functions?"
    ])
    module1.add_child(laplace_equation)

    fluid_flow = TreeNode("Applications of analytic functions to fluid-flow and electric field problems")
    fluid_flow.add_resource("Applications in Fluid Flow and Electric Fields", "https://placeholder.com")
    fluid_flow.add_questions("Applications of Analytic Functions", [
        "How are analytic functions used in fluid dynamics?",
        "Explain the application of analytic functions in electric field problems."
    ])
    module1.add_child(fluid_flow)

    complex_syllabus.add_child(module1)

    # Module 2: Conformal and Bilinear transformations
    module2 = TreeNode("Module 2: Conformal and Bilinear transformations", 7)
    conformal_mapping = TreeNode("Conformal mapping - Elementary transformations")
    conformal_mapping.add_resource("Conformal Mapping and Transformations", "https://placeholder.com")
    conformal_mapping.add_questions("Conformal Mapping", [
        "What is the significance of conformal mappings in complex analysis?",
        "Explain the transformation of shapes using elementary transformations like rotation and magnification."
    ])
    module2.add_child(conformal_mapping)

    bilinear_transformation = TreeNode("Bilinear transformation and Cross-ratio")
    bilinear_transformation.add_resource("Bilinear Transformation and Cross-ratio", "https://placeholder.com")
    bilinear_transformation.add_questions("Bilinear Transformation", [
        "What is the Cross-ratio in the context of bilinear transformations?",
        "How are regions bounded by straight lines transformed in bilinear transformations?"
    ])
    module2.add_child(bilinear_transformation)

    complex_syllabus.add_child(module2)

    # Module 3: Complex Integration
    module3 = TreeNode("Module 3: Complex Integration", 7)
    power_series = TreeNode("Functions given by Power Series - Taylor and Laurent series")
    power_series.add_resource("Power Series and Complex Functions", "https://placeholder.com")
    power_series.add_questions("Power Series", [
        "What are the differences between Taylor and Laurent series?",
        "How do you identify singularities in a complex function?"
    ])
    module3.add_child(power_series)

    contour_integral = TreeNode("Integration of a complex function along a contour")
    contour_integral.add_resource("Complex Integration along Contours", "https://placeholder.com")
    contour_integral.add_questions("Complex Integration", [
        "What is Cauchy's integral theorem?",
        "Explain the significance of Cauchy's residue theorem in complex integration."
    ])
    module3.add_child(contour_integral)

    complex_syllabus.add_child(module3)

    # Module 4: Vector Spaces
    module4 = TreeNode("Module 4: Vector Spaces", 6)
    vector_space = TreeNode("Vector space - subspace, linear combination, span")
    vector_space.add_resource("Introduction to Vector Spaces", "https://placeholder.com")
    vector_space.add_questions("Vector Spaces", [
        "What is the definition of a vector space?",
        "Explain the concept of a basis in a vector space."
    ])
    module4.add_child(vector_space)

    linear_dependence = TreeNode("Linearly dependent - Independent - bases; Dimensions")
    linear_dependence.add_resource("Linear Dependence and Dimensions", "https://placeholder.com")
    linear_dependence.add_questions("Linear Dependence", [
        "What does it mean for a set of vectors to be linearly independent?",
        "How do you find the dimension of a vector space?"
    ])
    module4.add_child(linear_dependence)

    complex_syllabus.add_child(module4)

    # Module 5: Linear Transformations
    module5 = TreeNode("Module 5: Linear Transformations", 6)
    linear_transformations = TreeNode("Linear transformations - Basic properties; Invertible transformations")
    linear_transformations.add_resource("Linear Transformations and Properties", "https://placeholder.com")
    linear_transformations.add_questions("Linear Transformations", [
        "What is the significance of an invertible linear transformation?",
        "Explain the matrix representation of a linear transformation."
    ])
    module5.add_child(linear_transformations)

    complex_syllabus.add_child(module5)

    # Module 6: Inner Product Spaces
    module6 = TreeNode("Module 6: Inner Product Spaces", 5)
    inner_product = TreeNode("Dot products and inner products; Lengths and angles of vectors")
    inner_product.add_resource("Inner Products and Vector Lengths", "https://placeholder.com")
    inner_product.add_questions("Inner Products", [
        "How do you calculate the length of a vector using an inner product?",
        "Explain the concept of orthogonalization in inner product spaces."
    ])
    module6.add_child(inner_product)

    complex_syllabus.add_child(module6)

    # Module 7: Matrices and System of Equations
    module7 = TreeNode("Module 7: Matrices and System of Equations", 5)
    eigenvalues = TreeNode("Eigenvalues and Eigenvectors; Properties of Eigenvalues")
    eigenvalues.add_resource("Eigenvalues and Eigenvectors Explained", "https://placeholder.com")
    eigenvalues.add_questions("Eigenvalues", [
        "What is the significance of eigenvalues and eigenvectors?",
        "Explain the Cayley-Hamilton theorem."
    ])
    module7.add_child(eigenvalues)

    gaussian_elimination = TreeNode("System of linear equations; Gaussian elimination")
    gaussian_elimination.add_resource("Solving Linear Equations with Gaussian Elimination", "https://placeholder.com")
    gaussian_elimination.add_questions("Gaussian Elimination", [
        "Explain the Gaussian elimination method for solving linear equations.",
        "How is the Gauss-Jordan method different from Gaussian elimination?"
    ])
    module7.add_child(gaussian_elimination)

    complex_syllabus.add_child(module7)

    return complex_syllabus


def build_math_logic_graph_tree():
    # Root node: Mathematical Logic and Graph Theory
    math_logic_graph_syllabus = TreeNode("Mathematical Logic and Graph Theory Syllabus")

    # Module 1: Mathematical Logic
    module1 = TreeNode("Module 1: Mathematical Logic", 7)
    
    statements = TreeNode("Statements and Notation - Connectives, Tautologies, Equivalence")
    statements.add_resource("Statements, Notation, and Connectives", "https://placeholder.com")
    statements.add_questions("Statements and Connectives", [
        "What are the basic connectives in logic?",
        "Explain the concept of tautologies and equivalence in logical expressions."
    ])
    module1.add_child(statements)
    
    predicate_calculus = TreeNode("Predicate Calculus - Inference Theory")
    predicate_calculus.add_resource("Predicate Calculus and Inference Theory", "https://placeholder.com")
    predicate_calculus.add_questions("Predicate Calculus", [
        "What is the difference between propositional and predicate calculus?",
        "Explain the inference theory for predicate calculus."
    ])
    module1.add_child(predicate_calculus)

    math_logic_graph_syllabus.add_child(module1)

    # Module 2: Algebraic Structures
    module2 = TreeNode("Module 2: Algebraic Structures", 6)
    
    semigroups = TreeNode("Semigroups and Monoids, Groups and Subgroups")
    semigroups.add_resource("Semigroups, Monoids, and Groups", "https://placeholder.com")
    semigroups.add_questions("Semigroups and Groups", [
        "What are the properties of a semigroup?",
        "Explain Lagrange's Theorem for groups."
    ])
    module2.add_child(semigroups)
    
    homomorphism = TreeNode("Homomorphism and Group Codes")
    homomorphism.add_resource("Homomorphism and Group Codes", "https://placeholder.com")
    homomorphism.add_questions("Homomorphism", [
        "What is the concept of homomorphism in group theory?",
        "Explain group codes in the context of algebraic structures."
    ])
    module2.add_child(homomorphism)

    math_logic_graph_syllabus.add_child(module2)

    # Module 3: Counting Techniques
    module3 = TreeNode("Module 3: Counting Techniques", 6)
    
    pigeonhole = TreeNode("Pigeonhole Principle, Permutations, and Combinations")
    pigeonhole.add_resource("Counting Principles: Pigeonhole, Permutations, and Combinations", "https://placeholder.com")
    pigeonhole.add_questions("Pigeonhole Principle", [
        "What is the pigeonhole principle?",
        "Explain the difference between permutations and combinations."
    ])
    module3.add_child(pigeonhole)
    
    recurrence_relations = TreeNode("Recurrence Relations and Generating Functions")
    recurrence_relations.add_resource("Recurrence Relations and Solutions", "https://placeholder.com")
    recurrence_relations.add_questions("Recurrence Relations", [
        "How do you solve recurrence relations?",
        "Explain the use of generating functions in recurrence relations."
    ])
    module3.add_child(recurrence_relations)

    math_logic_graph_syllabus.add_child(module3)

    # Module 4: Lattices and Boolean Algebra
    module4 = TreeNode("Module 4: Lattices and Boolean Algebra", 6)
    
    lattices = TreeNode("Lattices as Posets, Hasse Diagram, Properties of Lattices")
    lattices.add_resource("Lattices and their Properties", "https://placeholder.com")
    lattices.add_questions("Lattices", [
        "What are partially ordered relations?",
        "Explain the Hasse diagram and its role in lattice theory."
    ])
    module4.add_child(lattices)
    
    boolean_algebra = TreeNode("Boolean Algebra and Boolean Functions")
    boolean_algebra.add_resource("Introduction to Boolean Algebra", "https://placeholder.com")
    boolean_algebra.add_questions("Boolean Algebra", [
        "What are the key properties of Boolean algebra?",
        "How do you simplify Boolean functions?"
    ])
    module4.add_child(boolean_algebra)

    math_logic_graph_syllabus.add_child(module4)

    # Module 5: Fundamentals of Graphs
    module5 = TreeNode("Module 5: Fundamentals of Graphs", 6)
    
    graph_basics = TreeNode("Basic Concepts of Graph Theory")
    graph_basics.add_resource("Introduction to Graph Theory", "https://placeholder.com")
    graph_basics.add_questions("Graph Basics", [
        "What are the fundamental concepts in graph theory?",
        "Explain the difference between a planar and complete graph."
    ])
    module5.add_child(graph_basics)
    
    graph_algorithms = TreeNode("Graph Isomorphism, Connectivity, Cut sets")
    graph_algorithms.add_resource("Graph Algorithms and Connectivity", "https://placeholder.com")
    graph_algorithms.add_questions("Graph Algorithms", [
        "What is graph isomorphism?",
        "How do you find the shortest path in a graph?"
    ])
    module5.add_child(graph_algorithms)

    math_logic_graph_syllabus.add_child(module5)

    # Module 6: Trees, Fundamental Circuits, Cut Sets
    module6 = TreeNode("Module 6: Trees, Fundamental Circuits, Cut Sets", 6)
    
    tree_properties = TreeNode("Properties of Trees and Spanning Trees")
    tree_properties.add_resource("Tree Properties and Spanning Trees", "https://placeholder.com")
    tree_properties.add_questions("Tree Properties", [
        "What are the properties of trees in graph theory?",
        "Explain the concept of spanning trees and related algorithms."
    ])
    module6.add_child(tree_properties)
    
    fundamental_circuits = TreeNode("Fundamental Circuits and Cut-Sets")
    fundamental_circuits.add_resource("Fundamental Circuits and Cut-Sets in Graphs", "https://placeholder.com")
    fundamental_circuits.add_questions("Circuits and Cut-Sets", [
        "What are fundamental circuits in a graph?",
        "How do cut-sets help in graph connectivity?"
    ])
    module6.add_child(fundamental_circuits)

    math_logic_graph_syllabus.add_child(module6)

    # Module 7: Graph Coloring, Covering, Partitioning
    module7 = TreeNode("Module 7: Graph Coloring, Covering, Partitioning", 6)
    
    bipartite_graphs = TreeNode("Bipartite Graphs, Chromatic Number, Chromatic Polynomial")
    bipartite_graphs.add_resource("Graph Coloring and Chromatic Number", "https://placeholder.com")
    bipartite_graphs.add_questions("Graph Coloring", [
        "What is a bipartite graph?",
        "Explain the concept of the chromatic number and chromatic polynomial."
    ])
    module7.add_child(bipartite_graphs)
    
    matching_covering = TreeNode("Matching and Covering, Four Colour Problem")
    matching_covering.add_resource("Matching, Covering and the Four Colour Problem", "https://placeholder.com")
    matching_covering.add_questions("Matching and Covering", [
        "What is a matching in graph theory?",
        "Explain the Four Colour Problem and its significance in graph theory."
    ])
    module7.add_child(matching_covering)

    math_logic_graph_syllabus.add_child(module7)

    return math_logic_graph_syllabus

def display_menu(syllabus_list):
    """Display menu to choose and display specific syllabus."""
    print("Available Subjects:")
    for idx, syllabus in enumerate(syllabus_list, 1):
        print(f"{idx}. {syllabus.name}")

    user_input = input("\nEnter the number of the syllabus you want to explore: ")
    while not user_input.isdigit() or int(user_input) not in range(1, len(syllabus_list) + 1):
        user_input = input(f"Invalid input. Please enter a number between 1 and {len(syllabus_list)}: ")

    selected_syllabus = syllabus_list[int(user_input) - 1]
    display_next_module(selected_syllabus)

def display_next_module(syllabus):
    """Display the next module in the syllabus and track time."""
    modules = syllabus.children
    linked_list = LinkedList()  # Create a linked list to store module times

    for module in modules:
        print(f"\n--- {module.name} ---")
        for child in module.children:
            child.display_tree()

        start_time = time.time()  # Start time for the module
        start_time_str = time.strftime("%H:%M:%S", time.gmtime(start_time))  # Convert start time to HH:MM:SS
        print(f"Module started at: {start_time_str}")

        user_input = input("Do you want to answer questions related to this module? (type 'questions' to answer, 'completed' to move to the next module): ")
        
        while user_input.lower() not in ["questions", "completed"]:
            user_input = input("Invalid input. Type 'questions' to answer, 'completed' to move to the next module: ")

        if user_input.lower() == "questions":
            # Generate questions based on the module/topic
            for child in module.children:
                if child.name in child.questions_map:
                    print(f"\nQuestions for {child.name}:")
                    for question in child.questions_map[child.name]:
                        print(f"  - {question}")
            input("\nPress Enter to continue to the next module...")

        end_time = time.time()  # End time for the module
        end_time_str = time.strftime("%H:%M:%S", time.gmtime(end_time))  # Convert end time to HH:MM:SS
        print(f"Module ended at: {end_time_str}")

        # Calculate time spent on this module and add to total time
        module_time = end_time - start_time
        linked_list.append(module_time)  # Store the module time in the linked list

    # Print the times for all modules and the total time
    linked_list.print_times()

   
# Example usage:
syllabus1 = build_DSA_syllabus_tree()
syllabus2 = build_complex_tree()
syllabus3 = build_digital_system_design_tree()
syllabus4 = build_math_logic_graph_tree()

# Change the name for all four lessons
syllabus1.name = "Data Structures and Algorithms"
syllabus2.name = "Complex variables and Linear Algebra"
syllabus3.name = "Digital System and Design"
syllabus4.name = "Discrete Mathematics"

syllabus_list = [syllabus1, syllabus2, syllabus3, syllabus4]

# Display the menu
display_menu(syllabus_list)
