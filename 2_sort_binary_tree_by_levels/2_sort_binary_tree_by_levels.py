def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            result.append(current.left)

        if current.right is not None:
            result.append(current.right)

    return result