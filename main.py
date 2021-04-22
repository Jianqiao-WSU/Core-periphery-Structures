import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv
import transform_graph
import get_core_nodes

# df = pd.read_csv('C:/Users/ASUS/Desktop/project/Core-periphery-Structures/dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1], names=['source', 'target'])


graph_path = 'dataset/soc-sign-bitcoinotc-with-no-time.csv'
# graph_path = 'dataset/soc-sign-bitcoinalpha-with-no-time.csv'

G = transform_graph.transform_graph(graph_path)

core_nodes = get_core_nodes.get_core_nodes(graph_path)

# print(core_nodes[1])

# print(G.edges(core_nodes, data=True))

core_edges = G.edges(core_nodes, data=True)

num_of_core_edges = len(core_edges)

edge_weight = 0

for u, v, w in core_edges:
    # print(w['weight'])
    edge_weight += w['weight']

print(edge_weight)

avg_weight = edge_weight/num_of_core_edges

print(avg_weight)


# file = open("result/bitcoinotc.csv", "w", newline='')  # make the result as a csv file
# # file.write('Name\tPairID\tCoreness\n')
# writer = csv.writer(file)
# writer.writerow(['Name', 'PairID', 'Coreness'])

# for key, value in sorted(c.items(), key=lambda x: x[1]):
#     # file.write('%s\t%d\t%f\n' %(key, c[key], x[key]))
#     i ={key, c[key], x[key]}
#     print(i)
#     writer.writerow(i)
# file.close()


# fig = plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax, pos = cpnet.draw(G, c, x, ax)
# ax, _ = cpnet.draw(G, c, x, ax, pos=pos)
# nx.draw_networkx_labels(G, pos)

# plt.show()