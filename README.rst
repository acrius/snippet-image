============================
snippet-image
============================

Package for simple creation images of snippets for social networks using pillow_.

.. _pillow: https://pillow.readthedocs.io/en/stable/

Installation
---------------------------

`pip3 install snippet-image`

User guide
---------------------------

To start creating images for snippets, it is enough to import the function ```from snippet_image import create_snippet_image```.

.. code-block:: python

    from snippet_image import create_snippet_image

    image_blob = create_snippet_image(
            font='/home/iamterminator/.fonts/OpenSans-Bold.ttf', # Path to your font file
            font_size=62, # Font size
            background='/home/iamterminator/.wallpapers/jakethedog.jpg', # Path to your background image
            size=(1200, 630), # Size of snippet image. (width, height)
            text='Jake the Dog', # Text for draw on snippet image
            brightness=0.3, # Brightness of background
        )

    with open('jake-the-dog-snippet-image.jpg', 'wb') as file:
        file.write(image_blob.getvalue())

Read the docs in https://github.com/acrius/snippet-image.
