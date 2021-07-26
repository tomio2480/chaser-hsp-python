import CHaser

def main():
    value = []
    client = CHaser.Client()

    while True:
        value = client.get_ready()
        value = client.put_up()

if __name__ == "__main__":
    main()