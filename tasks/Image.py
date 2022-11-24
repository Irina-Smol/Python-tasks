#Вставляем одно изображение в другое с помощью Pillow
#Метод paste() из библиотеки Pillow, предоставляет возможность вставки одного изображения в другое изображение.
#По умолчанию изображение вставляется в верхней левой части фоновой картинки.

from PIL import Image

first_image = Image.open('lev-2.jpg')
second_image = Image.open('12.jpg')

first_image.paste(second_image)
first_image.save('paste.jpg', quality=95)

first_image.close()
second_image.close()
