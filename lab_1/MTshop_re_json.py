# 使用正则表达式来爬取,(使用json文件)
import csv
import json
import requests
from bs4 import BeautifulSoup
import re
import time
import logging
logging.basicConfig(level=logging.INFO)


# 返回网站html
def init(mt_url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 "
                      "Safari/537.36 "
    }
    # proxy = {"HTTP": "1.197.203.26:9999", "HTTPs": "182.34.37.120:49566"}
    response = requests.get(mt_url, headers=header)
    if response.status_code == 200:
        logging.info("页面连接成功，正在抓取...")
    else:
        logging.info("网站连接失败，请检查网络连接")
    data = response.content.decode("utf-8")
    return data


if __name__ == '__main__':
    PAGE = 5
    B_PERPAGE = 15
    id_list = []
    title_list = []
    score_list = []
    address_list = []
    price_list = []
    comment_list = []

    # 获取商户信息，分别存入列表
    for i in range(0, PAGE):
        mt_url = 'https://wh.meituan.com/meishi/pn' + str(i + 1) + '/'
        data = init(mt_url)
        print("")
        logging.info("正在抓取" + mt_url)
        soup = BeautifulSoup(data, 'html.parser')
        js = soup.find_all("script")
        b_msg = js[14].text
        string = re.findall("window._appState = (.*);", b_msg)[0]
        result = json.loads(string, encoding="utf-8")
        source = result["poiLists"]
        source = source["poiInfos"]
        for item in source:
            id_list.append(item['poiId'])
            title_list.append(item['title'])
            score_list.append(item['avgScore'])
            address_list.append(item['address'])
            price_list.append(item['avgPrice'])
            comment_list.append(item['allCommentNum'])

            time.sleep(2)

    # 写入为csv
    with open(r'武汉美食-json.csv', "w", newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['poiID', '商家名', '平均得分', '地址', '平均价格', '获得评论总数'])
        for i in range(0, PAGE * B_PERPAGE - 1):
            writer.writerow((id_list[i], title_list[i], score_list[i], address_list[i], price_list[i], comment_list[i]))

