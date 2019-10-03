import logging
import random
import time
import requests
import json
import csv

logging.basicConfig(level=logging.INFO)


def get_poiid():
    with open(r'../lab_1/武汉美食.csv', 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        column_id = [row[0] for row in reader]
        return column_id


def write_file(poiid, total_comment, total_star):
    with open(r'comments/{}.csv'.format(poiid), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['评论', '打分'])
        for i in range(0, len(total_comment)):
            writer.writerow([total_comment[i], total_star[i]])


def get_json(poiid):
    # 休眠两秒，从lab1中的美食poiid数据获取商户页面
    time.sleep(2)
    url = 'http://www.meituan.com/meishi/api/poi/getMerchantComment?' \
          'uuid=095e5a{}50d417a92d9.1526123380.1.0.0&platform=1&partner=126&' \
          'originUrl=http%3A%2F%2Fwww.meituan.com%2Fmeishi%2F4955158%2F&riskLevel=1&optimusCode=1&' \
          'id={}&userId=&offset=0&pageSize=10&sortType=1'.format(random.randint(100, 999), poiid)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 "
                      "Safari/537.36 "
    }
    print("正在抓取编号为{}的店铺".format(poiid))
    response = requests.get(url, headers=header)
    json_data = json.loads(response.content.decode('UTF-8'))
    return json_data


def get_page_number(json_data):
    page_number_total = json_data['data']['total']
    page_number = int(page_number_total / 10 + 1)
    return page_number


# 一页十条数据
def get_one_page_comment(json_data):
    comments_list = json_data['data']['comments']
    comments = []
    star = []
    onepage = [comments, star]
    for j in range(0, 10):
        PRS = comments_list[j]  # 字典
        comments.append(PRS['comment'].strip('"'))
        star.append(PRS['star'])
    return onepage


# 获取评论信息
def one_shop_all_comment(id, i):
    # 循环页数，获取每页评论信息
    for j in range(1, page_num):
        try:                    # 捕获异常，避免因为空评论等问题报错
            logging.info("正在抓取第{}家店铺第{}页".format(i, j))

            # 每页的offset值不同
            url = 'http://www.meituan.com/meishi/api/poi/getMerchantComment?' \
                  'uuid=095e5a{}50d417a92d9.1526123380.1.0.0&platform=1&partner=126&' \
                  'originUrl=http%3A%2F%2Fwww.meituan.com%2Fmeishi%2F4955158%2F&riskLevel=1&optimusCode=1&' \
                  'id={}&userId=&offset={}&pageSize=10&sortType=1'.format(random.randint(100, 999), id[i], (j - 1) * 10)
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 "
                              "Safari/537.36 "
            }

            response = requests.get(url, headers=header)
            json_data = json.loads(response.content.decode('UTF-8'))        # 获取该评论页面的json数据
            this_page_comment = get_one_page_comment(json_data)             # 打印后发现是一个二维数组
            for k in range(0, 10):
                total_comment.append(this_page_comment[0][k])               # 直接访问每个评论
                total_star.append(this_page_comment[1][k])
        except TypeError:
            pass
    return


if __name__ == '__main__':
    id = get_poiid()
    for i in range(1, len(id)):
        json_data = get_json(id[i])             # 这家店首页的json数据
        page_num = get_page_number(json_data)   # 这家店的评论页数
        total_star = []                         # 这家店的总星列表
        total_comment = []                      # 这家店的总评论列表
        one_shop_all_comment(id, i)             # 获取这家店的评论信息
        write_file(id[i], total_comment, total_star)   # 写入评论信息到文件
