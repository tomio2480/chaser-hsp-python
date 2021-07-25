import CHaser

def main():
    value = []
    client = CHaser.Client()

    while(True):
        value = client.get_ready()

        blank = 0
        enemy = 1
        block = 2
        item = 3

        up = 1
        left = 3
        right = 5
        down = 7

        # ランダムを使う準備
        import random

        # [] 内にある 4 つの値からひとつ選ぶ
        # "pray"er として勝つことを祈ろう！！
        dir = random.choice([up, left, right, down])
        
        mode = "walk"

        # ブロックをよける
        if dir == up and value[up] == block: # 上方向(value[1])に壁(2)があったら
            dir = left # 左に向く
        if dir == left and value[left] == block:
            dir = down
        if dir == down and value[down] == block:
            dir = right
        if dir == right and value[right] == block:
            dir = up
        
        # アイテムをとる
        if value[up] == item:
            dir = up
        if value[left] == item:
            dir = left
        if value[right] == item:
            dir = right
        if value[down] == item:
            dir = down
        
        # 敵のほうを向いて、モードを変える
        if value[up] == enemy: # 上方向に敵がいたら
            dir = up
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
            # 実際にブロックをおく
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