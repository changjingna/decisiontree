import xlwt
import xlrd
import pickle

'''
我的读取excel文件
'''
def read_excel():
    workbook=xlrd.open_workbook(r'D:\pytest\mydata1.xls',formatting_info=True)
    dataSheet=workbook.sheet_by_index(0) #Sheet1
    col1=dataSheet.col_values(1)    #属性1，第一列
    nemptyRIndex=[]
    for i in range(1,len(col1)):
        if dataSheet.cell(i,1).ctype == 1: #属性1不为空白值的行
            nemptyRIndex.append(i)
    nemptyCIndex=[1,2,5,6,7,8,9,10,11,12,13,14,15,16]
    dataSet=[]
    for j in nemptyRIndex:
        rowdata = []
        for i in nemptyCIndex:
            rowdata.append(dataSheet.cell_value(j,i))
        dataSet.append(rowdata)
        del rowdata
    return dataSet

#转换测试集为数字(测试部分属性)
def tran_dataSet(dataSet):
    tdataSet=[]
    for i in range(127):
        dataunit = dataSet[i]   #取每一行测试数据
        newdataunit = []
        #print(dataunit)
        for j in range(14): #遍历每个属性将其转换为数字进行表示
            if j == 0:  #属性1
                if dataunit[j] == 'Y':
                    newdataunit.append(1)
                else:
                    newdataunit.append(0)
            # if j == 1:
            #     if dataunit[j] == '步行/Walk':
            #         dataunit[j]=0
            #     elif dataunit[j] == '地铁/Subway':
            #         dataunit[j]=1
            #     elif dataunit[j] == '公交/Bus':
            #         dataunit[j]=2
            #     elif dataunit[j] == '开车(私家车)/Private Car':
            #         dataunit[j]=3
            #     elif dataunit[j] == '其他（单车）':
            #         dataunit[j]=4
            # tdataSet.append(dataunit)
            if j == 2:  #属性3
                if dataunit[j] == '是/Yes':
                    newdataunit.append(1)
                else:
                    newdataunit.append(0)
            #tdataSet.append(dataunit)
            if j == 3:  #属性4
                if dataunit[j] == '家人/Family':
                    newdataunit.append(0)
                elif dataunit[j] == '朋友/Friends':
                    newdataunit.append(1)
                elif dataunit[j] == '只是自己喝/Self only':
                    newdataunit.append(2)
                else:
                    newdataunit.append(3)
            #tdataSet.append(dataunit)
            if j == 4:  #属性5
                if dataunit[j] == '在家喝/At Home':
                    newdataunit.append(0)
                elif dataunit[j] == '路上喝(回家之前喝)/On the Road（before arriving home）':
                    newdataunit.append(1)
                elif dataunit[j] == '外出郊游喝 For Outing':
                    newdataunit.append(2)
                else:
                    newdataunit.append(3)
            #tdataSet.append(dataunit)
            if j == 5:  #属性6
                if dataunit[j] == '喝/Yes':
                    newdataunit.append(1)
                else:
                    newdataunit.append(0)
            #tdataSet.append(dataunit)
            if j == 6:  #属性7
                if dataunit[j] == '夫妻/Married couple':
                    newdataunit.append(0)
                elif dataunit[j] == '女/Female':
                    newdataunit.append(1)
                else:
                    newdataunit.append(2)
            #tdataSet.append(dataunit)
            if j == 10: #属性11
                if dataunit[j] == '未婚/Single':
                    newdataunit.append(0)
                elif dataunit[j] == '已婚无小孩/Married with no child':
                    newdataunit.append(1)
                elif dataunit[j] == '已婚有小孩/Married with child (children)':
                    newdataunit.append(2)
                else:
                    newdataunit.append(3)
        newdataunit.append(dataunit[13])
        tdataSet.append(newdataunit)
        del newdataunit
    #print(tdataSet)
    return tdataSet

#存储提取出来的测试集
def store_dataSet(filename,dataSet1):
    with open(filename,'wb') as fw:
        pickle.dump(dataSet1,fw)
    return None

#普通存储测试集
def store_plain(filename,dataSet1):
    f=open(filename,'w')
    f.write(str(dataSet1))  #存入以str形式
    f.close()

if __name__ == '__main__':
    mdataSet=read_excel()
    #store_dataSet('dataset.txt',mdataSet)
    tdataSet=tran_dataSet(mdataSet)
    count=0
    for i in range(127):
        if tdataSet[i][3] == 0 and tdataSet[i][5] == 0:
            print(i,':',tdataSet[i])

    #store_plain(r'D:\pytest\datatest.txt',tdataSet)

