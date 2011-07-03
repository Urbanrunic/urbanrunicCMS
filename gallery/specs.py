from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb(processors.Resize):
    width = 100
    height = 75
    crop = True

# first we define our medium resize processor
class ResizeMedium(processors.Resize):
    width = 300
    height = 300
    crop = True

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 600

# now let's create an adjustment processor to enhance the image at small sizes
class EnchanceThumb(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

# now let's create an adjustment processor to enhance the image at small sizes
class EnchanceMedium(processors.Adjustment):
    contrast = 1.5
    sharpness = 1.0

# now we can define our thumbnail spec
class Thumbnail(ImageSpec):
    access_as = 'thumbnail_image'
    pre_cache = True
    processors = [ResizeThumb, EnchanceThumb]

# now we can define our thumbnail spec
class Medium(ImageSpec):
    access_as = 'medium_image'
    pre_cache = True
    processors = [ResizeMedium, EnchanceMedium]

# and our display spec
class Display(ImageSpec):
    increment_count = True
    processors = [ResizeDisplay]