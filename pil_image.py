from PIL import Image


def contrast_grader(image):

    # Import an image from directory:
    input_image = Image.open(image)

    # Extracting the width and height of the image:
    width, height = input_image.size

    pixels = []

    # taking half of the width:
    for i in range(width//2):
        for j in range(height):
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))

            pixels.append([r, g, b])

    # Get max and min
    gb_threshold = 0
    for i in pixels:
        gb = (i[1] + i[2])/2
        gb_threshold += gb
    gb_threshold = round((gb_threshold/len(pixels)), 2)

    print(f"gb_threshold: {gb_threshold}")
    
    # Calc meat perc
    px_meal=0
    px_fat=0

    for i in pixels:
        #"blanco" (240,218,205)
        #"rojo" (145,50,82)

        # blanco = 240, 210
        # rojo = 145, 66

        # ================
        # rojo (158,31,24)
        # blanco (223,190,183)
        # 0 - 255
        # 126

        gb_threshold = 135

        red = i[0]
        gb = (i[1] + i[2])/2

        if gb > gb_threshold: px_fat+=1
        else: px_meal+=1


    perc_meal = round(px_meal/(px_fat+px_meal) * 100, 2)
    return(f"El porcentaje de la grasa es: {perc_meal}%")


print(contrast_grader("kobe2.jpg"))
