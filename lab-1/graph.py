import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge("Paul", "Diana", weight=30, reason="pizza", currency="RON", duedate="tomorrow")
G.add_edge("Diana", "Ralph", weight=50, reason="shopping")
G.add_edge("Ralph", "Paul", weight=40)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color="red", node_size=2500, arrows=True)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()