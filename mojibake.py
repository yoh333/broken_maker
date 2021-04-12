
def suzuha(size, file):
    s = '失敗した'  # 任意の文字列
    s_size: int = 12  # 文字列のbyte数

    with open(file, 'w', encoding='utf-8') as f:
        i: int = 0
        while size > i:
            f.write(s)
            i += s_size
        else:
            f.write('わたしは失敗した')  # 任意の文字列にするときはelse文をコメントアウト


def yabainari(size, file):
    import struct
    import random

    with open(file, 'wb') as f:
        for i in range(0, size):
            f.write(struct.pack('B', random.randint(0, 255)))