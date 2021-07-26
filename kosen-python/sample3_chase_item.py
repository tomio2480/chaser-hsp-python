import CHaser #同じフォルダにあるCHaser.pyを読み込み

def main():
    value = [] #フィールド情報を保存するリスト
    client = CHaser.Client() #サーバと通信するためのインスタンス

    mode = "up" #何もなければ上へ進むよう、upをセット

    while True:
        value = client.get_ready() #サーバに行動準備が完了したと伝える

        #壁を見つけたら回避行動をセット
        if mode == "up" and value[1] == 2:
            mode = "left"
        if mode == "left" and value[3] == 2:
            mode = "down"
        if mode == "down" and value[7] == 2:
            mode = "right"
        if mode =="right" and value[5] == 2:
            mode = "up"
        if mode == "up" and value[1] == 2:
            mode = "left"

        #アイテムがあればそちらへ優先的に進む
        if value[1] == 3:
            mode = "up"
        if value[3] == 3:
            mode = "left"
        if value[5] == 3:
            mode = "right"
        if value[7] == 3:
            mode = "down"

        #セットされたmodeに従って移動命令を出す
        if mode == "up":
            client.walk_up()
        elif mode == "left":
            client.walk_left()
        elif mode == "down":
            client.walk_down()
        elif mode == "right":
            client.walk_right()

if __name__ == "__main__":
    main() 