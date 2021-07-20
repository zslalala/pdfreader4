import pdfplumber
import pandas as pd
from MergeTheCell import Merge

absolute_path = r"D:\PyProject\pdfreader\2.PDF"

def print_hi(Page_Begin,Page_End):

    Page_Begin = Page_Begin - 1
    Page_End = Page_End - 1

    #定义一个空列表用来存储数据
    final_table = []

    with pdfplumber.open(absolute_path) as pdf:
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
    pt.to_csv('数据2.csv',index=False)
    print(pt)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(89,92)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
