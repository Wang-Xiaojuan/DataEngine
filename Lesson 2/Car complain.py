import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(page):
    # 请求URL
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'.format(page+1)
    # 得到页面的内容
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url,headers = headers,timeout = 10)
    content = html.text
    return(content)

def data_analysis(page):
    # 创建DataFrame
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    for num in range(page):
        content = get_soup(num)
        # 通过content创建BeautifulSoup对象
        soup = BeautifulSoup(content, 'html.parser')
        # 找到完整的投诉信息框\n",
        temp = soup.find('div',class_="tslb_b")
        tr_list = temp.find_all('tr')
        for tr in tr_list:
            # 提取汽车投诉信息
            temp = {}
            td_list = tr.find_all('td')
            if len(td_list) > 0:
                id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
                temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'], temp['problem'],temp['datetime'],temp['status'] = id, brand, car_model, type, desc, problem, datetime, status
                df = df.append(temp,ignore_index = True)
    return df
                         
page = 20 
df = data_analysis(page) 
print (df)  
