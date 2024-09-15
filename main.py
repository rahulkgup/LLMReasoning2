# main.py
from thought import generate_thought
from evaluation import find_best_thought
from utils import print_tree

def print_hi(name):
    """
    Main function to execute the Tree-of-Thought approach.
    """
    print(f'Hi, {name}')

    initial_prompt = "Write a haiku about AI and explore its implications."
    print("DEBUG: Starting to generate thought tree...")
    thought_tree = generate_thought(initial_prompt, max_depth=2)
    print("DEBUG: Thought tree generated.")

    print("\nGenerated Tree of Thoughts:")
    print_tree(thought_tree)
    print("DEBUG: Printed the thought tree.")

    # Pass both 'thought_tree' and 'initial_prompt' to the function
    best_thought = find_best_thought(thought_tree, initial_prompt)
    print("DEBUG: Found the best thought.")

    print("\nBest Thought:")
    print(f"Prompt: {best_thought.prompt}")
    print(f"Response: {best_thought.response}")

if __name__ == '__main__':
    print_hi('PyCharm')