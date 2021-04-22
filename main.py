import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv
import transform_graph
import get_core_nodes

# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time.csv', sep=',', names=['from', 'to', 'rate'], index_col=0)  # load data from dataset
# df = pd.read_csv('C:/Users/ASUS/Desktop/project/Core-periphery-Structures/dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1], names=['source', 'target'])


graph_path = 'dataset/soc-sign-bitcoinotc-with-no-time.csv'

G = transform_graph.trasform_graph(graph_path)

core_nodes = get_core_nodes.get_core_nodes(graph_path)



# print(G.get_edge_data(edge[1]))

# for u, v, w in G.edges(data=True):
#     print(u, v, w['weight'])

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