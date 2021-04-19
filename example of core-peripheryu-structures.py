import cpnet
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
G = nx.karate_club_graph()
alg = cpnet.BE() # Load the Borgatti-Everett algorithm
alg.detect(G) # Give the network as an input
x = alg.get_coreness()  # Get the coreness of nodes
c = alg.get_pair_id()  # Get the group membership of nodes
print(x)
fig = plt.figure(figsize=(8, 6))
ax = plt.gca()
ax, pos = cpnet.draw(G, c, x, ax)
plt.show()