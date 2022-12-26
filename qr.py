import qrcode
import PIL
import cv2
from PIL import Image

img=qrcode.make("https://leetcode.com/abhishekpurohit20/")
img.save("leetcode.png")

img=qrcode.make("Welcome to India")
img.save("Welcome.jpg")



d=cv2.QRCodeDetector()
retval,points,straightcode=d.detectAndDecode(cv2.imread("Welcome.jpg"))
print(retval)



from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('leetcode.png')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage)
img_3.save("Welcome1.png")


img = qrcode.make('Hello, I am Abhishek')
print(type(img))  # qrcode.image.pil.PilImage
img.save("some_file.png")
