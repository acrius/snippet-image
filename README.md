# snippet-image

Package for simple creation images of snippets for social networks using [pillow](https://pillow.readthedocs.io/en/stable/).
Pictures for snippets can be inserted for sharing pages in social networks, for example in tag meta:


```html
<meta property="og:image" content="Link to your snippet image" />
<meta name="twitter:image" content="Link to your snippet image" />
```

## Installation

```
pip3 install snippet-image
```

## User guide

To start creating images for snippets, it is enough to import the function ```from snippet_image import create_snippet_image```.

```python
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

```

Next, open the file ```jake-the-dog-snippet-image.jpg``` and you will see the following image.

![Jake the dog snippet image](./assets/jake-the-dog-snippet-image.jpg)

## API

### create_snippet_image

Args:

* font (str) - Path to font file. Is required. For load font used PIL.ImageFont.

Kwargs:

* size (tuple(int, int)) - Size of snippet image. (width, height).
* text (str) - Text of snippet image. By default is an empty string.
* background (str) - Path to background image file.
* background_color (tuple(int, int, int)) - Background color of snippet image. Used when background is None.
                                            By default is (0, 0, 0).
* overlay (str) - Path to overlay image. if size is None, overlay size is used.
                  As an overlay, an image with a transparent background is used.
* brightness (float)- Brightness of background of snippet image. Value from 0 to 1.
* font_color(tuple(int, int, int, int)) - RGBA font color. By default is (255, 255, 255, 255).
* font_size (int) - Size of snippet image text. By default is 64.
* padding (float) - Text indents to the left and right of the snippet image.
                    Value from 0 to 1.
                    0 - 0% width;
                    1 - 100% width.
* center tuple(int, int) - Background image center for crop and resize image. (x, y).
                    Defaults is center of background image.
 
Return                   

* BytesIO blob of snippet image

## How it works

### Size of snippet image

If the size is set, then it is used as the snippet image size.
If the size is not set, then the overlay must be set,
and then the size of the overlay is used as the image snippet size.

### Background

If the path to the image with background is set as ```background```,
then it is selected as the background for snippet image.
For open used

```python
PIL.Image.open(background)
```
If the path is not specified, then the fill color as ```background_color``` is used as the background.

```python
PIL.Image.new('RGB', size, background_color)
```

Next, the background image is enhanced brightness.

```python
PIL.ImageEnhance.Brightness(image).enhance(brightness)
```

Next, the background image is cropped and resized.

### Text

For load font used:

```python
font = PIL.ImageFont.truetype(font, size=font_size, encoding='UTF-8')
```

To align text in the center, the maximum width in chars that a line can occupy is calculated.

```python
line_length = int((width * (1 - padding)) / (font.getsize(text)[0] / len(text)))    
```

### Overlay

An overlay is an image with a transparent background to create a kind of watermark.

For example:

![Overlay example](./assets/overlay.png)

For paste used:

```python
image.paste(overlay_image, (0, 0), mask=overlay_image)
```

## Applications

Example with background and overlay

![Example with background and overlay](./assets/Show%20cases%20snippet%20images%20with%20background.png)

Example without background and overlay

![Example without background and overlay](./assets/Show%20cases%20snippet%20images%20without%20background.png)

## Integration

Django: [django-snippet-image](https://github.com/acrius/django-snippet-image).

Wagtail: [wagtail-snippet-image](https://github.com/acrius/wagtail-snippet-image).

## Example

The example is in exmaple.py.

For run install dependencies (pillow, snippet-image) and execute:

```
python3 example.py
```

or use poetry:

```
poetry install
poetry run python3 example.py
```

## Test

For run install dependencies (pillow, snippet-image, pytest) and execute:

```
pytest
```

or use poetry

```
poetry install
poetry run pytest
```
