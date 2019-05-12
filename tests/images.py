from os.path import (
    join,
    dirname,
)
from snippet_image import create_snippet_image

ASSERT_PATH = join(dirname(dirname(__file__)), 'assets')

IMAGE_SNIPPET_TEXT = 'What time is it?'
IMAGE_SNIPPET_OVERLAY = join(ASSERT_PATH, 'overlay.png')
IMAGE_SNIPPET_FONT = join(ASSERT_PATH, 'OpenSans-Bold.ttf')
IMAGE_SNIPPET_BACKGROUND = join(ASSERT_PATH, 'background.jpg')
IMAGE_SNIPPET_BACKGROUND_COLOR = (0, 76, 153)
IMAGE_SNIPPET_FONT_SIZE = 64
IMAGE_SNIPPET_BRIGHTNESS = 0.3
IMAGE_SNIPPET_SIZE = (1200, 630)

PURPOSE_IMAGE_WITH_BACKGROUND = join(ASSERT_PATH, 'snippet-image-with-background.jpg')
PURPOSE_IMAGE_WITHOUT_BACKGROUND = join(ASSERT_PATH, 'snippet-image-without-background.jpg')
PURPOSE_IMAGE_WITH_SIZE = join(ASSERT_PATH, 'snippet-image-with-size.jpg')


def generate_image_with_background():
    image_blob = create_snippet_image(
        font=IMAGE_SNIPPET_FONT,
        font_size=IMAGE_SNIPPET_FONT_SIZE,
        background=IMAGE_SNIPPET_BACKGROUND,
        overlay=IMAGE_SNIPPET_OVERLAY,
        text=IMAGE_SNIPPET_TEXT,
        brightness=IMAGE_SNIPPET_BRIGHTNESS,
    )

    return image_blob


def generate_image_without_background():
    image_blob = create_snippet_image(
        font=IMAGE_SNIPPET_FONT,
        font_size=IMAGE_SNIPPET_FONT_SIZE,
        background_color=IMAGE_SNIPPET_BACKGROUND_COLOR,
        overlay=IMAGE_SNIPPET_OVERLAY,
        text=IMAGE_SNIPPET_TEXT,
        brightness=IMAGE_SNIPPET_BRIGHTNESS,
    )

    return image_blob


def generate_image_with_size():
    image_blob = create_snippet_image(
        font=IMAGE_SNIPPET_FONT,
        font_size=IMAGE_SNIPPET_FONT_SIZE,
        background_color=IMAGE_SNIPPET_BACKGROUND_COLOR,
        size=IMAGE_SNIPPET_SIZE,
        text=IMAGE_SNIPPET_TEXT,
        brightness=IMAGE_SNIPPET_BRIGHTNESS,
    )

    return image_blob


def generate_image_with_size_and_background():
    image_blob = create_snippet_image(
        font=IMAGE_SNIPPET_FONT,
        font_size=IMAGE_SNIPPET_FONT_SIZE,
        background=IMAGE_SNIPPET_BACKGROUND,
        size=IMAGE_SNIPPET_SIZE,
        text=IMAGE_SNIPPET_TEXT,
        brightness=IMAGE_SNIPPET_BRIGHTNESS,
    )

    return image_blob


def generate_image_with_empty_text():
    image_blob = create_snippet_image(
        font=IMAGE_SNIPPET_FONT,
        font_size=IMAGE_SNIPPET_FONT_SIZE,
        background=IMAGE_SNIPPET_BACKGROUND,
        overlay=IMAGE_SNIPPET_OVERLAY,
        brightness=IMAGE_SNIPPET_BRIGHTNESS,
    )

    return image_blob
