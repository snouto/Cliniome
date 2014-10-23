__author__ = 'Mohamed'
import numpy as np
from math import sqrt
from scipy.stats.stats import  *
from prepare import *
import pandas as pd

ROWS = 1
COLUMNS = 0






def dawnDamping(adj,mu=3.0):

    matrix = np.matrix(adj)
    links = matrix.sum(axis=COLUMNS)
    dvec = links / (links+mu)

    return dvec







def dawnMatrix(adjMatrix):
    matrix = np.matrix(adjMatrix)
    colsums = matrix.sum(axis=COLUMNS)
    transposed = matrix
    #transitionMatrix = np.transpose((transposed/(colsums+1e-16)))
    intermediate = (colsums + 1e-16)
    transitionMatrix = np.divide(transposed,intermediate)
    return transitionMatrix


def Dawn(adjMatrix,expressionVector,mutationVector,damping,maxit=100,
         epsilon=1e-04,goldStandard=None,patientTag="defaultPatient"):


    dawnmatrix = dawnMatrix(adjMatrix)
    expressionVector = expressionVector.transpose()
    ranking_T = expressionVector/expressionVector.sum()
    ranking_T = ranking_T.transpose()
    constantTerm = expressionVector/expressionVector.sum()
    tail =  (1-damping)
    constantTerm = np.multiply(constantTerm,tail)

    capsule = {}

    for i in range(1,maxit):
        first = np.multiply(dawnmatrix,ranking_T)
        first = np.diag(first)
        second = np.multiply(first,damping)
        second = second.transpose()
        third = second + constantTerm
        third = np.diag(third)
        third = np.matrix(third)
        ranking_T1 = third.transpose()
        inner = ranking_T1 - ranking_T
        powered = np.power(inner,2)
        mag = sqrt(powered.sum())
        ranking_T = ranking_T1
        print ("mag : %s" % mag)
        if mag < epsilon:
            print("We are breaking from the loop")
            break

    capsule['Rank'] = ranking_T
    capsule['PercentRank'] = 100.0 * (rankdata(ranking_T) / (len(ranking_T) + 1))
    capsule['isMutated'] = mutationVector

    mutatedRanks = []

    if mutationVector != None:

             if mutationVector.sum() > 0:
                mutatedRanks = (mutationVector == 1.0)
               # mutatedRanks = mutatedRanks[:,-3]
             else:
                  mutatedRanks = [0.0 for x in range(len(mutationVector))]


    return {'summaryOutput':capsule , 'mutatedRanks' : mutatedRanks}





def main():

    adjfile = open('/home/snouto/Desktop/adjmatrixPickled.bin','rb')
    expressionfile = open('/home/snouto/Desktop/expressionData.bin','rb')
    adjmatrix = pickle.load(adjfile)
    adjacencymatrix = [[float(x) for x in list] for list in adjmatrix]
    adjacencymatrix = np.matrix(adjacencymatrix)
    expressionMatrix = pickle.load(expressionfile)
    expressionMatrix = [[float(x) for x in list] for list in expressionMatrix]
    expressionMatrix = np.matrix(expressionMatrix)
    expressionVector = expressionMatrix[:,0]

    adjmatrix = np.matrix(adjmatrix)
    expressionMatrix = np.matrix(expressionMatrix)
    expressionVector = expressionMatrix[:,0]
    damping = dawnDamping(adjmatrix)

    dawn = Dawn(adjmatrix,expressionVector,None,damping)

    print (dawn)

    return dawn



if __name__ =='__main__':
    main()

