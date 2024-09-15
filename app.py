import streamlit as st
from graphviz import Digraph
from main import generate_thoughts  # Import the function from main.py

def display_thoughts(node, depth=0):
    """
    Recursively displays the thoughts in the Streamlit app without nesting expanders.
    """
    if node:
        st.write("  " * depth + "- " + node["content"])
        if node.get("children"):
            for child in node["children"]:
                display_thoughts(child, depth + 1)

def build_graph(node, graph, parent_id=None):
    """
    Recursively builds a graphviz Digraph from the thought tree.
    """
    node_id = str(id(node))
    graph.node(node_id, node["content"][:20]+"..." if len(node["content"]) > 20 else node["content"])
    if parent_id:
        graph.edge(parent_id, node_id)
    for child in node.get("children", []):
        build_graph(child, graph, node_id)

def main():
    st.title("Tree of Thought Application")
    st.write("Implementing the Tree of Thought approach using OpenAI's GPT models.")

    # User Inputs
    prompt = st.text_area("Enter your prompt:", "Write a haiku about AI and explore its implications.")
    constraints = st.text_area("Enter constraints (optional):", "")
    max_depth = st.slider("Select the maximum depth of the tree:", min_value=1, max_value=5, value=3)
    thoughts_per_node = st.slider("Select the number of thoughts per node:", min_value=1, max_value=5, value=2)

    # Generate Thoughts Button
    if st.button("Generate Thoughts"):
        if not prompt.strip():
            st.error("Please enter a valid prompt.")
        else:
            with st.spinner("Generating thoughts..."):
                try:
                    thoughts_tree = generate_thoughts(prompt, constraints, max_depth, thoughts_per_node)
                    st.success("Thought generation complete!")
                    
                    st.header("Generated Thoughts:")
                    display_thoughts(thoughts_tree)
                    
                    st.header("Thought Tree Visualization:")
                    graph = Digraph(format='png')
                    build_graph(thoughts_tree, graph)
                    st.graphviz_chart(graph.source)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()