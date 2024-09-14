# thought.py
from api import get_completion
from utils import extract_sub_prompts
import logging

logger = logging.getLogger(__name__)


class Thought:
    def __init__(self, prompt, response, children=None):
        self.prompt = prompt
        self.response = response
        self.children = children if children is not None else []


def generate_thought(prompt, max_depth=3, current_depth=0, max_sub_prompts=3):
    """
    Recursively generates thoughts branching out to a specified depth.

    Args:
        prompt (str): The current prompt to generate a response for.
        max_depth (int): The maximum depth of recursion.
        current_depth (int): The current depth in the recursion.
        max_sub_prompts (int): The maximum number of sub-prompts to generate per response.

    Returns:
        Thought: An instance of the Thought class representing the current node.
    """
    logger.debug(f"Generating thought for prompt: '{prompt}' at depth: {current_depth}")

    if current_depth >= max_depth:
        response = get_completion(prompt)
        logger.debug(f"Max depth reached. Response: '{response}'")
        return Thought(prompt, response)

    response = get_completion(prompt)
    logger.debug(f"Response: '{response}'")

    sub_prompts = extract_sub_prompts(response)
    logger.debug(f"Extracted sub-prompts: {sub_prompts}")

    # Limit the number of sub-prompts to prevent excessive branching
    sub_prompts = sub_prompts[:max_sub_prompts]

    children = []
    for sub_prompt in sub_prompts:
        # Increment current_depth by 1 for each recursive call
        child = generate_thought(sub_prompt, max_depth, current_depth + 1, max_sub_prompts)
        children.append(child)

    return Thought(prompt, response, children)