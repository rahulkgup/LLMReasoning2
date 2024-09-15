# main.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from thought import generate_thought
from evaluation import find_best_thought
from utils import print_tree

# Load the OpenAI API key from the .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_thoughts(prompt, constraints="", max_depth=3, thoughts_per_node=2):
    """
    Generates a thought tree based on the prompt and constraints using OpenAI's API.

    Args:
        prompt (str): The initial prompt to start generating thoughts.
        constraints (str): Any constraints to guide the thought generation.
        max_depth (int): The maximum depth of the thought tree.
        thoughts_per_node (int): The number of thoughts to generate per node.

    Returns:
        dict: A tree structure representing the generated thoughts.
    """
    # Initialize the tree with the initial prompt
    thoughts_tree = {"content": prompt, "children": []}

    def expand_node(node, depth):
        if depth >= max_depth:
            return

        # Construct the messages for OpenAI ChatCompletion
        messages = [
            {"role": "system", "content": f"Constraints: {constraints}"},
            {"role": "user", "content": node['content']}
        ]

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" or another supported model
                messages=messages,
                max_tokens=150,  # Adjust as needed
                n=thoughts_per_node,  # Number of thoughts per node
                temperature=0.7  # Adjust for creativity
            )

            # Process the responses
            thoughts = []
            for choice in response.choices:
                thought_content = choice.message.content.strip()
                if thought_content:
                    child_node = {"content": thought_content, "children": []}
                    thoughts.append(child_node)
                    expand_node(child_node, depth + 1)
            node["children"] = thoughts

        except Exception as e:
            # Handle API errors
            raise RuntimeError(f"An error occurred during OpenAI API call: {e}")

    expand_node(thoughts_tree, 0)
    return thoughts_tree

# Optional: Keep a main function for standalone testing
if __name__ == '__main__':
    initial_prompt = "Write a haiku about AI and explore its implications."
    constraints = ""
    print("DEBUG: Starting to generate thought tree...")
    thought_tree = generate_thoughts(initial_prompt, constraints, max_depth=2, thoughts_per_node=2)
    print("DEBUG: Thought tree generated.")

    print("\nGenerated Tree of Thoughts:")
    print_tree(thought_tree)
    print("DEBUG: Printed the thought tree.")

    # Find and print the best thought
    best_thought = find_best_thought(thought_tree, initial_prompt)
    print("DEBUG: Found the best thought.")

    print("\nBest Thought:")
    print(f"Prompt: {best_thought['content']}")
    # Since responses are plain text, no decoding is necessary