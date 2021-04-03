from days._20210123 import num_unival_subtrees, Node

def test_num_unival_subtrees():
    #    0
    #   / \
    #  1   0
    #     / \
    #    1   0
    #   / \
    #  1   1
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert num_unival_subtrees(tree) == 5