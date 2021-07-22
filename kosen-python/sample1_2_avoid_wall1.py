import CHaser

def main():
    value = []
    client = CHaser.Client()

    while(True):
        value = client.get_ready()

        if(value[1] == 2): # 上のマスがブロックか確認
            # ブロックの場合、左にwalkする
            value = client.walk_left()
        else:
            # ブロックではない場合、上にwalkする
            value = client.walk_up()

if __name__ == "__main__":
    main()