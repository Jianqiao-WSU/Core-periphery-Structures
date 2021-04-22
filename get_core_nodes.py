import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv


def get_core_nodes (graph_path):
    df = pd.read_csv('dataset/soc-sign-bitcoinotc.csv',usecols=[0,1,2], names=['source', 'target', 'rate'])
    
    # print(df)
    G = nx.from_pandas_edgelist(df)

    # print(nx.info(G))
    algorithm = cpnet.KM_config()
    algorithm.detect(G)
    c = algorithm.get_pair_id()
    x = algorithm.get_coreness()
    core_nodes = []

    # print('Name\tPairID\tCoreness')
    for key, value in sorted(c.items(), key=lambda x: x[1]):
        
        if(x[key] == 1):
            # print('%s\t%d\t%f' %(key, c[key], x[key]))
            core_nodes.append(key)
    # print(core_nodes)

    print(len(core_nodes)) #number of core nodes

    # print(G.edges(core_nodes[1]))
    # edge = G.edges(core_nodes[1])
    # print(list(G.edges(data=True))[0])
    return core_nodes