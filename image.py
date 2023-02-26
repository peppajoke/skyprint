from PIL import Image, ImageDraw, ImageFont
import numpy

def create_text_image(text, image_width=800, image_height=600, font_size=48, font_path='Helvetica.ttf'):
    """
    Creates a JPG image of the input text in black, Arial font.

    Args:
        text (str): The input text to render as an image.
        image_width (int): The width of the output image in pixels (default: 800).
        image_height (int): The height of the output image in pixels (default: 600).
        font_size (int): The font size to use for rendering the text (default: 48).
        font_path (str): The file path to the font file to use (default: 'arial.ttf').

    Returns:
        PIL.Image.Image: A Pillow Image object representing the rendered text.
    """
    # Create a new Pillow image with the specified width and height
    image = Image.new(mode='RGB', size=(image_width, image_height), color='black')

    # Create a new Pillow ImageDraw object
    draw = ImageDraw.Draw(image)

    # Load the Arial font at the specified size
    font = ImageFont.truetype(font_path, size=font_size)

    # Calculate the text size and position
    text_width, text_height = draw.textsize(text, font=font)
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    # Render the text in black using the Arial font
    draw.text((x, y), text, fill='white', font=font)

    # Convert the image to JPG format and return it as a Pillow Image object
    return black_to_transparency_gradient(image.convert('RGB'))

def white_to_transparency_gradient(img):
    x = numpy.asarray(img.convert('RGBA')).copy()

    x[:, :, 3] = (255 - x[:, :, :3].mean(axis=2)).astype(numpy.uint8)

    return Image.fromarray(x)

def black_to_transparency_gradient(img):
    x = numpy.asarray(img.convert('RGBA')).copy()
    x[:, :, 3] = (x[:, :, :3].mean(axis=2)).astype(numpy.uint8)
    return Image.fromarray(x)