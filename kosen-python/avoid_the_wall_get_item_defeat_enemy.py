import CHaser # 同じフォルダにあるCHaser.pyを読み込み

def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバと通信するためのインスタンス

    # マスの状態を変数に格納する
    blank = 0
    enemy = 1
    block = 2
    item = 3


    # 自らの周辺マスの要素の要素番号を変数に格納する。
    '''
    [ ][x][x]
    [ ][C][♡]
    [H][ ][ ]
    このときは、[0, 2, 2, 0, 0, 3, 1, 0, 0] が返る。
    それぞれの要素を確認するためには先頭から0,1,2,3...8までの要素番号を指定する。
    
    要素番号とマスの対応関係はこのようになる。
    [0][1][2]
    [3][4][5]
    [6][7][8]
    '''
    # 上下左右の配列番号を変数に格納する
    up = 1
    left = 3
    right = 5
    down = 7

    while(True):
        value = client.get_ready() # サーバに行動準備が完了したと伝える
        dir = up
        mode = "walk"

        # ブロックをよける
        if value[up] == block: # 自らのupにブロックがあるとき
            dir = left # 左に動くモードに変更する
    
        if value[left] == block:
            dir = right
        
        if value[right] == block:
            dir = down

        if value[down] == block:
            dir = up

        # アイテムをとる
        if(value[up] == item): # 自らのupにアイテムがあるとき
            dir = up # 上に動くモードに変更する

        if(value[left] == item):
            dir = left

        if(value[right] == item):
            dir = right

        if(value[down] == item):
            dir = down

        # 敵のほうを向いて、モードを変える
        if value[up] == enemy: # 上方向に敵がいたら
            dir = up #上に向く
            mode = "put"
        
        if value[left] == enemy:
            dir = left
            mode = "put"
        
        if value[right] == enemy:
            dir = right
            mode = "put"

        if value[down] == enemy:
            dir = down
            mode = "put"

        # モードをもとに行動する
        if mode == "walk":
            # 実際に移動する
            if dir == left:
                value = client.walk_left()
            elif dir == right:
                value = client.walk_right()
            elif dir == down:
                value = client.walk_down()
            elif dir == up:
                value = client.walk_up()
        elif mode == "put":
            # 実際に移動する
            if dir == left:
                value = client.put_left()
            elif dir == right:
                value = client.put_right()
            elif dir == down:
                value = client.put_down()
            elif dir == up:
                value = client.put_up()


if __name__ == "__main__":
    main()