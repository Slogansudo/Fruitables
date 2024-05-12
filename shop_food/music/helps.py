import uuid


class SaveImage(object):
    def SaveArtistImageFile(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'artist/{uuid.uuid4()}.{image_extension}'

    def SaveAlbumImageFile(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'album/{uuid.uuid4()}.{image_extension}'

    def SaveMusicImageFile(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'music/{uuid.uuid4()}.{image_extension}'
