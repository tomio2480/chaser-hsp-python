import CHaser #同じフォルダにあるCHaser.pyを読み込み

def main():
    value = [] #フィールド情報を保存するリスト
    client = CHaser.Client() #サーバと通信するためのインスタンス

    while(True):
        value = client.get_ready() #サーバに行動準備が完了したと伝える

        # 自分の右側をSearchする例
        value = client.search_right()

        print(value) #コンソールに検索結果を記録

if __name__ == "__main__":
    main()