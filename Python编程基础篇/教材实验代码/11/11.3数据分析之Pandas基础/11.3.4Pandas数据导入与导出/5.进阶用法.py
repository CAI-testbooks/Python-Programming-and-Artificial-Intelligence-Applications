import pandas as pd


df = pd.DataFrame({
    '列名1': [1, 2, 3],
    '列名2': ['A', 'B', 'C'],
    '列名3': [4.5, 5.5, 6.5]
})
# 1.导出部分列
df.to_csv('data.csv', columns=['列名1', '列名2'], index=False)  # 导出指定列到CSV文件，不包含索引

# 2.处理中文和特殊字符
df.to_csv('output_utf8.csv', encoding='utf-8-sig', index=False)  # 使用UTF-8编码导出，适合中文字符