from  lxml import html
import json
import data_conv

page = ''
with open('page.html', 'r', encoding='utf-8') as f:
     page = f.read()

tree = html.fromstring(page)

# get items
x = '//div[contains(@class, "HomeCardContainer")]'
elements = tree.xpath(x)

data = []
# Testing if we're able to fetch data accurately
for el in elements:
     item = {}
     # xpath always returns a list so use [0]
     # we might get empty list so use try-except block while fetching elements.. to prevent code from breaking
     k5 = 'Address'
     try:
          x5 = './/div[contains(@class, "bp-Homecard__Address")]'
          p5 = el.xpath(x5)[0] # get property
          p5 = ' '.join(p5.text.split())     # clean & format it
          item[k5] = f'{p5}'
     except:
          item[k5] = ''
          pass

     k1 = 'Price'
     try:
          x1 = './/span[contains(@class, "bp-Homecard__Price--value")]'
          p1 = el.xpath(x1)[0]
          p1 = ' '.join(p1.text.split())
          item[k1] = f'{p1}'
     except:
          item[k1] = ''
          pass
     
     k2 = 'No. of Beds'
     try:
          x2 = './/span[contains(@class, "bp-Homecard__Stats--beds text-nowrap")]'
          p2 = el.xpath(x2)[0]
          p2 = ' '.join(p2.text.split())
          item[k2] = f'{p2}'
     except:
          item[k2] = ''
          pass
     
     k3 = 'No. of Baths'
     try:
          x3 = './/span[contains(@class, "bp-Homecard__Stats--baths")]'
          p3 = el.xpath(x3)[0]
          p3 = ' '.join(p3.text.split())
          item[k3] = f'{p3}'
     except:
          item[k3] = ''
          pass
     
     k4 = 'Area'
     try:
          x4 = './/span[contains(@class, "bp-Homecard__Stats--sqft")]'
          p4 = el.xpath(x4)[0]
          p4 = ' '.join(p4.text_content().split())     
          p4 = p4 
          item[k4] = f'{p4}'
     except:
          item[k4] = ''
          pass

     k6 = 'Extra Info'
     try:
          x6 = './/span[contains(@class, "KeyFacts-item")]'
          p6 = el.xpath(x6)[0]
          p6 = ' '.join(p6.text.split())
          p61 = el.xpath(x6)[1]
          p61 = ' '.join(p61.text.split())
          p62 = el.xpath(x6)[0]
          p62 = ' '.join(p62.text.split())
          item[k6] = f'{p6} | {p61} | {p62}'
     except:
          item[k6] = ''
          pass


     # print(item)

     if len(item)!=0: # avoid empty items
          data.append(item)


# ## writing to different data formats
# data_conv.to_json(data)
# data_conv.to_csv(data)
data_conv.to_excel(data)
# # data_conv.to_sheet(data)