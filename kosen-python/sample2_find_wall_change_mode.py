import CHaser

def main():
    value = []
    client = CHaser.Client()

    mode = "up" #最初のモードを指定する。

    while(True):
        value = client.get_ready()

        # 指定されたモードの方向にブロックがあるかを確認する。
        # ブロックがあればモードを変更する
        if mode == "up" and value[1] == 2:
            mode = "left"
        
        if mode == "left" and value[3] == 2:
            mode = "down"
        
        if mode == "down" and value[7] == 2:
            mode = "right"
        
        if mode == "right" and value[5] == 2:
            mode = "up"
            
       # modeに入っている値で行動を決める 
        if mode == "up":
            value = client.walk_up()
        elif mode == "left":
            value = client.walk_left()
        elif mode == "down":
            value = client.walk_down()
        elif mode == "right":
            value = client.walk_right()

if __name__ == "__main__":
    main()