import json


def main():
    print("bob")

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        obj = {"val": self.val}
        if self.left is not None:
            obj["left"] = self.left.serialize()
        if self.right is not None:
            obj["right"] = self.right.serialize()
        return json.dumps(obj)

def serialize(root):
    """
    Serialize the tree into a string

    Example input:
              Node("bob")
    Node("sally")   Node("jeff")

    Example output:
    {val: "bob", left: {val: "sally"}, right: {val: "jeff"}
    """
    return root.serialize()



def deserialize(s):
    """Deserialize the string into a tree1"""
    obj = json.loads(s)

    deseralized = Node(
        obj["val"],
        deserialize(obj["left"]) if "left" in obj else None,
        deserialize(obj["right"]) if "right" in obj else None
    )

    return deseralized


if __name__ == 'main':
    main()
