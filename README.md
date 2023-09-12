# Generating QR Codes with Python and Segno

This tutorial will guide you through the process of creating QR codes in Python using the Segno library. You'll learn how to create basic black-and-white QR codes, adjust their size, change colors, rotate them, and even add animated backgrounds.

## Prerequisites

Before you begin, make sure you have Segno installed. You can install it using pip:

```bash
$ python -m pip install segno
```

## Creating a Basic QR Code

To create a basic black-and-white QR code that encodes some content, follow these steps:

1. Create a Python file, e.g., `basic_qrcode.py`.
2. Import the Segno library:

```python
import segno
```

3. Use the `make_qr()` function to encode the content you want. For example, to encode the text "Hello, World":

```python
qrcode = segno.make_qr("Hello, World")
```

4. Save the QR code as an image using the `.save()` method. Specify the filename, including an optional file path:

```python
qrcode.save("basic_qrcode.png")
```

5. Run the Python script from your command line:

```bash
$ python basic_qrcode.py
```

Congratulations! You've created a basic black-and-white QR code.

## Adjusting the Size of the QR Code

If you find the QR code difficult to scan due to its size, you can adjust it by adding a scale parameter to the `.save()` method. The scale parameter changes the width and height of the QR code's modules. For example, to create a QR code with 5x5 pixel modules:

```python
qrcode.save("scaled_qrcode.png", scale=5)
```

## Formatting the Border of the QR Code

To change the size of the border (quiet zone) around the QR code, you can modify the border parameter in the `.save()` method. By default, the quiet zone is four modules on each side. To remove it, set `border=0`:

```python
qrcode.save("borderless_qrcode.png", border=0)
```

To create a QR code with a wider border, increase the value of the border parameter:

```python
qrcode.save("wide_border_qrcode.png", border=10)
```

## Changing the Colors of the QR Code

You can make your QR codes more colorful by changing their colors. Use the `.save()` method with the light and dark parameters to adjust the colors of the light and dark modules of the QR code:

```python
qrcode.save("colorful_qrcode.png", light="lightblue", dark="darkgreen")
```

You can also set the color of the quiet zone:

```python
qrcode.save("colorful_qrcode.png", light="lightblue", dark="darkgreen", quiet_zone="maroon")
```

To change the colors of the data modules (the actual data blocks), use the data_light and data_dark parameters:

```python
qrcode.save("colorful_data_qrcode.png", data_light="lightgreen", data_dark="darkblue")
```

## Rotating the QR Code

You can rotate a QR code using the `.to_pil()` method. Specify the rotation angle in degrees. To rotate by 45 degrees and expand the canvas to contain the whole code:

```python
qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("rotated_qrcode.png")
```

## Creating Animated QR Codes

To create an animated QR code with a moving background, you'll need to install additional dependencies: pillow and qrcode-artistic:

```bash
$ python -m pip install pillow qrcode-artistic
```

Here's how you can create an animated QR code:

```python
import segno
from urllib.request import urlopen

qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")

qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5
)
```

This code creates a QR code with an animated background using a GIF. You can adjust the parameters as needed.

## Conclusion

You've learned how to generate QR codes in Python using the Segno library and customize them in various ways. Whether you need basic black-and-white QR codes or creative, colorful, and animated ones, Segno provides the tools to make your QR codes stand out. Have fun experimenting with different styles and options!
