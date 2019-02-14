import matplotlib.pyplot as plt

#设置画节点用的盒子的样式
decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round",fc="0.8")
#设置画箭头的样式
arrow_args = dict(arrowstyle="<-")

#获取叶子节点的个数
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    seconDict = myTree[firstStr]
    for key in seconDict.keys():
        if type(seconDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(seconDict[key])
        else:
            numLeafs += 1
    return numLeafs

#获取树的深度
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    seconDict = myTree[firstStr]
    for key in seconDict.keys():
        if type(seconDict[key]).__name__ == 'dict':
            thisDepth = getTreeDepth(seconDict[key]) + 1
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

#绘制中间的文字
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid ,txtString)

'''
绘制节点
annotate()函数为指定数据点xy添加一个nodeTxt的注释
xycoords设置指定点的坐标类型；axes fraction表示以子绘图区左下角为参考，单位是百分比
'''
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                            va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)


#绘制树
def plotTree(myTree,parentPt,nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


'''
createPlot是主函数
'''
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')  #窗口id;背景颜色
    fig.clf()   #清除figure
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    # 节点的x轴的偏移量为-1/plotTree.totlaW/2,1为x轴的长度，除以2保证每一个节点的x轴之间的距离为1/plotTree.totlaW*2
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    #plt.show()
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
    # plt.rcParams['axes.unicode_minus'] = False
    #plt.savefig(r'D:\temp.png') #当plt.show()时就不能存入了