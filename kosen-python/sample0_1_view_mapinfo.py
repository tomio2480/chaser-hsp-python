import CHaser

def main():
    value = []
    client = CHaser.Client()

    while True:
        value = client.get_ready()
        # ここから周辺情報を画面に表示します
        map_info = ""
        for cell in value:
            map_info += str(cell)
        print(map_info)
        # ここまで
        value = client.walk_up()

"""
【参考】
今回は HSP 版に合わせた書き方をしていますが，
Python の場合，10 行目から 13 行目を，
次の一行に置きかえても周辺情報を見ることができます．

print(value)
"""

if __name__ == "__main__":
    main()