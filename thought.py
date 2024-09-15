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


def generate_thought(prompt, max_depth=3, current_depth=0):
    """
    Recursively generates thoughts branching out to a specified depth.
    """
    logger.debug(f"Generating thought for prompt: '{prompt}' at depth: {current_depth}")

    if current_depth >= max_depth:
        response = get_completion(prompt)
        logger.debug(f"Max depth reached. Response: {response}")
        return Thought(prompt, response)

    response = get_completion(prompt)

    if response.startswith("Error:"):
        logger.error(f"API Error encountered: {response}")
        # Do not generate sub-prompts on error
        return Thought(prompt, response)

    sub_prompts = extract_sub_prompts(response)
    logger.debug(f"Extracted sub-prompts: {sub_prompts}")

    children = []
    for sub_prompt in sub_prompts:
        child = generate_thought(sub_prompt, max_depth, current_depth + 1)  # Incremented depth
        children.append(child)

    return Thought(prompt, response, children)