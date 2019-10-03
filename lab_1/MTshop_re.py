# 使用正则表达式来爬取,(不用json)
import re
import requests
import csv
import logging


# 获取某一页商家信息,
def get_shop_info(url, headers):
    response = requests.get(url, headers=headers)
    id_list = []
    title_list = []
    score_list = []
    address_list = []
    price_list = []
    comment_list = []

    # 使用正则表达式抓取每项信息
    b_poiId = re.findall(r'"poiId":(\d+),', response.text)  # 商家id，值为列表
    b_title = re.findall(r'"frontImg".*?title":(.*?),', response.text) # 商家名字
    b_avgScore = re.findall(r'"avgScore":(.*?),', response.text)  # 平均分
    b_allCommentNum = re.findall(r'"allCommentNum":(\d+),', response.text)  # 评论总数
    b_address = re.findall(r'"address":(.*?),', response.text)  # 商家地址
    b_avgPrice = re.findall(r'"avgPrice":(\d+),', response.text)  # 平均价格
    for item in range(len(b_poiId)):
        # strip()函数用来去掉字符串左右的字符
        id_list.append(b_poiId[item])
        title_list.append(b_title[item].strip('"'))
        score_list.append(b_avgScore[item])
        address_list.append(b_address[item].strip('"'))
        price_list.append(b_avgPrice[item])
        comment_list.append(b_allCommentNum[item])

    b_info = [id_list, title_list, score_list, address_list, price_list, comment_list]
    return b_info


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 "
                      "Safari/537.36 "
    }
    with open(r'武汉美食.csv', "w", newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['poiID', '商家名', '平均得分', '地址', '平均价格', '获得评论总数'])
        # 爬取每页的商家
        for n in range(1, 50):
            url = 'https://wh.meituan.com/meishi/pn' + str(n) + '/'
            print("正在获取第{}页商家信息".format(n))
            b_info = get_shop_info(url, headers)

            id_list = b_info[0]
            title_list = b_info[1]
            score_list = b_info[2]
            address_list = b_info[3]
            price_list = b_info[4]
            comment_list = b_info[5]

            for i in range(len(id_list)):
                writer.writerow(
                    [id_list[i], title_list[i], score_list[i], address_list[i], price_list[i], comment_list[i]])




