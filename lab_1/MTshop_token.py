# 构造token来爬取,(使用json文件)
# base64解码和二进制解压
import base64
import zlib


# 解析token
def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string


if __name__ == '__main__':
    token = [
        'eJxVjstuqzAURf/F06LYxkAgUgeQ0MvzkoQ8QFUHbngnJgGcpKG6/35dqR1UOtLeZ501OJ+gdzMwwwgZCEnglvdgBvAETTQgAT6Ii6qqsqxPsUIMIoHDb6bIhgTe+90CzF4xwkiaqujti6wFeMWGjCSMdIF+uiK6rIj5slwhgYrzyzCDsBwnLK/5lbaTw5lB0YeqhgeMofgECJ1thC7y+J30O/nPHorXhTvUZSta7t2z5sij+2iuqiuMqyT3lDH961/cpPO5/7IZojDYtlraKOfij7JtjiFG8yGyya3cO0TLCiiXZtMG9+xkLi1rSM9r4sEqXch6Qcan5WXbMs9edilVt3ubIXYKrHUXxXSJu8bmL5auGLt8nXgqbntVM6N459ZGjGwSnIp4rGoe1h+Qre5Dn+3plG4e88ZtF0fM/KvR3iKHXuerfSf3FtRPtMvIIXmi2Q2N2chI+95somyc15phQmdlOlH0cGgRBszmflI+P4N//wEWi44a',
        'eJxVjstuozAUht/F26LYBkxDpC4gocN1SEIuoGoWbsw1MQngJC1V372u1C5GOtJ/Od/i/wC9x8AMI2QipIBb3oMZwBM0MYACxCA/hBBVQwgjYmIFHP7vDGIq4LXfLcDsBcusPBL077tZy+IFmypSMJrK6tfr0qu6vG/KkxCohLgMMwjLccLzWlxpOzmcOZR+qGp4wBjKJUDifCNxqccfpT8qfnMkp0t2qMtWuty/s+Yo4vtoraorTKo09/Ux+xtcvLQLRPC8GeIo3LZG1ujn4o++bY4RRvMhdrRbuXc1gxVQLa2mDe/sZC1te8jOa82HVbZQp4U2Piwv25b7zrLLKNnuHY74KbTXXZzQJe4aRzzbU93c5evUJ7jtiWHFyc6rzQQ5WngqkrGqRVS/Qb66Dz3b00e6eZ83Xrs4Yh5czfYWu/Q6X+07tbfh9EQ7ph3SB8puaGQj19rXZhOzcV4bpgXdleXG8btLiyjkjgjS8ukJfH4B4qqN+w==',
        'eJxdjktvozAURv+Lt0WxjYFCpC4gocNzSEIeoGoWbswzMQngJFNG89/HldrNSFf6vnvuWdw/YPAZmGOELIQUcC8GMAd4hmYGUIAY5UXXdZUg3USEmAo4/scsSwHvw34J5m8YYaQ86+jXJ9lI8IYtFSkYmRJ9d012VZPzaflSArUQ13EOYTXNeNGIG+1mxwuHso91A48YQ/kJkDrfSl3m6SvpV4rvPZavS3dsqk62Iniw9iSSx2Sv6xtM66wItCn/GV79rA9F+LodkzjadUbeapfyh7ZrTzFGizFxyb06eMRgJVQru+2iBzvbK8cZ88uGBLDOl6pZkulpdd11PHBXfU713cHliJ8jZ9MnKV3hvnXFq2Nq1r7YZIGOu0E37CTd+42VIpdE5zKd6kbEzW/I149xYAf6TLcfi9bvlifMw5vV3ROP3hbrQ68ODjTPtGfkmD1RdkcTmzjp3tttwqZFY1g29Na2lyQfHi3jiLsizKqXF/D3Hwp7jhM=',
        'eJxdjslyozAURf9FW1OWkAwYV/UCnAbjIQSw8ZDKgilGTM2shK78e5Qq96ZX5977zuL9Ba0Vg5WIkIqQAMakBSsgztFcBgLoO36RFISWqriUCZYFEP23KaIAwtZ/AqtXEauCIqG3n8Hl/VWUiCws5cWb8IiYR7wQfgBCiysg7fu6W0HIGJuXCe2HoJpHf0rIc5dSyH8A3C2P3OXMHwwe7P/1A3 aux29VzwlW1ZkJ2O4T5rjJnDN8j4r7 siT2Pfr02qbHbazmFs14Zuok8nCzoUXy6uR0x7GAiVJ1WFt JdW9uRjvvT02IPnZfth36NMSRtRyS1seyZe/w0pMS9pMQwUuNi1VW30/rMag6/SR4q0/V89p73 CyFtx57270mT/LiUNlR4zvt8SWnJhpnQTBUboP2n3p2lW73eiwgy/KxNA3aeekG6oVNWXiLswjGa3OmTe8b5/ockSpQGrHOsK 0nluPVGdt6m26X DrGwVkjH0========='
    ]



    for i in range(0, len(token)):
        token1 = decode_token(token[i])
        print(token1)
