from sklearn.model_selection import train_test_split
import operator
from math import log2
import xlrd
import cjnTreePlotter

'''
加载训练集和测试集
'''
def load_data(train_size):
    workbook = xlrd.open_workbook(r'D:\pytest\alldata.xls', formatting_info=True)
    dataSheet = workbook.sheet_by_index(0)  # Sheet1
    rowCounts = 155
    columnCounts = 17
    data_set = []
    for i in range(1, rowCounts):
        rowData = []
        for j in range(1, columnCounts):
            if j == 3 or j == 4:
                pass
            else:
                if dataSheet.cell(i, j).ctype == 1:
                    temp = str(dataSheet.cell_value(i, j)).strip().lower()
                    rowData.append(temp)
                else:
                    rowData.append(dataSheet.cell_value(i, j))
        data_set.append(rowData)
        del rowData
    # for d in data_set:
    #     print(d)
    data_size = len(data_set)
    test_data_size = data_size-train_size
    train_data, test_data = train_test_split(data_set, test_size=test_data_size / data_size)
    return train_data, test_data


#1
def data_member(x):
    member = {'n': 0, 'y': 1}
    return member[x]
#2
def data_transportation(x):
    t = {'开车(私家车)/private car': 0,
         '公交/bus': 1,
         '地铁/subway': 1,
         '步行/walk': 2,
         '其他（单车）': 3}
    return t[x]
#3
def data_drinkBySelf(x):
    bySelf = {'否/no': 0, '是/yes': 1}
    return bySelf[x]
#4
def data_whodrink(x):
    if x == '只是自己喝/self only':
        who_drink = 0
    elif x == '家人/family':
        who_drink = 1
    elif x == '朋友/friends':
        who_drink = 2
    else:
        who_drink = 3
    # who_drink = {'只是自己喝/Self only ': 0, '家人/Family': 1, '朋友/Friends ': 2,
    #              '其他，请注明: Other, please specify                       ': 3}
    return who_drink
#5
def data_wheredrink(x):
    if x == '在家喝/at home':
        where_drink = 0
    elif x == '路上喝(回家之前喝)/on the road（before arriving home）':
        where_drink = 1
    elif x == '外出郊游喝 for outing':
        where_drink = 2
    else:
        where_drink = 3
    # where_drink = {'在家喝/At Home': 0,
    #                '路上喝(回家之前喝)/On the Road（before arriving home）': 1,
    #                '外出郊游喝 For Outing': 2,
    #                '其他，请注明: /Other, Please Specify': 3}
    return where_drink
#6
def data_dailydrink(x):
    daily_drink = {'不喝/no': 0, '喝/yes': 1}
    return daily_drink[x]
#7
def data_gender(x):
    # if x == '女/female':
    #     gender = 0
    # elif x == '男/male':
    #     gender = 1
    # else:
    #     gender = 2
    gender = {'女/female': 0, '男/male': 1, '夫妻/married couple': 2}
    return gender[x]
#8
def data_age(x):
    age = {'18-22岁/years old': 0,
           '23-28/years old': 1,
           '29-35/years old': 2,
           '36-45/years old': 3,
           '46-55/years old': 4,
           '56岁以上 over 56': 5}
    return age[x]
#9
def data_education(x):
    education = {'小学/elementary school': 0,
                 '初中/middle school': 1,
                 '高中/技校或同等水平毕业 high school/training school or equivalent degree': 2,
                 '大专/college': 3,
                 '本科/bachelor': 4,
                 '研究生及以上/master or higher': 5}
    return education[x]
#10
def data_occupation(x):
    occupation = {'大众群体（商业服务业一般从业人员/个体工商户/产业工人）'
                  'general public（business service practitioner/self employed/industry worker）': 0,
                '私营企业主 self owned entrepreneur（商业服务业一般从业人员/个体工商户/产业工人）': 1,
                '外企以及私企白领 foreign-capital enterprise/ private enterprise employee': 2,
                '国有企事业职员 state owned enterprise employee': 3,
                '文体艺术人士 (包括教师) education/art/sports': 4,
                '高校学生 university student': 5,
                '公务员 public servant': 6,
                '自由职业者 freelancer': 7,
                '退休/下岗/待业 retired/laid off/unemployed': 8}
    return occupation[x]
#11
def data_marital(x):
    # if x == '未婚/single':
    #     marital = 0
    # elif x == '已婚有小孩/married with child (children)':
    #     marital = 1
    # elif x == '拒不便告知 unwilling to tell':
    #     marital = 2
    # else:
    #     marital = 3
    marital = {'未婚/single': 0,
               '已婚无小孩/married with no child': 1,
               '已婚有小孩/married with child (children)': 2,
               '拒不便告知 unwilling to tell': 3}
    return marital[x]
