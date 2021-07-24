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

    mode = up # hsp版ではmodeではなくdirとなっていることに注意


    while(True):
        value = client.get_ready() # サーバに行動準備が完了したと伝える

        # ブロックをよける
        if value[up] == block: # 自らのupにブロックがあるとき
            mode = left # 左に動くモードに変更する
    
        if value[left] == block:
            mode = right
        
        if value[right] == block:
            mode = down

        if value[down] == block:
            mode = up

        # アイテムをとる
        if(value[up] == item): # 自らのupにアイテムがあるとき
            mode = up # 上に動くモードに変更する
        if(value[left] == item):
            mode = left
        if(value[right] == item):
            mode = right
        if(value[down] == item):
            mode = down

        # 実際に移動する
        if mode == left:
            value = client.walk_left()
        elif mode == right:
            value = client.walk_right()
        elif mode == down:
            value = client.walk_down()
        elif mode == up:
            value = client.walk_up()



if __name__ == "__main__":
    main()