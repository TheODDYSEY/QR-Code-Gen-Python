import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://youtu.be/RSj0mPJsMy0?t=173")
nirvane_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvane_url,
    target="animated_qrcode.gif",
    scale=5
)