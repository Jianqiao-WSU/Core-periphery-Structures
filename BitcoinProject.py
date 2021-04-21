#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:59:46 2021

@author: parikshitpanwar
"""
import cpnet
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from csv import reader

# col_list = ['A', 'B', 'C', 'D']
# ds = pd.read_csv('/Users/parikshitpanwar/Desktop/Library/Elements of Network Science/Project/Core-periphery-Structures-main/dataset/soc-sign-bitcoinotc.csv')

# listofcols = list(ds.columns)

# mycolist = ['2', '4', '1289241911.72836']
# print(ds[mycolist])

df = pd.read_csv('dataset/soc-sign-bitcoinotc.csv',usecols=[0,1,2], names=['source', 'target', 'rate'])
# print(df)
g = nx.from_pandas_edgelist(df)

print(nx.info(g))

kmconfig = cpnet.KM_config()
kmconfig.detect(g)
a = kmconfig.get_pair_id()
b = kmconfig.get_coreness()

# Variable to calculate total weight of edge
edgeWeight = 0

# with open('dataset/soc-sign-bitcoinotc.csv', 'r') as fin:
#     csv_reader = reader(fin)
#     for row in csv_reader:
#         print(row)

df.sort_values(["source"], axis=0,
                 ascending=True, inplace=True)

sourceList = []

for key, value in b.items():
    if value > 0:
        sourceList.append(key)
    
print(sourceList)

# Read csv row wise.
# with open('dataset/soc-sign-bitcoinotc.csv', 'r') as fin:
#     csv_reader = reader(fin)
#     for key, value in b.items():
#         if value > 0:
#             for row in csv_reader:
#                 print(key)
#                 if key == row[0]:
#                     # print(row[0])
#                     edgeWeight += int(row[2])
                   
# with open('dataset/soc-sign-bitcoinotc.csv', 'r') as fin:
#     csv_reader = reader(fin)
#     for row in csv_reader:
#         for key, value in b.items():
#             if value > 0:


# print(n)
# print(edgeWeight)






        
