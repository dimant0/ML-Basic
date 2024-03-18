class Storage:
    def __init__(self):
        self.storage = 'local'
        self.path = None


class Cloud(Storage):
    def connect(self, login, password):
        pass

    def get_file(self, id):
        pass

