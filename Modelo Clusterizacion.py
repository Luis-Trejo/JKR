# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:50:29 2019

@author: Kike
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

dataframe = pd.read_csv(r"C:\Users\Kike\Documents\MEGA\Yopter\analisis.csv")
dataframe.head()

dataframe.describe()

