# evaluation.py

def evaluate_thought(thought):
    """
    Evaluates the quality of a thought. This can be customized based on specific criteria.
    For demonstration, we'll just return the length of the response.
    """
    return len(thought.response)


def find_best_thought(tree):
    """
    Traverses the tree to find the thought with the highest evaluation score.
    """
    best = tree
    stack = [tree]

    while stack:
        current = stack.pop()
        if evaluate_thought(current) > evaluate_thought(best):
            best = current
        stack.extend(current.children)

    return best