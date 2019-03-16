"""
author : leliyliu
you can learn the property of markov chain
马尔科夫链要能收敛，需要满足以下条件：
1.可能的状态数是有限的。
2.状态间的转移概率需要固定不变。
3.从任意状态能够转变到任意状态。
4.不能是简单的循环，例如全是从x到y再从y到x。
"""


import numpy as np

def markov(iterator,init_array):
    #init_array=np.array([0.1,0.2,0.7])
    transfer_matrix=np.array([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]])
    restmp=init_array
    for i in range(iterator):
        res=np.dot(restmp,transfer_matrix)
        #print(i,"\t",res)
        restmp=res
    print(iterator, "\t", res)

def matrixpower():
    transfer_matrix = np.array([[0.9, 0.075, 0.025],
                               [0.15, 0.8, 0.05],
                               [0.25, 0.25, 0.5]])
    restmp = transfer_matrix
    for i in range(25):
        res = np.dot(restmp, transfer_matrix)
        print (i, "\t", res)
        restmp = res

matrixpower()

iterator=30
for i in range(100):
    init_array=np.random.randint(1,100,size=(1,3))
    init_array=init_array/np.sum(init_array)
    #print(init_array)
    markov(iterator,init_array)

