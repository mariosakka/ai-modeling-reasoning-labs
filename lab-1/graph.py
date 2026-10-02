import networkx as nx
import matplotlib.pyplot as plt

# we use a library for generaing directed graphs

G = nx.DiGraph()

# we can add edges with attributes like weight, reason and currency.
# these attributes can be used to store additional information about the edges between the specified nodes
# with the first two arguments being the nodes and the rest being the attributes of the edge
G.add_edge("Paul", "Diana", weight=30, reason="pizza", currency="RON", duedate="tomorrow")
G.add_edge("Diana", "Ralph", weight=50, reason="shopping")
G.add_edge("Ralph", "Paul", weight=40)


pos = nx.spring_layout(G)


# creates a directed graph with the specified nodes and edges, and draws it using matplotlib. The nodes are colored red, sized at 2500, 
# and arrows are shown to indicate directionality.
# Edge labels are also displayed to show the weights of the edges. Finally, the graph is displayed using plt.show().

nx.draw(G, pos, with_labels=True, node_color="red", node_size=2500, arrows=True) # with_labels means that nodes will be labeled, not edges

# easy way of getting the edge labels after we have defined the edges with all attributes, in this case the weights of the edges

edge_labels = nx.get_edge_attributes(G, "weight")  

# add edge labels to the graph, which will display the weights of the edges on the graph visualization
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Finally, we display the graph using plt.show(), which will render the graph in a window or inline if using a Jupyter notebook.
plt.show()