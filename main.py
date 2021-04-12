
import mojibake as moji


def main(func):
    file_name = input("ファイル名を入力してください:")
    ext = input("拡張子を入力してください:")
    file = file_name + '.' + ext

    # ファイルサイズMBをBに変換
    size = float(input("ファイルサイズを入力してください(MB):"))
    size = int(size*1024 ** 2)

    # 任意のファイル作成プログラムに引数を渡す
    func(size, file)


if __name__ == '__main__':
    main(moji.yabainari)
