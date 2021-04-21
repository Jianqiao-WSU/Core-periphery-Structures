import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time.csv', sep=',', names=['from', 'to', 'rate'], index_col=0)  # load data from dataset
#df = pd.read_csv('C:/Users/ASUS/Desktop/project/Core-periphery-Structures/dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1], names=['source', 'target'])
df = pd.read_csv('dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1], names=['source', 'target'])
print(df)
# df=nx.from_pandas_adjacency(df)
G = nx.from_pandas_edgelist(df)
# print(G)

# read E-R random graph
n=40
p=10
g = nx.erdos_renyi_graph(n, p, seed=None, directed=False)


algorithm = cpnet.KM_config()
algorithm.detect(G)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

algorithm.detect(g)
b = algorithm.get_pair_id()
y = algorithm.get_coreness()

# print(c)
print('Name\tPairID\tCoreness')
for key, value in sorted(c.items(), key=lambda x: x[1]):
    print('%s\t%d\t%f' %(key, c[key], x[key]))
print (y)

# fig = plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax, pos = cpnet.draw(G, c, x, ax)
# ax, _ = cpnet.draw(G, c, x, ax, pos=pos)
# nx.draw_networkx_labels(G, pos)

# plt.show()