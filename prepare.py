__author__ = 'root'
import pickle
import numpy as np

import pandas as pd


"""
adjfile = open('/home/snouto/Desktop/adjmatrixPickled.bin','rb')
expressionfile = open('/home/snouto/Desktop/expressionData.bin','rb')
adjmatrix = pickle.load(adjfile)
adjacencymatrix = [[float(x) for x in list] for list in adjmatrix]
adjacencymatrix = np.matrix(adjacencymatrix)
expressionMatrix = pickle.load(expressionfile)
expressionMatrix = [[float(x) for x in list] for list in expressionMatrix]
expressionMatrix = np.matrix(expressionMatrix)
expressionVector = expressionMatrix[:,0]
"""

path = '/home/snouto/Desktop/'
adjmatrix = pd.DataFrame.from_csv(path+'pathway.bin',header=1,sep=',')
expressionmatrix = pd.DataFrame.from_csv(path+'expression.bin',header=1,sep=',')
adjmatrix = np.matrix(adjmatrix)
expressionMatrix = np.matrix(expressionmatrix)