#12
def data_income(x):
    # if x == '3000以下/below 3000 rmb':
    #     income = 0
    # elif x == '3000-4999元/rmb':
    #     income = 1
    # elif x == '5000元/rmb-9999元/rmb':
    #     income = 2
    # elif x == '10000-14999元/rmb':
    #     income = 3
    # elif x == '15000-19999元/rmb':
    #     income = 4
    # elif x == '20000-29999元/rmb':
    #     income = 5
    # elif x == '30000及以上/30000 and above':
    #     income = 6
    # else:
    #     income = 7
    income = {'3000以下/below 3000 rmb': 0,
              '3000-4999元/rmb': 1,
              '5000元/rmb-9999元/rmb': 2,
              '10000-14999元/rmb': 3,
              '15000-19999元/rmb': 4,
              '20000-29999元/rmb': 5,
              '30000及以上/30000 and above': 6,
              '拒不便告知 unwilling to tell': 7}
    return income[x]

def tranVals(data_set):
    rowCounts = len(data_set)
    columnCounts = len(data_set[0])
    tranDataSet = []
    for data in data_set:
        tranRowData = []
        for j in range(columnCounts):
            if j == 0:
                if data[j] == '':
                    tranRowData.append(2)
                else:
                    tranRowData.append(data_member(data[j]))
            elif j == 1:
                tranRowData.append(data_transportation(data[j]))
            elif j == 2:
                tranRowData.append(data_drinkBySelf(data[j]))
            elif j == 3:
                tranRowData.append(data_whodrink(data[j]))
            elif j == 4:
                tranRowData.append(data_wheredrink(data[j]))
            elif j == 5:
                tranRowData.append(data_dailydrink(data[j]))
            elif j == 6:
                tranRowData.append(data_gender(data[j]))
            elif j == 7:
                tranRowData.append(data_age(data[j]))
            elif j == 8:
                tranRowData.append(data_education(data[j]))
            elif j == 9:
                tranRowData.append(data_occupation(data[j]))
            elif j == 10:
                tranRowData.append(data_marital(data[j]))
            elif j == 11:
                tranRowData.append(data_income(data[j]))
            elif j == 12:
                tranRowData.append(data[j])
            else:
                tranRowData.append(data[j])
        tranDataSet.append(tranRowData)
    return tranDataSet


