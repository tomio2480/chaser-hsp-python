import CHaser

def main():
    value = []
    client = CHaser.Client()

    while(True):
        value = client.get_ready()
        # ここから周辺情報を画面に表示します
        map_info = ""
        for cell in value:
            map_info += str(cell)
        print(map_info)
        # ここまで
        value = client.walk_up()

if __name__ == "__main__":
    main()