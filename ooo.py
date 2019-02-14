from math import log2
import operator
import pickle
from test2 import read_excel
from test2  import tran_dataSet
import xlrd
import random
import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder

'''
我的构造并存储决策树代码
'''


#创建测试数据集
def createDataSet():
    dataSet = [[0, 0, 0, 0, 'no'],  # 数据集
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']  # 分类属性
    return dataSet, labels  # 返回数据集和分类属性

#读取表格全部数据
def read_my_excel():
    workbook=xlrd.open_workbook(r'D:\pytest\alldata.xls',formatting_info=True)
    dataSheet=workbook.sheet_by_index(0) #Sheet1
    rowCounts=155
    columnCounts=17
    allDataSet=[]
    with open(r'D:\pytest\alldata.txt','w') as fw:  #将读到的数据写入txt文本中
        for i in range(1,rowCounts):
            rowData = []
            for j in range(1,columnCounts):
                if j == 3 or j == 4:
                    pass
                else:
                    rowData.append(dataSheet.cell_value(i,j))
            print(rowData)
            rowData=str(rowData).strip('[').strip(']').replace(',','\t')+'\n'
            fw.write(rowData)
            #allDataSet.append(rowData)
            del rowData
    return allDataSet

#数据预处理（数值化并处理缺失和重复值）
def transToValues(excelDataSet):
    column_labels=['member','transportation','drink self','who drink','where drink','daily drink','sex','age',
                   'education','occupation','marital','income','total volumes','segmentation']
    dataSet_pd=DataFrame(excelDataSet,columns=column_labels)
    lc=LabelEncoder()   #创建LabelEncoder对象
    for col in range(12):  # 为每一列序列化
        dataSet_pd[col] = lc.fit_transform(dataSet_pd[col])
    return None


#13
def data_totalVolumes(x):
    x=int(x)
    if x >=0 and x <1:
        key='s'
    elif x >= 1 and x <= 2:
        key='m'
    else:
        key='l'
    totalVolumes={'s':0,'m':1,'l':2}
    return totalVolumes[x]

#14
def data_label(x):
    dataLabel={'Light shopper':0,'Medium shopper':1,'Heavy shopper':2}
    return dataLabel[x]



# def transToValues1(file_name,save_name,remove_unKnowValue=True,remove_duplicates=True):
#
#     converters={1:data_member,2:data_transportation,3:data_drinkBySelf,4:data_whodrink,5:data_wheredrink,
#                 6:data_dailydrink,7:data_gender,8:data_age,9:data_education,10:data_occupation,11:data_marital,
#                 12:data_income,13:data_totalVolumes,14:data_label}
#     # dataSet_pd=pd.read_excel(file_name,sheet_name=0,header=None,skiprows=0,skipfooter=0,converters=converters,
#     #                          names=['bianhao', 'member', 'transportation', 'drinkBySelf', 'whodrink', 'wheredrink',
#     #                                 'dailydrink','gender', 'age', 'education', 'occupation', 'marital', 'income',
#     #                                 'totalVolumes','labels'])
#     dataSet_pd=pd.read_table(file_name,header=None,converters=converters,
#                              names=['member','transportation','drinkBySelf','whodrink','wheredrink','dailydrink',
#                                     'gender','age','education','occupation','marital','income','totalVolumes','labels'],
#                              encoding='utf-8')
#     if remove_duplicates:
#         dataSet_pd.drop_duplicates(inplace=True)
#         print('drop duplicates!')
#
#     if remove_unKnowValue:
#         #处理缺失值
#         dataSet_pd.replace(['?'], np.NAN, inplace=True)
#
#     dataSet_pd.to_tabel(save_name, header=False, index=False)


#生成随机数划分训练和测试
def generateRandom(partDataSet):
    lenp=len(partDataSet)
    nump=round(lenp*0.3)#round() 返回最接近原数的整型值（四舍五入）
    parttestset=[]
    parttrainset=[]
    record2, set1 = 0, set()
    while record2 < nump:
        record1 = len(set1)
        random1 = random.randint(1, lenp)  # [1,57]
        set1.add(random1)
        record2 = len(set1)
        if (record2 - record1) == 1:
            parttestset.append(partDataSet[random1 - 1])
    for i in range(lenp):
        if (i+1) not in set1:
            parttrainset.append(partDataSet[i])
    return parttestset,parttrainset

#生成训练集和测试集(参数：已经处理过的数据集)
def generateTrainSet(dealDataSet):
    ldataset=[]
    mdataset=[]
    hdataset=[]
    for i in range(len(dealDataSet)):
        if dealDataSet[i][-1] == 'Light shopper':
            ldataset.append(dealDataSet[i])
        elif dealDataSet[i][-1] == 'Medium shopper':
            mdataset.append(dealDataSet[i])
        else:
            hdataset.append(dealDataSet[i])
    trainset=[] #训练集 70%
    testset=[] #测试集 30%
    test1,train1=generateRandom(ldataset)
    test2,train2=generateRandom(mdataset)
    test3,train3=generateRandom(hdataset)
    # testset.extend(test1)
    # testset.extend(test2)
    # testset.extend(test3)
    testset=test1+test2+test3 #+用于组合列表
    trainset=train1+train2+train3
    return trainset,testset

#计算给定数据集的经验熵(关键用数据集的最后一列)
def calcSahnnoEnt(dataSet):
    numEntires=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntires
        shannonEnt-=prob*log2(prob)
    return shannonEnt

#按照给定特征划分数据集(只去掉给定特征所在列)
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec=featVec[:axis] #[0,axis)
            reducedFeatVec.extend(featVec[axis+1:]) #[axis+1,最后]
            retDataSet.append(reducedFeatVec)
    #print('splitDataSet里的retDataSet:',retDataSet)
    return retDataSet

#计算信息增益
def calcEntGain(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcSahnnoEnt(dataSet)
    infoGain=[]
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcSahnnoEnt(subDataSet)
        singleInfoGain=baseEntropy-newEntropy
        infoGain.append(singleInfoGain)
    return infoGain

#计算信息增益率
def calcEntGainRate(dataSet):
    minfoGain=[]
    minfoGain=calcEntGain(dataSet) #信息增益
    numInfoGain=len(minfoGain)
    sumInfoGain=0.0
    for i in range(numInfoGain):
        sumInfoGain+=minfoGain[i]
    averInfoGain=sumInfoGain / numInfoGain #信息增益平均值
    infoGainRate={}
    for i in range(numInfoGain):
        if minfoGain[i]>averInfoGain: #若信息增益大于信息增益平均值则计算增益率
            #计算信息增益率
            featList = [example[i] for example in dataSet]
            uniqueVals = set(featList)
            IVa = 0.0
            for value in uniqueVals:
                subDataSet = splitDataSet(dataSet, i, value)
                prob = len(subDataSet) / float(len(dataSet))
                IVa -= prob * log2(prob)
            infoGainRate[i]= minfoGain[i] / IVa
        else:
            pass
    return infoGainRate

#选择最优特征
def chooseBestFeatureToSplit(dataSet):
    bestInfoGain = 0.0  # 信息增益
    bestInfoGainRate=0.0
    bestFeature=-999  #最优特征索引值
    minfoGainRate=calcEntGainRate(dataSet)
    infoGain1=[]
    if not minfoGainRate: #字典为空
        infoGain1=calcEntGain(dataSet)
        bestInfoGain=max(infoGain1)
        bestFeature=list.index(max(infoGain1))
        print(bestFeature)
    else:
        bestInfoGainRate = max(zip(minfoGainRate.values(),minfoGainRate.keys()))
        bestFeature=bestInfoGainRate[1]
        print(bestFeature)
    return bestFeature  #返回最有特征的索引值

#统计classList中出现此处最多的元素（类标签）
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

#递归创建决策树
def createTree(dataSet,labels,featLabels):
    print('进入决策树:',len(dataSet))
    # for i in range(len(dataSet)):
    #     print(dataSet)
    classList=[example[-1] for example in dataSet]  #取分类标签
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最优特征（获得最优特征的索引值）
    #1.递归停止条件1：类别完全相同
    if classList.count(classList[0])== len(classList):
        print('递归停止条件1执行：',classList[0])
        return classList[0]
    #2.递归停止条件2：遍历完所有特征时返回出现次数最多的类标签：
    if len(dataSet[0]) == 1 or bestFeat == -999:
        print('递归停止条件2执行：',majorityCnt(classList))
        return majorityCnt(classList)
    #建立决策树
    bestFeatLabel=labels[bestFeat]  #获得最优特征的标签
    featLabels.append(bestFeatLabel)    #记录各个用于分类特征
    myTree={bestFeatLabel:{}}   #生成树
    print('myTree:',myTree)
    del(labels[bestFeat])   #从labels列表里删除已经用过的标签
    featValues=[example[bestFeat] for example in dataSet]   #得到特征值所在列的所有值
    uniqueVals=set(featValues)
    for value in uniqueVals:    #遍历特征，创建决策树   myTree[][]??
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),labels,featLabels)
    return myTree

