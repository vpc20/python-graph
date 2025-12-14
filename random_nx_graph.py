import networkx as nx
import matplotlib.pyplot as plt
import random


def generate_random_graph(n, p):
    """
    Generates a random graph using the Erdos-Renyi model and plots it.

    :param n: Number of nodes.
    :param p: Probability of edge creation.
    """
    # Generate a random graph using the Erdos-Renyi model
    G = nx.erdos_renyi_graph(n, p)

    # Check if the graph is connected and regenerate if necessary (optional)
    while not nx.is_connected(G) and p < 1.0:
        print("Generated graph is not connected. Regenerating...")
        G = nx.erdos_renyi_graph(n, p)

    print(f"Generated a graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15)
    plt.title(f"Random Graph (n={n}, p={p})")
    plt.show()  # Display the plot


def generate_random_directed_graph(n, p):
    """
    Generates a random graph using the Erdos-Renyi model and plots it.

    :param n: Number of nodes.
    :param p: Probability of edge creation.
    """
    # Generate a random graph using the Erdos-Renyi model
    G = nx.erdos_renyi_graph(n, p, directed=True)

    # Check if the graph is connected and regenerate if necessary (optional)
    # while not nx.is_connected(G) and p < 1.0:
    #     print("Generated graph is not connected. Regenerating...")
    #     G = nx.erdos_renyi_graph(n, p)

    print(f"Generated a graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15)
    plt.title(f"Random Graph (n={n}, p={p})")
    plt.show()  # Display the plot


def generate_random_dag(num_nodes, prob_edge):
    """
    Generates a random DAG using a topological sort approach.
    Edges are added only from lower indexed nodes to higher indexed nodes.
    """
    DAG = nx.DiGraph()
    # Add nodes
    DAG.add_nodes_from(range(num_nodes))

    # Add edges randomly, ensuring no cycles
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            if random.random() < prob_edge:
                DAG.add_edge(u, v)

    # Visualize the graph
    # Using 'layered' layout for better visualization of the DAG structure
    # pos = nx.planar_layout(DAG)  # or nx.spring_layout(DAG), nx.circular_layout(DAG), etc.
    pos = nx.spring_layout(DAG)  # or nx.spring_layout(DAG), nx.circular_layout(DAG), etc.
    nx.draw(DAG, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', arrows=True, font_size=15)
    plt.show()

    # return G


# --- Example Usage ---
# Define parameters
num_nodes = 7
edge_probability = 0.3
# edge_probability = 0.5

# Run the function
if __name__ == "__main__":
    # generate_random_graph(num_nodes, edge_probability)
    generate_random_directed_graph(num_nodes, edge_probability)
    # generate_random_dag(num_nodes, edge_probability)
