



class MediaFile:
    def __init__(self, name):
        self.name = name
        self.size = None
        self.owner = None
        self.meta_data = None
        self.path = None
        self.created_at = None

    def create(self):
        self.path = '/new/path'
        print(f'Создание нового файла {self.name}')
        self._type_file()

    def open(self, path):
        self.path = path
        print(f'Открытие файла c path: {self.path}')
        self._type_file()

    def update(self, path):
        self.open(path)
        print(f'Работа с файлом {self.path}')

    def remove(self, path):
        self.open(path)
        print(f'Удаление файла {self.path}')
        self.path = None

    def _type_file(self):
        print(f'Тип файла {self.meta_data}')


class AudioFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'audio'


class VideoFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'video'


class PhotoFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'photo'

    def resize(self):
        print(f'Изменение размера изображения {self.path}')
