import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time.csv', sep=',', names=['from', 'to', 'rate'], index_col=0)  # load data from dataset
# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1,2], names=['source', 'target', 'rate'], index_col=False)
df = pd.read_csv('dataset/soc-sign-bitcoinotc.csv',usecols=[0,1,2], names=['source', 'target', 'rate'])
print(df)

# df=nx.from_pandas_adjacency(df)
G = nx.from_pandas_edgelist(df)
# print(G)
print(nx.info(G))


algorithm = cpnet.KM_config()
algorithm.detect(G)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

# print(c)

print('Name\tPairID\tCoreness')
for key, value in sorted(c.items(), key=lambda x: x[1]):
    print('%s\t%d\t%f' %(key, c[key], x[key]))

# file = open("bitcoinotc.txt", "w")  # make the result as a txt file
# file.write('Name\tPairID\tCoreness\n')

# for key, value in sorted(c.items(), key=lambda x: x[1]):
#     file.write('%s\t%d\t%f\n' %(key, c[key], x[key]))
# file.close()


# sig_c, sig_x, significant, p_values = cpnet.qstest(
#     c, x, G, algorithm, significance_level=0.05, num_of_rand_net=100, num_of_thread=16
# )

# pos = nx.spring_layout(
#     G, scale = 2
# )
# fig = plt.figure(figsize=(12, 12))
# ax = plt.gca()
# draw_nodes_kwd = {"node_size": 30, "linewidths": 0.3}
# ax, pos = cpnet.draw(
#     G,
#     sig_c,
#     sig_x,
#     ax,
#     draw_nodes_kwd=draw_nodes_kwd,
#     max_colored_group_num=5,
#     draw_edge=False,
#     layout_kwd = {"verbose":True, "iterations":500}
# )


# fig = plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax, pos = cpnet.draw(G, c, x, ax)
# ax, _ = cpnet.draw(G, c, x, ax, pos=pos)
# nx.draw_networkx_labels(G, pos)

# plt.show()