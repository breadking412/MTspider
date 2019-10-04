# 读取文件，划分测试集和训练集并进行验证
import pandas as pd


def MT_kfold():
    data = pd.read_csv('data/all_comment.csv')
    print(data.shape)


if __name__ == '__main__':
    MT_kfold()
