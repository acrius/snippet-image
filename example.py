from tests.images import (
    generate_image_with_background,
    generate_image_without_background,
    generate_image_with_size,
    generate_image_with_size_and_background,
)

PURPOSE_IMAGE_WITH_BACKGROUND = 'snippet-image-with-background.jpg'
PURPOSE_IMAGE_WITHOUT_BACKGROUND = 'snippet-image-without-background.jpg'
PURPOSE_IMAGE_WITH_SIZE = 'snippet-image-with-size.jpg'
PURPOSE_IMAGE_WITH_SIZE_AND_BACKGROUND = 'snippet-image-with-size-and-background.jpg'


def create_images():
    create_image_with_background()
    create_image_without_background()
    create_image_with_size()
    create_image_with_size_and_background()


def create_image_with_background():
    image_blob = generate_image_with_background()
    _save_image(
        image_blob,
        PURPOSE_IMAGE_WITH_BACKGROUND,
    )


def create_image_without_background():
    image_blob = generate_image_without_background()
    _save_image(
        image_blob,
        PURPOSE_IMAGE_WITHOUT_BACKGROUND,
    )


def create_image_with_size():
    image_blob = generate_image_with_size()
    _save_image(
        image_blob,
        PURPOSE_IMAGE_WITH_SIZE,
    )


def create_image_with_size_and_background():
    image_blob = generate_image_with_size_and_background()
    _save_image(
        image_blob,
        PURPOSE_IMAGE_WITH_SIZE_AND_BACKGROUND,
    )


def _save_image(blob, filename):
    with open(filename, 'wb') as file:
        file.write(blob.getvalue())


if __name__ == '__main__':
    create_images()
