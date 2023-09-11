import segno

qrcode = segno.make_qr("Hello,World")

qrcode_rotated = qrcode.to_pil(
    scale=5,
    light="lightblue",
    dark="green",
    ).rotate(45, expand=True)

qrcode_rotated.save("rotated_qrcode3.png",)
