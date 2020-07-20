import json

def get_descendant(node):
    all_descendants = []
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        if current_node.children:
            for child in current_node.children:
                all_descendants.append(child.id)
                queue.append(child)

    return json.dumps({"descendants": all_descendants})


def change_parent(root, node_id, parent_id):
    found = 0
    parent = None
    node = None
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        if cur_node.id == node_id:
            node = cur_node
            found += 1

        if cur_node.id == parent_id:
            parent = cur_node
            found += 1

        if found == 2:
            break

        if cur_node.children:
            for child in cur_node.children:
                queue.append(child)

    # remove the node from its old parent
    node.parent.children.remove(node)
    # add the node to the new parent
    parent.children.append(node)
    # change the node parent, height and root
    node.parent = parent
    node.height = parent.height + 1
    node.root = parent.root
    get_descendant(node)

    return root