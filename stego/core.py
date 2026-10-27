from PIL import Image

def load_pixels(path):
    """
    Load the pixels of an image and return them as a bytearray along with the image size"""
    img = Image.open(path)
    img = img.convert("RGB")
    ba = bytearray(img.tobytes())
    return ba, img.size

