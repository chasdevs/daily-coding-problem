from days._20210118 import deserialize, serialize, Node

def test_serialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))

def test_main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    deser = deserialize(serialize(node))
    assert deser.left.left.val == 'left.left'