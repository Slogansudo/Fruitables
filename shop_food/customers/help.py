from django.db.models import TextChoices
import uuid


class SaveMediaFile(object):
    def customer_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'customer/{uuid.uuid4()}.{image_extension}'


