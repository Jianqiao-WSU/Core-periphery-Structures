import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv

# transform the format of the graph, add weight to edge

def transform_graph (graph_path):
    G = nx.DiGraph()
    for d in pd.read_csv(graph_path,sep=',', header=None, names=['source', 'target', 'Weight'], chunksize=100):
        G.add_weighted_edges_from([tuple(x) for x in d.values])
    # G.to_csv('result/soc-sign-bitcoinotc1111.csv')
    # print(111)
    return G

