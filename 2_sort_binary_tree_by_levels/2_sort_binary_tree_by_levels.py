def tree_by_levels(node):
    if node is None:
        return False

    result = []
    queue = [node]

    while queue is not None:
        current = queue.pop(0)
        result.append(current)

        if current.left is not None:
            result.append(current)

        if current.right is not None:
            result.append(current)

    return result