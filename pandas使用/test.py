import pandas as pd

def find_last_empty_row_clear(file_path, sheet_name=0):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    # 删除全空行
    non_empty = df.dropna(how='all')
    
    if non_empty.empty:
        return 1  # 没有任何数据，第一个空行就是第1行
    
    # 最后一个非空行的索引
    last_index = non_empty.index[-1]
    
    # 转换为 Excel 行号（索引+1 是当前行）
    last_data_row = last_index + 1
    
    # 下一个空行
    next_empty_row = last_data_row + 1
    
    return next_empty_row


file_path = r'C:\Users\35382\Desktop\fortest.xlsx'
# print(find_last_empty_row_clear(file_path))

data = pd.read_excel(file_path,header=None,usecols=[0])
print(data)