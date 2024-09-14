# utils.py

def extract_sub_prompts(response):
    """
    Parses the response to extract sub-prompts for further reasoning.
    This function should be tailored based on how you expect the responses to be formatted.
    For simplicity, let's assume each line is a new sub-prompt.
    """
    return [line.strip() for line in response.split('\n') if line.strip()]

def print_tree(thought, level=0):
    """
    Utility function to print the tree structure.
    """
    indent = "  " * level
    print(f"{indent}- Prompt: {thought.prompt}")
    print(f"{indent}  Response: {thought.response}")
    for child in thought.children:
        print_tree(child, level + 1)