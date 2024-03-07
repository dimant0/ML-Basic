class Storage:
    def __init__(self):
        self.storage = 'local'
        self.path = None


class Cloud(Storage):
    def __init__(self):
        super().__init__()
        self.storage = 'cloud'
        self.is_connected = False

    def _connect(self, login, password):
        print(f'Соединение с облаком [login={login}, password={password}]')
        self.is_connected = True

    def get_file(self, id):
        if self.is_connected:
            print(f'Получение файла с id={id} из облака')

        else:
            print(f'Сначала необходимо подключится к облаку')
