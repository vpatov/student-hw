# Basic Image Processor (let's build 1% of Photoshop!)

Write a program that processes an image, and outputs a processed image.
It will take in as command line parameters the path of the image (should just be a file on the local machine), the type of processing to perform, and the name of the output image.

```
python3 ./image_processor.py <image_path> <transformation_type> <output_image_path>
```
Example:
```
python3 ./image_processor.py image.png blue_channel newimage.png
```
This will open the image image.png, will process it such that only the blue channel remains, and will write the result to a new image called newimage.png.

## Transformations 

Types of transformations that you should implement:




```red_channel, blue_channel, green_channel```

These leave only the specified color channel in the image, removing other color channels.

---



```grayscale```

This grayscales the image.

---


```invert```

This inverts the colors in the image (see attached image for example).


---


```half_size```

This reduces the image dimensions by half. For example, a 1200x1600 image will become a 600x800 image.

---


```double_size```


This doubles the size of the image, stretching it. (Bonus points if you also average neighboring pixels instead of just copying pixels).



---



```mirror_vertical```

Takes the left half of the image (when dividing vertically), and mirrors it onto the right half.


---


```mirror_horizontal```

Takes the top half of the image (when dividing horizontally), and mirrors it onto the bottom half.


---


```tile_100```

Takes the top-left 100x100 section of the image, and repeatedly tiles it into a 5x5 arrangement (the output image will have a size of 500x500).

---


```tile_50```

Takes the bottom-left 50x50 section of the image, and repeatedly tiles it into a 8x8 arrangement (the output image will have a size of 400x400).

---


```tile_100```

Takes the top-left 100x100 section of the image, and repeatedly tiles it into a 5x5 arrangement (the output image will have a size of 500x500).

---


```tile_150_100```

Takes the top-right 150x100 section of the image, and repeatedly tiles it into a 3x5 arrangement (the output image will have a size of 450x500).

---


```average_color```

Computes the average color of the image, and creates a new 100x100 image that contains just that color.

---


```color_palette```

Given a following color palette of 64 colors[1], replace each color in the image with a color from the palette that is closest to the original color. The distance between two colors is defined as the average of the differences of the RGB color values.

For example:
The distance between `(10, 10, 10)` and `(12, 12, 15)` is `3`.
The distance between `(10, 10, 10)` and `(14, 14, 17)` is `5`.
Therefore `(12,12,15)` is closer to `(10,10,10)` than `(14,14,17)` is.

Use the attached palette `color_palette.txt`, which contains a list of `64` colors in RGB format.
 
[1] The original Atari Galala (1981) used a 6-bit color scheme.


---



## Considerations/Tips


### PIL 



If you're using Python, you can use the `PIL` image library to help you work with images more easily. The library takes care of things like decoding the raw image data (usually compressed with JPEG), and lets you work with a 2D grid of pixels (RGB values) instead. An RGB value is a tuple of three integers ranging from [0,255].

```python
from PIL import Image
image = Image.open('./path/to/my/image.jpg')

print(image.size)
# (800, 600)
r,g,b = image.getpixel((123, 234))
# make a pixel a little more red, but make sure the value isn't more than 255.
image.putpixel((123, 234), (min(r + 30, 255), g, b))
```


You can learn more about what functionality is available in the PIL library here:

https://pillow.readthedocs.io/en/stable/reference/Image.html


### Functions


Functions are your friend. One way to write good, clean code is to use lots of small, lean functions that do one thing, and do it well. However, how one defines "one thing" is more of an art than a science.


### Test Data


Try using multiple images, of various sizes and proportions, and with varying content. This will help you better understand how your program behaves.

