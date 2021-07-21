
#合并字段函数
def MergeField(table,begin_index,end_index,field):
    #初始化返回值
    ret = ""
    #合并单元格
    for i in range(begin_index,end_index):
        #如果字段不为NONE和空
        if table[i][field] is not None and len(table[i][field]) > 0:
            ret += table[i][field]
    return ret

#开始合并,适用于三列表格
def MergeFuc(table,begin_index,end_index):
    ret0 = MergeField(table,begin_index,end_index,0)
    ret1 = MergeField(table,begin_index,end_index,1)
    ret2 = MergeField(table,begin_index,end_index,2)
    Ret = [ret0,ret1,ret2]
    return Ret

#合并入口逻辑函数
def Merge(table):
    print(table)
    Ret = []
    begin_index = 0
    end_index = len(table) - 1
    #length代表table的长度
    length = len(table)
    switch = True
    for i,cells in enumerate(table):
        if (switch is True) and ((cells[0] is None)):
            begin_index = i - 1
            switch = False
        if (switch is False) and ((cells[0] is not None) and (cells[1] is not None) and (cells[2] is not None)):
            end_index = i
            del(Ret[-1])
            tempcell = MergeFuc(table,begin_index,end_index)
            Ret.append(tempcell)
            switch = True
        if switch is True:
            Ret.append(cells)
        #处理位于末尾的不连贯问题
        if switch is False and i == length - 1:
            end_index = i + 1
            del(Ret[-1])
            tempcell = MergeFuc(table, begin_index, end_index)
            Ret.append(tempcell)
            switch = True

    return Ret



