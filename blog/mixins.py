from io import BytesIO
from PIL import Image


class CropShrinkImageMixin:

    def shrink_image(self, field_name, resize_shape):
        img: Image = Image.open(getattr(self, field_name))
        img.thumbnail(self.get_shrinked_size(field_name, resize_shape), Image.ANTIALIAS)
        image_file = BytesIO()
        img.save(image_file, 'png')
        getattr(self, field_name).file = image_file

    def get_shrinked_size(self, field_name, resize_shape):
        actual_img_width, actual_img_height = getattr(self, field_name).width, getattr(self, field_name).height
        ratio = min(resize_shape[0] / actual_img_width, resize_shape[1] / actual_img_height)
        return int(actual_img_width * ratio), int(actual_img_height * ratio)

    def crop_image(self, field_name, resize_shape):
        img: Image = Image.open(getattr(self, field_name))
        new_width = resize_shape[0]
        new_height = resize_shape[1]
        left = (img.width - new_width) / 2
        top = (img.height - new_height) / 2
        right = (img.width + new_width) / 2
        bottom = (img.height + new_height) / 2
        img = img.crop((left, top, right, bottom))
        image_file = BytesIO()
        img.save(image_file, format='png')
        getattr(self, field_name).file = image_file