'''
多数表决：返回标签列表中数量最大的类
'''
def most_voted_attribute(label_list):
    label_nums = {}
    for label in label_list:
        if label in label_nums.keys():
            label_nums[label] += 1
        else:
            label_nums[label] = 1
    sorted_label_nums = sorted(label_nums.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_label_nums[0][0]  #返回出现最多次的键（也就是标签名称）

'''
决策树的生成
'''
def generate_decesion_tree(data_set,attribute_label):
    label_list = [entry[-1] for entry in data_set]
    if label_list.count(label_list[0]) == len(label_list): #所有数据类标签一样
        return label_list[0]
    if len(data_set[0]) == 1:   #数据集中属性已经用完
        return most_voted_attribute(label_list)
    best_attribute_index, best_split_point = best_attribute_selection(data_set)
    best_attribute = attribute_label[best_attribute_index]
    decision_tree = {best_attribute: {}}
    del(attribute_label[best_attribute_index])  #找到最佳划分属性后需要将其从属性名列表中删除
    """
    如果best_split_point为空，说明此时最佳划分属性的类型为离散值，否则为连续值
    """
    if best_split_point is None:    # is: best_split_point=0.0不影响判断是不是None
        attribute_list = [entry[best_attribute_index] for entry in data_set]
        attribute_set = set(attribute_list)
        for attribute in attribute_set:
            sub_labels = attribute_label[:] #attribute_label只会在第一次被del一个属性，之后不会
            decision_tree[best_attribute][attribute] = generate_decesion_tree(
                split_data_set(data_set, best_attribute_index, attribute, continuous=False), sub_labels)
    else:
        """
        最佳划分属性类型为连续值，此时计算出的最佳划分点将数据集一分为二，划分字段取名为<=和>
        """
        sub_labels = attribute_label[:]
        decision_tree[best_attribute]["<="+str(best_split_point)]=generate_decesion_tree(
            split_data_set(data_set, best_attribute_index, best_split_point, True, 0), sub_labels)
        sub_labels = attribute_label[:]
        decision_tree[best_attribute][">" + str(best_split_point)] = generate_decesion_tree(
            split_data_set(data_set, best_attribute_index, best_split_point, True, 1), sub_labels)
    return decision_tree


'''
选择最佳离散属性或者来连续属性的最佳划分点
分两种情况计算
'''
def best_attribute_selection(data_set):
    num_attributes = len(data_set[0])-1
    info_D = calc_info_D(data_set)  #计算香农熵
    max_grain_rate = 0.0    #最大信息增益比
    best_attribute_index = -1
    best_split_point = None
    continuous = False
    for i in range(num_attributes):
        attribute_list = [entry[i] for entry in data_set]
        info_A_D = 0.0  #特征A对数据集D的信息增益
        split_info_D = 0.0  #数据集D关于特征A的值的熵
        if i is 12:
            continuous = True
        #属性值为连续
        if continuous == True:
            attribute_list.sort()   #排序
            temp_set = set(attribute_list)
            attribute_list = list(temp_set)
            split_points = []
            for index in range(len(attribute_list) - 1):    #求各个划分点
                split_points.append((float(attribute_list[index]) + float(attribute_list[index + 1])) / 2)
            for split_point in split_points:
                info_A_D = 0.0
                split_info_D = 0.0
                for part in range(2):
                    sub_data_set = split_data_set(data_set,i,split_point,True,part)
                    prob = len(sub_data_set) / float(len(data_set))
                    info_A_D += prob * calc_info_D(sub_data_set)
                    split_info_D -= prob * log2(prob)
                if split_info_D == 0.0:
                    split_info_D += 1
                """
                由于关于属性A的熵split_info_D可能为0，因此需要特殊处理
                常用的做法是把求所有属性熵的平均，为了方便，此处直接加1
                """
                grain_rate = (info_D - info_A_D) / split_info_D #计算信息增益比
                if grain_rate > max_grain_rate:
                    max_grain_rate = grain_rate
                    best_split_point = split_point
                    best_attribute_index = i
        else:
            attribute_list = [entry[i] for entry in data_set]
            attribute_set = set(attribute_list)
            for attribute in attribute_set:
                sub_data_set = split_data_set(data_set, i, attribute,False)
                prob = len(sub_data_set) / float(len(data_set))
                info_A_D += prob * calc_info_D(sub_data_set)
                split_info_D -= prob * log2(prob)
                if split_info_D == 0.0:
                    split_info_D += 1
                grain_rate = (info_D - info_A_D) / split_info_D
                if grain_rate > max_grain_rate:
                    max_grain_rate = grain_rate
                    best_attribute_index = i
                    best_split_point = None

    return best_attribute_index, best_split_point


'''
计算数据集D的香农熵
'''
def calc_info_D(data_set):
    num_entries = len(data_set)
    label_nums = {}
    for entry in data_set:
        label = entry[-1]
        if label in label_nums:
            label_nums[label] += 1
        else:
            label_nums[label] = 1
    info_D = 0.0
    for label in label_nums.keys():
        prob = float(label_nums[label]) / num_entries
        info_D -= prob * log2(prob)
    return info_D


'''
按属性划分数据集
part在连续属性划分时使用，为0时表示得到划分点左边的数据集，为1时表示得到右边的数据集
'''
def split_data_set(data_set, index, value, continuous, part = 0):
    res_data_set=[]
    if continuous == True:
        for entry in data_set:
            if part == 0 and float(entry[index]) <= value:
                reduced_entry = entry[:index]
                reduced_entry.extend(entry[index+1:])
                res_data_set.append(reduced_entry)
            if part == 1 and float(entry[index]) > value:
                reduced_entry = entry[:index]
                reduced_entry.extend(entry[index + 1:])
                res_data_set.append(reduced_entry)
    else:
        for entry in data_set:
            if entry[index] == value:
                reduced_entry = entry[:index]
                reduced_entry.extend(entry[index + 1:])
                res_data_set.append(reduced_entry)
    return res_data_set


'''
对一项测试数据进行预测，通过递归来预测该项数据的标签
decision_tree:字典结构的决策树
attribute_labels:数据的属性名列表
one_test_data：预测的一项测试数据
'''
def decesion_tree_predict(decesion_tree, attribute_labels, one_test_data):
    first_key = list(decesion_tree.keys())[0]   #将字典结构的决策树的键值列表化，获取第一个键名
    second_dic = decesion_tree[first_key]
    attribute_index = attribute_labels.index(first_key)
    res_label =None
    for key in second_dic.keys():
        if key[0] == '<':   #取键值的第一个字符来比较
            value = float(key[2:])
            if float(one_test_data[attribute_index]) <= value:
                    if type(second_dic[key]).__name__ == 'dict':
                        res_label = decesion_tree_predict(second_dic, attribute_labels, one_test_data)
                    else:
                        res_label = second_dic[key]
        elif key[0] == '>':
            value = float(key[1:])
            if float(one_test_data[attribute_index]) > value:
                if type(second_dic[key]).__name__ == 'dict':
                    res_label = decesion_tree_predict(second_dic[key], attribute_labels, one_test_data)
                else:
                    res_label = second_dic[key]
        else:
            if one_test_data[attribute_index] == key:
                if type(second_dic[key]).__name__ == 'dict':
                    res_label = decesion_tree_predict(second_dic[key], attribute_labels, one_test_data)
                else:
                    res_label = second_dic[key]
    return res_label


if __name__ == '__main__':
    train_size = 108
    train_data, test_data = load_data(train_size)
    tran_train_data = tranVals(train_data)
    attribute_label = ['Member', 'Transportation',
                       'selfDrink',
                       'who',
                       'where',
                       'drinkDaily',
                       'gender', 'age', 'education',
                       'occupation', 'married',
                       'Income', 'Total volumes', 'segmentation']
    aaa = generate_decesion_tree(tran_train_data, attribute_label)
    print(aaa)
    cjnTreePlotter.createPlot(aaa)



