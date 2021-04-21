import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


# read E-R random graph
n=40
p=10
g = nx.erdos_renyi_graph(n, p, seed=None, directed=False)

algorithm = cpnet.KM_config()
algorithm.detect(g)
b = algorithm.get_pair_id()
y = algorithm.get_coreness()

print (y)