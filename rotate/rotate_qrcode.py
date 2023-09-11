import segno

qrcode = segno.make_qr("Hello,World")

qrcode_rotated = qrcode.to_pil().rotate(45)
qrcode_rotated.save("rotated_qrcode.png")
