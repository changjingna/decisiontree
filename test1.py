import xlrd
import xlwt
from datetime import date

'''
学习python 读写excel文件，列、行以0开始计数
'''
#读取excel文件
def read_excel():
    workbook=xlrd.open_workbook(r'D:\pytest\test1.xls',formatting_info=True)
    print(workbook.sheet_names())
    sheet2_name=workbook.sheet_names()[1]
    #
    sheet2=workbook.sheet_by_index(1)
    sheet2=workbook.sheet_by_name('Sheet2')
    #工作表的名字，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)
    #读取日期
    rows=sheet2.row_values(3)
    #cols=sheet2.col_values(2)
    #if sheet2.cell().ctype == 3:
    date_value=xlrd.xldate_as_tuple(sheet2.cell_value(2,2),workbook.datemode)
    date_tmp=date(*date_value[:3]).strftime('%Y/%m/%d')
    print(rows,date_tmp)
    #
    print(sheet2.cell(1,0).value)
    print(sheet2.cell_value(1,0))
    print(sheet2.row(1)[0].value)
    #单元格数据类型 ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    print(sheet2.cell(1,0).ctype)
    #
    print(sheet2.merged_cells)
    #获取合并单元格的第一个单元格的值
    merge=[]
    for rlow,rhigh,clow,chigh in sheet2.merged_cells:
        merge.append([rlow,clow])
    print(merge)
    for index in merge:
        print(sheet2.cell_value(index[0],index[1]))
    return None


#设置单元格样式
def set_style(name,height,bold=False):
    style=xlwt.Style #初始化样式
    font=xlwt.Font() #为样式创建字体
    font.name=name
    font.bold=bold
    font.colour_index=4
    font.height=height
    style.font=font
    return style

#写excel文件
def write_excel():
    f=xlwt.Workbook() #创建工作簿
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    row0=[u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
    column0=[u'机票',u'船票',u'火车票',u'汽车票',u'其他']
    status=[u'预订',u'出票',u'退票',u'业务小计']
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])
    i,j=1,0
    while i<4*len(column0) and j<len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j])
        sheet1.write_merge(i,i+3,7,7)
        i+=4
        j+=1
    sheet1.write_merge(21,21,0,1,u'合计')

    i = 0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + i + 1, 1, status[j])
        i += 4

    f.save(r'D:\demo1.xls')  # 保存文件



if __name__ == '__main__':
    #write_excel()
    read_excel()


