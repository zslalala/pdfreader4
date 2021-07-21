import pdfplumber
import pandas as pd
from MergeTheCell import Merge

relative_path = "2016.PDF"

def PrintFileToExcel(Page_Begin,Page_End,file_name):

    file_name = file_name + '.csv'
    Page_Begin = Page_Begin - 1
    Page_End = Page_End - 1

    #定义一个空列表用来存储数据
    final_table = []

    with pdfplumber.open(relative_path) as pdf:
        for i in range(Page_Begin,Page_End + 1,1):
            now_page = pdf.pages[i]
            tables = now_page.extract_tables()
            if(i == Page_Begin):
                t = tables[-1]
            else:
                t = tables[0]

            t_afterdeal = Merge(t)
            final_table.extend(t_afterdeal)

    #获取列表抬头
    title = final_table[0]
    #删除列表抬头
    del(final_table[0])
    pt = pd.DataFrame(final_table,columns=title)
    print(pt.dtypes)
    # pt.to_csv('数据2.csv',index=False)
    pt.to_csv(file_name,mode = 'a',index=False,encoding='utf-8')
    print(pt)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PrintFileToExcel(37, 38, '合并资产负债表')
    PrintFileToExcel(40, 41, '合并利润表')
    PrintFileToExcel(43, 44, '合并现金流量表')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
