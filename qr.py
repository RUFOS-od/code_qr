# creation de code Qr
import qrcode
img = qrcode.make('https://forms.gle/4bUZaWHeaGeySgx59')
type(img)  # qrcode.image.pil.PilImage
img.save("recensement.png")