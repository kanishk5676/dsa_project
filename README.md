# Data Structures and Algorithms Syllabus Tree

This repository contains a Python implementation of a Data Structures and Algorithms syllabus tree structure using an object-oriented approach. Each topic and subtopic is represented as a node in the tree, with information on duration, additional resources, and related questions.

## Project Structure

### `TreeNode` Class

The `TreeNode` class represents each node in the syllabus tree with the following attributes:
- `name`: Name of the topic, module, or subtopic.
- `hours`: Duration in hours (optional for each node).
- `resources`: A dictionary storing resources related to each topic (e.g., video links or articles).
- `children`: A list of child nodes (subtopics under a given topic).
- `questions_map`: A dictionary storing questions related to each topic.

### Key Methods
- `add_child(child_node)`: Adds a subtopic as a child node under the current topic.
- `add_resource(key, url)`: Adds a resource (key-value pair) for the topic, where the key is a short description, and the URL points to an online resource.
- `add_questions(topic, questions)`: Stores questions related to a specific topic.
- `display_tree(level=0)`: Recursively displays the tree structure with topics, resources, and questions.

### Main Functions
- `build_syllabus_tree()`: Constructs the syllabus tree for Data Structures and Algorithms, organizing it into modules and subtopics with relevant resources and questions.
- `generate_n_questions(n)`: Generates a set of `n` random questions from a predefined dataset of questions on topics such as Algorithm Analysis, Linear Data Structures, Trees, Graphs, and more.

### Example Usage

```python
# Build and display the syllabus tree
syllabus_tree = build_syllabus_tree()

# Generate and print 3 random questions from the dataset
generate_n_questions(3)
