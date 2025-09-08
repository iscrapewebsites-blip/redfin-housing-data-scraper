import page_scrap
from pathlib import Path

datap = Path.cwd() / 'data'

data = []
for file in datap.iterdir():
     file_dir = f'data/{file.name}'
     item = page_scrap.get_xp_data(file_dir)
     if item!='':
          data.append(item)


import data_conv
data_conv.to_json(data)
data_conv.to_csv(data)
data_conv.to_excel(data)
