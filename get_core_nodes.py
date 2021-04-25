import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv

# get core nodes of the network

# graph_path = 'dataset/soc-sign-bitcoinotc.csv'

def get_core_nodes (graph_path):
    df = pd.read_csv(graph_path, usecols=[0,1,2], names=['source', 'target', 'rate'])
    
    # print(df)
    G = nx.from_pandas_edgelist(df)

    # print(nx.info(G))
    algorithm = cpnet.KM_config()
    algorithm.detect(G)
    c = algorithm.get_pair_id()
    x = algorithm.get_coreness()
    core_nodes = []

    result = {}
    for key, value in sorted(c.items(), key=lambda x: x[1]):
        if(x[key] == 1):
            core_nodes.append(key)

    
    # add up two dict
    for k1,v1 in c.items():
        for k2,v2 in x.items():
            if k1 == k2:
                result[k1] = [v1,v2]

    # print(result.items())


    # number of core nodes
    print("Number of core nodes: ", len(core_nodes)) 

    # write the output coreness file
    # with open('result/bitcoin/bitcoinotc_coreness.csv', 'w', newline ='') as f:
    #     writer = csv.writer(f)
    #     header = ['Node ID', 'Pair ID', 'Coreness']
    #     writer.writerow(header)
    #     # writer.writerows(result.items())
    #     for key, values in result.items():
    #         writer.writerow([key, values[0], values[1]])

    return core_nodes

# get_core_nodes (graph_path)