#使用决策树分类
def classify(inputTree,featLabels,testVec):
    firstStr=next(iter(inputTree))  #返回迭代器的下一个项目(决策树下一节点)
    #print('first:',firstStr)   #有自己的房子，有工作
    secondDict=inputTree[firstStr]  #节点对应的字典
    #print('second:',secondDict)    #{0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}, {0: 'no', 1: 'yes'}
    featIndex=featLabels.index(firstStr)    #0,1
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':  #说明还有分支
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel   #classLabel:yes或no

#存储决策树
def storeTree(inputTree,filename):
    with open(filename,'wb') as fw:
        pickle.dump(inputTree,fw)
    return None

#读取决策树
def grabTree(filename):
    fr=open(filename,'rb')
    return pickle.load(fr)

#读取测试集数据
def grabDataSet(filename):
    rdataset=open(filename,'rb')
    return pickle.load(rdataset)

#普通读取测试数据
def readDataSet(filename):
    f=open(filename,'r')
    rdataSet=str(f.read(filename))
    f.close()
    return rdataSet

if __name__ == '__main__':
     # mdataSet = read_excel()
     # tdataSet = tran_dataSet(mdataSet)
     # mlabels = ['1会员', '3自己饮用否', '4给谁买', '5在哪喝', '6平时喝酒情况', '7性别', '11婚姻情况']
     # featLabels=[]
     # myTree=createTree(tdataSet,mlabels,featLabels)
     #transToValues1(r'D:\pytest\alldata.txt', r'D:\pytest\123.txt')
     a = 0










