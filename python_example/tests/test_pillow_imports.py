import pathlib

import pytest
from PIL import Image
from PIL import ImageDraw

################################################################################
# Regression Tests
def test_import_Image():
  import PIL.Image

def test_import_ImageFile():
  import PIL.ImageFile

def test_import_ImageDraw():
  from PIL import ImageDraw

def test_ImageOpen_Input():
  img = Image.open(pathlib.Path(__file__).parent / 'skull.png')

@pytest.mark.skip(reason="Example of how to skip a test.")
def test_ImageOpen_Output():
  """
  This can fail, just to show if it has changed.
  """
  img = Image.open(pathlib.Path(__file__).parent / 'skull.png')
  attributes = [
    "info",
    "category",
    "palette",
    "pyaccess",
    "decoderconfig",
    "text",
    "filename",
    "fp",
    "readonly",
    "im",
    "mode",
    "decodermaxblock",
    "tile",
    "_PngImageFile__idat",
    "png",
    "size",
  ]
  assert attributes in img.__dict__.keys()

def test_ImageOpen_Save():
  """
  Does it still work the same?
  """
  img = Image.open(pathlib.Path(__file__).parent / 'skull.png')
  # img = img.convert("RGBA") # was ignored, then depricated, then raises an error
  img = img.convert("RGB")
  img.save(pathlib.Path(__file__).parent / 'skull.jpg')

def test_ImageNew_Save():
  """
  Create a file without an extension.
  """
  img = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
  img.save(pathlib.Path(__file__).parent / "test", "png")
  with open(pathlib.Path(__file__).parent / "test") as f:
    f.close()

def test_concat_ImageNew_Save():
  Image.new("RGB", size=(50, 50), color=(256, 0, 0)).save("test2", "JPEG")

def test_ImageDraw_PointOutput():
  image = Image.new("RGBA", (200, 200),
                       (255, 255, 255, 0))
  draw = ImageDraw.Draw(image)
  draw.point((25, 25), fill="black")

def test_ImageOpen_size():
  img = Image.open(pathlib.Path(__file__).parent / 'skull.png')
  img.size
  print(img.size[1])
  print(img.size[0])
