import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time.csv', sep=',', names=['from', 'to', 'rate'], index_col=0)  # load data from dataset
df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time and rate.csv', sep=',',usecols=[0,1], names=['source', 'target'])
print(df)
# df=nx.from_pandas_adjacency(df)
G = nx.from_pandas_edgelist(df)
print(G)
algorithm = cpnet.KM_config()
algorithm.detect(G)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

# print(c)

print('Name\tPairID\tCoreness')
for key, value in sorted(c.items(), key=lambda x: x[1]):
    print('%s\t%d\t%f' %(key, c[key], x[key]))