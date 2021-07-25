import CHaser

def main():
    value = []
    client = CHaser.Client()

    move_mode = "up"
    put_mode = "off"

    while(True):
        value = client.get_ready()
        
        if move_mode == "up" and value[1] == 2:
            move_mode = "left"
        if move_mode == "left" and value[3] == 2:
            move_mode = "down"
        if move_mode == "down" and value[7] == 2:
            move_mode = "right"
        if move_mode == "right" and value[5] == 2:
            move_mode = "up"
        if move_mode == "up" and value[1] == 2:
            move_mode = "left"

        if value[1] == 3:
            move_mode = "up"
        if value[3] == 3:
            move_mode = "left"
        if value[5] == 3:
            move_mode = "right"
        if value[7] == 3:
            move_mode = "down"
        
        if value[1] == 1:
            put_mode = "up"
        elif value[3] == 1:
            put_mode = "left"
        elif value[5] == 1:
            put_mode = "right"
        elif value[7] == 1:
            put_mode = "down"
        else:
            put_mode = "off"
        
        if put_mode == "off":
            if move_mode == "up":
                value = client.walk_up()
            elif move_mode == "left":
                value = client.walk_left()
            elif move_mode == "down":
                value = client.walk_down()
            elif move_mode == "right":
                value = client.walk_right()
        else:
            if put_mode == "up":
                value = client.put_up()
            elif put_mode == "left":
                value = client.put_left()
            elif put_mode == "down":
                value = client.put_down()
            elif put_mode == "right":
                value = client.put_right()


if __name__ == "__main__":
    main()