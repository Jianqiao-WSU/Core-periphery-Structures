import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


df = pd.read_csv('dataset/soc-sign-bitcoinotc.csv', sep=',', names=['from', 'to', 'rate'])  # load data from dataset
# print(df)
df=nx.from_pandas_adjacency(df)
G = nx.from_pandas_edgelist(df)

# print(G)
M = nx.erdos_renyi_graph(80, 0.1)
# L = nx.karate_club_graph()



algorithm = cpnet.KM_config()
# algorithm.detect(L)
# c = algorithm.get_pair_id()
# x = algorithm.get_coreness()

# print(c)

# G = nx.karate_club_graph()

c = algorithm.get_pair_id()
x = algorithm.get_coreness()

print(c)