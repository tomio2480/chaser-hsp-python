import CHaser #同じフォルダにあるCHaser.pyを読み込み

def main():
    value = [] #フィールド情報を保存するリスト
    client = CHaser.Client() #サーバと通信するためのインスタンス

    while True:
        value = client.get_ready() #サーバに行動準備が完了したと伝える

        # 自分の右側をSearchする例
        value = client.search_right()

        # ここから周辺情報を画面に表示します
        map_info = ""
        for cell in value:
            map_info += str(cell)
        print(map_info)
        # ここまで

if __name__ == "__main__":
    main()