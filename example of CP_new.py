import cpnet
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

# alg = cpnet.BE() # Load the Borgatti-Everett algorithm
# alg = cpnet.MINRES()
# alg.detect(G)
kmconfig = cpnet.KM_config()
kmconfig.detect(G)
c = kmconfig.get_pair_id()
x = kmconfig.get_coreness()

# Printing node ID and group ID.
print("{:<10} {:<10}".format('Node_ID', 'Group ID'))

for key, value in c.items():
    print("{:<10} {:<10}".format(key, value))

print("\n")
#Printing node ID and Coreness.
print("{:<10} {:<10}".format('Node_ID', 'Coreness'))

for key, value in x.items():
    print("{:<10} {:<10}".format(key, value))
    
print(nx.info(G))

fig = plt.figure(figsize=(8, 6))
ax = plt.gca()
ax, pos = cpnet.draw(G, c, x, ax)
ax, _ = cpnet.draw(G, c, x, ax, pos=pos)
nx.draw_networkx_labels(G, pos)

plt.show()