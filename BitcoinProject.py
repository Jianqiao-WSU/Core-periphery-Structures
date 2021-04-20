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

g = nx.Graph()

with open('dataset/soc-sign-bitcoinotc.csv') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        # print(row[2])
        g.add_edge(row[0], row[1], weight = row[2])

print(nx.info(g))