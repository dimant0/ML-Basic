class MediaFile:
    """Базовый класс, где описываются основные методы работы с медиа-файлами. У базового класса есть список свойств,
    имя, размер, собственник, метаданные, полный путь файла, дата и время создания
    """

    def __init__(self, name):
        self.name = name
        self.size = None
        self.owner = None
        self.meta_data = None
        self.path = None
        self.created_at = None

    def create(self):
        """Создание файла"""
        pass

    def open(self, path):
        """Открытие существующего файла"""
        pass

    def remove(self, path):
        """Удаление существующего файла"""
        pass

    def save(self, filename):
        """Сохранение измененного файла"""
        pass

    def get_type_file(self):
        """Получение типа файла"""
        pass


class AudioFile(MediaFile):
    """Класс Аудиофайл, создает объекты с типом аудио"""

    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'audio'

    def get_length(self):
        """Метод для получения длины трека"""
        pass

    def play(self):
        """Метод для проигрывания трека"""
        pass


class VideoFile(MediaFile):
    """Класс Видеофайл, создаёт объекты с типом видео"""

    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'video'

    def get_length(self):
        """Метод для получения длины ролика"""
        pass

    def play(self):
        """Метод для проигрывания ролика"""
        pass


class PhotoFile(MediaFile):
    """Класс Фотофайл, создает объекты изображений"""

    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'photo'

    def resize(self, x, y):
        """Метод для изменения размера картинки"""
        pass

    def convert_to_png(self):
        """Метод для преобразования изображения в PNG"""
        pass

    def convert_to_jpeg(self):
        """Метод для преобразования изображения в JPEG"""
        pass


"""
img = PhotoFile('photo')
img.open('/1.jpg')
img.resize(100, 100)
img.convert_to_png()
img.save()

video = VideoFile('video_file')
video.open('/1.mpg')
print(video.get_length())
video.play()

audio = AudioFile('audio_file')
audio.open('/1.mp3')
print(audio.get_length())
audio.play()
audio.remove()

Перспективы добавления нового функционала: в рамках текущего задания новые типы файлов добавлять несложно.

"""
