import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv

# df = pd.read_csv('dataset/soc-sign-bitcoinotc-with no time.csv', sep=',', names=['from', 'to', 'rate'], index_col=0)  # load data from dataset
# df = pd.read_csv('C:/Users/ASUS/Desktop/project/Core-periphery-Structures/dataset/soc-sign-bitcoinotc-with-no-time.csv', sep=',',usecols=[0,1], names=['source', 'target'])
df = pd.read_csv('dataset/soc-sign-bitcoinotc.csv',usecols=[0,1,2], names=['source', 'target', 'rate'])
print(df)
G = nx.from_pandas_edgelist(df)

print(nx.info(G))


algorithm = cpnet.KM_config()
algorithm.detect(G)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

core_nodes = []
print('Name\tPairID\tCoreness')
for key, value in sorted(c.items(), key=lambda x: x[1]):
    
    if(x[key] == 1):
        print('%s\t%d\t%f' %(key, c[key], x[key]))
        core_nodes.append(key)
print(core_nodes)


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