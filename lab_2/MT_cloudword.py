import datetime
import time
from time import sleep

import jieba
import pandas as pd
from wordcloud import WordCloud
from matplotlib.image import imread
import re
import matplotlib.pyplot as plt


def cloudword(word, maxword):
    stopwords = pd.read_csv("./cloudword/chineseStopwords.txt", index_col=False, quoting=3, sep="\t",
                            names=['stopword'], encoding='utf-8')  # 噪声词
    Mask = imread('./cloudword/image/mask/cn.jpg')   # 遮罩

    outpath = './cloudword/image/output/cn.png'
    print("正在分词")
    cut_text = " ".join(jieba.cut(word))
    print("正在统计高频词汇")
    wordcloud0 = WordCloud(
        background_color="white",
        font_path="./cloudword/font/msyhbd.ttc",
        mask=Mask,
        max_words=maxword,
        max_font_size=70,
        min_font_size=8,  # 显示的最小的字体大小
        scale=5,
        stopwords=stopwords  # 过滤噪声词

    )
    print("正在生成词云...")
    # 产生词云
    word_cloud = wordcloud0.generate_from_text(cut_text)
    word_cloud.to_file(outpath)  # 保存图片
    # 显示图片
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('./data/all_comment.csv')
    df.to_csv('./data/comments.txt', encoding='utf-8', header=None, index=None, sep=' ')
    sleep(2)
    print("文本转换完成")
    comment_text = open('./data/comments.txt', 'r', encoding='utf-8').read()
    print("正在分析评论组成成分")
    start = time.time()
    cloudword(comment_text, 100)
    end = time.time()
    print("词云已成功生成!用时 %d s" % (end-start))
