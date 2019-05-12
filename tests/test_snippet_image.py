from os.path import (
    join,
    dirname,
)
from PIL import Image
from functools import reduce
from operator import add
from math import sqrt
from snippet_image import __version__

from .images import (
    generate_image_with_background,
    generate_image_without_background,
    generate_image_with_size,
    generate_image_with_size_and_background,
    generate_image_with_empty_text,
)


ASSERT_PATH = join(dirname(dirname(__file__)), 'assets')

PURPOSE_IMAGE_WITH_BACKGROUND = join(ASSERT_PATH, 'snippet-image-with-background.jpg')
PURPOSE_IMAGE_WITHOUT_BACKGROUND = join(ASSERT_PATH, 'snippet-image-without-background.jpg')
PURPOSE_IMAGE_WITH_SIZE = join(ASSERT_PATH, 'snippet-image-with-size.jpg')
PURPOSE_IMAGE_WITH_SIZE_AND_BACKGROUND = join(ASSERT_PATH, 'snippet-image-with-size-and-background.jpg')
PURPOSE_IMAGE_WITH_EMPTY_TEXT = join(ASSERT_PATH, 'snippet-image-with-empty-text.jpg')


def test_version():
    assert __version__ == '0.1.4'


def test_image_with_background():
    image_blob = generate_image_with_background()
    _compare_result_and_purpose_images(
        image_blob,
        PURPOSE_IMAGE_WITH_BACKGROUND,
    )


def test_image_without_background():
    image_blob = generate_image_without_background()
    _compare_result_and_purpose_images(
        image_blob,
        PURPOSE_IMAGE_WITHOUT_BACKGROUND,
    )


def test_image_with_size():
    image_blob = generate_image_with_size()
    _compare_result_and_purpose_images(
        image_blob,
        PURPOSE_IMAGE_WITH_SIZE,
    )


def test_image_with_size_and_background():
    image_blob = generate_image_with_size_and_background()
    _compare_result_and_purpose_images(
        image_blob,
        PURPOSE_IMAGE_WITH_SIZE_AND_BACKGROUND,
    )


def test_image_with_empty_text():
    image_blob = generate_image_with_empty_text()
    _compare_result_and_purpose_images(
        image_blob,
        PURPOSE_IMAGE_WITH_EMPTY_TEXT,
    )


def _compare_result_and_purpose_images(result_blob, purpose_file):
    result_image = Image.open(result_blob)
    purpose_image = Image.open(purpose_file)
    rms = _compare_images(
        result_image,
        purpose_image,
    )

    assert rms == 0


def _compare_images(source, purpose):
    source_histogram = source.histogram()
    purpose_histogram = purpose.histogram()
    rms = sqrt(
        reduce(
            add,
            map(
                lambda a, b: (a - b) ** 2,
                source_histogram,
                purpose_histogram,
            )
        ),
    )

    return rms
