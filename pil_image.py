from PIL import Image

# Import an image from directory:
input_image = Image.open("kobe2.jpg")

# Extracting pixel map:
pixel_map = input_image.load()

# Extracting the width and height 
# of the image:
width, height = input_image.size

pixel = []

# taking half of the width:
for i in range(width//2):
    for j in range(height):
        # getting the RGB pixel value.
        r, g, b = input_image.getpixel((i, j))

        pixel.append([r, g, b])

px_meal=0
px_fat=0

for i in pixel:
    #"blanco" (240,218,205)
    #"rojo" (145,50,82)

    # blanco = 240, 210
    # rojo = 145, 66

    # ================
    # rojo (158,31,24)
    # blanco (223,190,183)

    umbral_blanco = 135

    red = i[0]
    gb = (i[1] + i[2])/2

    if gb>umbral_blanco: px_fat+=1
    else: px_meal+=1


perc_meal = round(px_meal/(px_fat+px_meal) * 100, 2)
print(f"El porcentaje de la grasa es: {perc_meal}%")