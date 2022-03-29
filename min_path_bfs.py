"""
Let's say you have start node "dog" and you end node "cat" and set of nodes = ["dag", "nag", "cog", "cot", "bot", "cat"].

You've to find minimum distance from start node to end node. The only condition is, you can move to another node with only 1 letter diff. For ex, from "dog" you can go to "dag" or "cog" as both of these words have only 1 different char from "dog".

Find minimum required hop to reach at destination node. If it's not possible, return -1.
"""


import copy
import pdb

class Solution:

    def start(self, nodes, start_node, end_node):
        if start_node == end_node or len(nodes) == 0:
            return 0

        ccnodes = copy.copy(nodes)
        matched_nodes = [start_node]
        depth = 1
        selected_depth = -1
        pivot_node = start_node
        # pdb.set_trace()

        while len(matched_nodes) > 0 and len(ccnodes) > 0:
            ccnodes, matched_nodes = self.iterate_over(ccnodes, matched_nodes)
            # pdb.set_trace()
            if end_node in matched_nodes:
                selected_depth = depth
                break
            else:
                depth += 1

        return selected_depth


    def iterate_over(self, cnodes, pivot_nodes):
        ccnodes = []
        matched_nodes = []
        for node_value in cnodes:
            if self.compare_multiplenodes(node_value, pivot_nodes):
                matched_nodes.append(node_value)
            else:
                ccnodes.append(node_value)
        return ccnodes, matched_nodes
        

    def compare_multiplenodes(self, node_a, other_nodes):
        return any(self.compare_nodes(node_a, b) for b in other_nodes)


    def compare_nodes(self, node_a, node_b):
        diff_count = 0
        for i, val_a in enumerate(node_a):
            val_b = node_b[i]
            if val_a != val_b:
                diff_count += 1
            if diff_count > 1:
                return False
        return True


print Solution().start(["dog", "cog", "cag", "cat"], "dog", "cat")
print Solution().start(["dog", "cog", "cag", "cot", "cat"], "dog", "cat")
print Solution().start(["dog", "cog", "cot", "cat", "sat"], "dog", "sat")
print Solution().start(["dog", "cog", "cat"], "dog", "cat")
print Solution().start(["dog", "cot", "cat"], "cot", "cat")