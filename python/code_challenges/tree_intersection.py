from data_structures.binary_tree import BinaryTree

def tree_intersection(tree_a, tree_b):
    same_nums = set()
    tree_a_keys = {}
    tree_a_values = BinaryTree.pre_order(tree_a)
    tree_b_values = BinaryTree.pre_order(tree_b)

    for a_val in tree_a_values:
        tree_a_keys[a_val] = None
    for b_val in tree_b_values:
        if b_val in tree_a_keys:
            same_nums.add(b_val)

    return list(same_nums)
