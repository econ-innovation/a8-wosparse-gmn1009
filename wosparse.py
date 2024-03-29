import pandas as pd
filepath = 'qje2014_2023.txt'
df = pd.read_csv(filepath, sep='\t')
papers_basic_info = df[['UT', 'PY', 'SO', 'SN', 'DI', 'VL', 'IS']].copy()
papers_abstracts = df[['UT', 'AB']].copy()
papers_titles = df[['UT', 'TI']].copy()
papers_authors = df[['UT', 'AU']].copy()  # 这里只是简单复制了包含作者信息的列
papers_basic_info.to_csv('papers_basic_info.csv', index=False)
papers_abstracts.to_csv('papers_abstracts.csv', index=False)
papers_titles.to_csv('papers_titles.csv', index=False)
papers_authors.to_csv('papers_authors.csv', index=False)
