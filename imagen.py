from PIL import Image

img = Image.open('busqueda/marvel-thor.png')
new_img = img.resize((150,200))
new_img.save('busqueda/marvel-thor-150x200.png','png')

img = Image.open('busqueda/marvel-wolverine.png')
new_img = img.resize((150,200))
new_img.save('busqueda/marvel-wolverine-150x200.png','png')

