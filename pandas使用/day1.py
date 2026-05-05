import pandas as pd
#创建DataFrame数据
info_website = pd.DataFrame({'name': ['编程帮', 'c语言中文网', '微学苑', '92python'],
     'rank': [1, 2, 3, 4],
     'language': ['PHP', 'C', 'PHP','Python' ],
     'url': ['www.bianchneg.com', 'c.bianchneg.net', 'www.weixueyuan.com','www.92python.com' ]})
#创建ExcelWrite对象
with pd.ExcelWriter('website.xlsx') as writer:
    info_website.to_excel(writer)
print('输出成功')
