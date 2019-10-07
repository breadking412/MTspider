#  进行文件预处理（去除重复，nan文件），打标签
import csv
import logging
import pandas as pd
import os


logging.basicConfig(level=logging.INFO)


# 对comments文件夹内文件按照序号大小排序, 返回文件名的列表
# 不写入文件也可以，这里写入文件方面查阅
def get_file_name_list():
    f = open("./shop_id_name.txt", 'w')  # 先创建一个空的文本
    path = "./comments/"  # 指定需要读取文件的目录
    files = os.listdir(path)  # 采用listdir来读取所有文件
    files.sort()  # 排序
    file_name_list = []  # 创建一个空列表
    for file_ in files:  # 循环读取每个文件名
        if not os.path.isdir(path + file_):  # 判断该文件是否是一个文件夹
            f_name = str(file_)
            file_name_list.append(f_name)  # 把当前文件名返加到列表里
            f.write(f_name + '\n')  # 写入之前的文本中

    return files


def merge(filename):
    df = pd.read_csv('comments/{}'.format(filename))  # 返回一个DataFrame类型的文件
    df = df.dropna(axis=0)  # 去除缺省值
    df = df.drop_duplicates(['评论'])  # 去除重复行
    df['情感标签'] = df['打分'].map(lambda make_label: 1 if make_label > 30 else 0)
    return df


def iterator_shop_comment(files_list):
    # 迭代器
    one_shop_comments = map(merge, files_list)
    for i in one_shop_comments:
        i.to_csv('./data/all_comment.csv', mode='a', encoding='utf-8', header=False, index=False)


def write_file(files_list):
    with open('./data/all_comment.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['评论', '打分', '情感标签'])
    iterator_shop_comment(files_list)
    print("数据集制作完成")


if __name__ == '__main__':
    files_name = get_file_name_list()
    write_file(files_name)


















# # 将文件分为好评和差评（发现没啥用，爷白费事写了）
# def pre_file(file_name_list):
#     for i in range(len(file_name_list)):
#         if i % 15 == 0:
#             print("正在获取第{}家商店的评论信息,".format(i))
#         df = pd.read_csv('comments/{}'.format(file_name_list[i]))  # 返回一个DataFrame类型的文件
#
#         df = df.dropna(axis=0)  # 去除缺省值
#         df = df.drop_duplicates()  # 去除重复行
#         df['情感标签'] = df['打分'].map(lambda make_label: 1 if make_label > 30 else 0)
#
#         # 写入进csv
#         df_1 = df[df.情感标签 == 1]
#         df_2 = df[df.情感标签 == 0]
#         df_1.to_csv("好评.csv", mode='a', index=False, header=False)
#         df_2.to_csv("差评.csv", mode='a', index=False, header=False)
#     print("")
#     logging.info("数据预处理完成")
#
# 方法2
# # 将全部评论放在一个csv文件中，打上标签
# def all_comment(file_name_list):
#     df_all = pd.DataFrame(columns=['评论', '打分', '情感标签'])
#     for i in range(len(file_name_list)):
#         # for i in range(15):
#         print(i)
#         df = pd.read_csv('comments/{}'.format(file_name_list[i]))  # 返回一个DataFrame类型的文件
#         df = df.dropna(axis=0)  # 去除缺省值
#         df = df.drop_duplicates()  # 去除重复行
#         df['情感标签'] = df['打分'].map(lambda make_label: 1 if make_label > 30 else 0)
#         df_all = df_all.append(df)
#
#         df_all.to_csv("数据集.csv", mode='a', index=False, header=True)
#     print("")
#     logging.info("数据集制作完成")
#
