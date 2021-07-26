import CHaser #同じフォルダにあるCHaser.pyを読み込み

def main():
    value = [] #フィールド情報を保存するリスト
    client = CHaser.Client() #サーバと通信するためのインスタンス

    while True:
        value = client.get_ready() #サーバに行動準備が完了したと伝える

        #壁がなければそちらへ進む
        if value[1] != 2:
            value = client.walk_up()
        elif value[3] != 2:
            value = client.walk_left()
        elif value[7] != 2:
            value = client.walk_down()
        elif value[5] != 2:
            value = client.walk_right()

        print(value) #コンソールに結果を記録

if __name__ == "__main__":
    main() 