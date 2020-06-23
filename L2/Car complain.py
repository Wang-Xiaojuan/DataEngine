{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-8-625ddbbb1bdd>, line 12)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-8-625ddbbb1bdd>\"\u001b[1;36m, line \u001b[1;32m12\u001b[0m\n\u001b[1;33m    return(content)\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "def get_soup(page):\n",
    "    # 请求URL\n",
    "    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'.format(page+1)\n",
    "    # 得到页面的内容\n",
    "    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}\n",
    "    html = requests.get(url,headers = headers,timeout = 10)\n",
    "    content = html.text\n",
    "return(content)\n",
    " \n",
    "def data_analysis(page):\n",
    "    # 创建DataFrame\n",
    "    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])\n",
    "    for num in range(page):\n",
    "        content = get_soup(num)\n",
    "        # 通过content创建BeautifulSoup对象\n",
    "        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')\n",
    "        # 找到完整的投诉信息框\n",
    "        temp = soup.find('div',class_=\"tslb_b\")\n",
    "        tr_list = temp.find_all('tr')\n",
    "        for tr in tr_list:\n",
    "            # 提取汽车投诉信息\n",
    "            temp = {}\n",
    "            td_list = temp.find_all('td')\n",
    "            if len(td_list) > 0:\n",
    "                id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text\n",
    "                temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'], temp['problem'],temp['car_model'],temp['datetime'],temp['status'] = id, brand, car_model, type, desc, problem, datetime, status \n",
    "                df = df.append(temp,ignore_index = True)\n",
    "return df\n",
    "\n",
    "page = 2\n",
    "df = data_analysis(page)\n",
    "print (df)                           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# 请求URL\n",
    "def get_page_content(request_url):\n",
    "    # 得到页面的内容\n",
    "    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}\n",
    "    html=requests.get(request_url,headers=headers,timeout=10)\n",
    "    content = html.text\n",
    "    # 通过content创建BeautifulSoup对象\n",
    "    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')\n",
    "    return soup\n",
    "\n",
    "#分析当前页面的投诉\n",
    "def analysis(soup):\n",
    "    # 找到完整的投诉信息框\n",
    "    temp = soup.find('div',class_=\"tslb_b\")\n",
    "    # 创建DataFrame\n",
    "    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])\n",
    "\n",
    "    tr_list = temp.find_all('tr')\n",
    "    for tr in tr_list:\n",
    "        # 提取汽车投诉信息\n",
    "        temp = {}\n",
    "        td_list = tr.find_all('td')\n",
    "        #第一个tr没有td，其余都有8个td    \n",
    "        if len(td_list) > 0:\n",
    "            #解析第一个字段内容\n",
    "            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text\n",
    "            #放到DataFrame中\n",
    "            temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'],temp['problem'],temp['datetime'],temp['status'] = id, brand, car_model, type, desc, problem, datetime, status\n",
    "            df = df.append(temp,ignore_index = True)\n",
    "    return df\n",
    "\n",
    "\n",
    "page_num = 2\n",
    "base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'\n",
    "\n",
    "\n",
    "# 创建DataFrame\n",
    "result = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])\n",
    "\n",
    "for i in range(page_num):\n",
    "    request_url = base_url + str(i+1) + '.shtml'\n",
    "    soup = get_page_content(request_url)\n",
    "    df = analysis(soup)\n",
    "    result = result.append(df)\n",
    "    \n",
    "result.to_csv('result.csv',index = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
