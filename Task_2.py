class TreeSearch:
    def __init__(self):
        self.parents = []
        self.children = []

    # Tree mein nodes add karna
    def add_node(self, parent_node, child_node):
        child_node = child_node.strip()

        if parent_node in self.parents:
            idx = self.parents.index(parent_node)
            if child_node:
                self.children[idx].append(child_node)
        else:
            self.parents.append(parent_node)
            self.children.append([child_node] if child_node else [])

    # DFS search method
    def dfs_find_goal(self, start_node, goal_node):

        if start_node not in self.parents:
            print("Error: Start node not found in tree.")
            return

        visited = []
        stack = []
        traversal_path = []

        stack.append(start_node)

        while len(stack) > 0:
            current = stack.pop()

            if current not in visited:
                visited.append(current)
                traversal_path.append(current)

                print("Visiting:", current)

                # Goal node check
                if current == goal_node:
                    print("Goal node found!")
                    path_str = " -> ".join(traversal_path)
                    print("Traversal Path:", path_str)
                    return traversal_path

                # Current node ke children find karna
                neighbors = []

                for i in range(len(self.parents)):
                    if self.parents[i] == current:
                        neighbors = self.children[i]
                        break

                # Children ko stack mein add karna
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print("Goal node not found.")


# Execution
search = TreeSearch()

search.add_node('A', 'B')
search.add_node('A', 'F')
search.add_node('A', 'D')
search.add_node('A', 'E')

search.add_node('B', 'K')
search.add_node('B', 'J')

search.add_node('F', ' ')
search.add_node('D', 'G')

search.add_node('E', 'C')
search.add_node('E', 'H')
search.add_node('E', 'I')

search.add_node('K', 'N')
search.add_node('K', 'M')

search.add_node('J', '')
search.add_node('G', '')
search.add_node('C', '')
search.add_node('H', '')
search.add_node('I', 'L')
search.add_node('N', '')
search.add_node('M', '')
search.add_node('L', '')

# DFS search
search.dfs_find_goal('A', 'G')