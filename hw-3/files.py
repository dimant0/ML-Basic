
class MediaFile:
    def __init__(self, name):
        self.name = name
        self.size = None
        self.owner = None
        self.meta_data = None
        self.path = None
        self.created_at = None

    def create(self):
        pass

    def open(self, path):
        pass

    def remove(self, path):
        pass

    def save(self, filename):
        pass

    def get_type_file(self):
        pass


class AudioFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'audio'

    def get_length(self):
        pass

    def play(self):
        pass


class VideoFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'video'

    def get_length(self):
        pass

    def play(self):
        pass


class PhotoFile(MediaFile):
    def __init__(self, name):
        super().__init__(name)
        self.meta_data = 'photo'

    def resize(self):
        pass

    def convert_to_png(self):
        pass

    def convert_to_jpeg(self):
        pass
