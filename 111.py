from PIL import Image

image = "IMG_3480.JPG"

img = Image.open(image)

box = (100, 0, 1000, 1000)

img2 = img.crop(box)

img2.save('myimage_cropped3.jpg')

img2.show()
