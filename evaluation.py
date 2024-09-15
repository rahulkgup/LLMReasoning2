# evaluation.py
from sentence_transformers import SentenceTransformer, util
import logging

# Initialize the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose a different pre-trained model


def find_best_thought(tree, initial_prompt):
    """
    Traverses the tree to find the thought with the highest semantic similarity to the initial prompt.

    Args:
        tree (Thought): The root of the thought tree.
        initial_prompt (str): The initial prompt to evaluate relevance.

    Returns:
        Thought: The best thought based on evaluation criteria.
    """
    best = tree
    best_score = compute_similarity(initial_prompt, tree.response)
    stack = [tree]

    while stack:
        current = stack.pop()
        current_score = compute_similarity(initial_prompt, current.response)

        if current_score > best_score:
            best = current
            best_score = current_score

        stack.extend(current.children)

    return best


def compute_similarity(prompt, response):
    """
    Computes the semantic similarity between the prompt and the response.

    Args:
        prompt (str): The initial prompt.
        response (str): The response to evaluate.

    Returns:
        float: Similarity score between 0 and 1.
    """
    embeddings = model.encode([prompt, response], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    return similarity