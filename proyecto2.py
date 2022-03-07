import tkinter as tk 
from PIL import ImageTk, Image
import util
import ventanas

RaizComic = tk.Tk()
RaizComic.title("¡Comics!")
RaizComic.geometry('600x600')
image2 = Image.open('marvelydc.png')
image1 = ImageTk.PhotoImage(image2)
background_Label = tk.Label(RaizComic, image=image1)
background_Label.image1 = image1
background_Label.place(x=0, y=0, height=600, width=600)

Bienvenida = tk.Label(RaizComic, text = '¡BIENVENIDOS!')
Bienvenida.place(x=150, y= 10)
Bienvenida.config(bg = 'black', fg = 'white', justify = 'right', font = ('Comic Sans', 30))

busqueda = tk.Entry(RaizComic, width = 30)
busqueda.place(x = 215, y = 140, height = 20)

def BuscarHeroe():
    if busqueda.get().lower() == ("man").lower():
        ventanas.busqueda_man()
    elif busqueda.get().lower() == ('green').lower():
        ventanas.busqueda_green()
    elif busqueda.get().lower() == ('iron man').lower():
        ventanas.BotonIron()
    elif busqueda.get().lower() == ('hulk').lower():
        ventanas.BotonHulk()
    elif busqueda.get().lower() == ("cyclo").lower():
        ventanas.BotonCyclo()  
    elif busqueda.get().lower() ==("capitan america").lower():      
        ventanas.BotonCapi()
    elif busqueda.get().lower() == ("thor").lower():          
        ventanas.BotonThor()
    elif busqueda.get().lower() == ("wolverine").lower():   
        ventanas.BotonWol()      
    elif busqueda.get().lower() == ("hawkeye").lower():  
        ventanas.BotonHaw()
    elif busqueda.get().lower() == ("silver Surfer").lower(): 
        ventanas.BotonSilver()
    elif busqueda.get().lower() == ("daredevil").lower():
        ventanas.BotonDare()
    elif busqueda.get().lower() == ("superman").lower():
        ventanas.BotonSuper()
    elif busqueda.get().lower() == ("linterna verde").lower():
        ventanas.BotonVerde()
    elif busqueda.get().lower() == ("wonder woman").lower():
        ventanas.BotonWonder()
    elif busqueda.get().lower() == ("robin").lower():
        ventanas.BotonRobin()
    elif busqueda.get().lower() == ("black canary").lower():
        ventanas.BotonBlack()
    elif busqueda.get().lower() == ("flash").lower():
        ventanas.BotonFlash()
    elif busqueda.get().lower() == ("flecha verde").lower():
        ventanas.BotonFlecha()
    elif busqueda.get().lower() == ("martin").lower():
        ventanas.BotonMartin()
    elif busqueda.get().lower() == ("bluee beetle").lower():
        ventanas.BotonBlue()
    elif busqueda.get().lower() == ('spiderman').lower() or ('spider').lower() or ('spi').lower():
        ventanas.BotonSpiderman()


def salir():
    RaizComic.destroy()


def marvelbo():
    elframe = tk.Toplevel()
    elframe.geometry('675x600')
    elframe.title('Comics de Marvel')

    scrollbar = tk.Scrollbar(elframe)
    c = tk.Canvas(elframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command= c.yview)
    scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
    elframe = tk.Frame(c)
    c.pack(side='left', fill='both', expand= True)
    c.create_window(0,0, window= elframe, anchor= 'nw')
    imagefondo = Image.open('fondo.png')
    imagefondo1 = ImageTk.PhotoImage(imagefondo)
    background_Label = tk.Label(elframe, image=imagefondo1)
    background_Label.imagefondo1 = imagefondo1
    background_Label.place(x=0, y=0, height=1120, width=950)

    w = 125
    h = 189

    LabelList = []
    PhotoList = []

    heroes = util.getHeroePorPublihser('Marvel Comics')

    for Hero in heroes:
        path = 'marvel/' + Hero['id'] + '.png'
        img = Image.open(path).resize((w,h))
        PhotoImg = ImageTk.PhotoImage(img)
        PhotoList.append(PhotoImg)
        Label = tk.Label(elframe, image = PhotoImg)
        LabelList.append(Label)

    pixs_per_row = 4
    row = col = 0

    for label in LabelList:
        label.grid(row = row, column = col)
        col += 2
        if col >= pixs_per_row:
            col = 0
            row += 1
        
#-------------------------Spiderman------------------------------
        tk.Label(elframe, font=8,
        text=("Spiderman\n Amazing Fantasy #15\n Peter Parker\n Marvel Comics")).grid(row=0, column=1)

        def boton_spider():
            ventanas.BotonSpiderman()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_spider)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=0, column=1, sticky = "s")

#----------------------Iron Man--------------------------------
        tk.Label(elframe, font=8,
        text=("Iron Man\n Tales of Suspense #39\n Tony Stark\n Marvel Comics")).grid(row=1, column=1)

        def boton_iron():
            ventanas.BotonIron()


        boton_1 = tk.Button(elframe, text = "Más", command = boton_iron)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=1, column=1, sticky = "s")

#---------------------HULK--------------------------------
        tk.Label(elframe, font=8,
        text=("Hulk\n The Incredible Hulk #1\n Bruce Banner\n Marvel Comics")).grid(row=2, column=1)

        def boton_hulk():
            ventanas.BotonHulk()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_hulk)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=2, column=1, sticky = "s")

#---------------------Daredevil---------------------------
        tk.Label(elframe, font=8,
        text=("Daredevil\n Daredevil #1\n Matthew Michael Murdock\n Marvel Comics")).grid(row=3, column=1)

        def boton_dare():
            ventanas.BotonDare()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_dare)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=3, column=1, sticky = "s")

#--------------------Cyclops-------------------------------
        tk.Label(elframe, font=8,
        text=("Cyclops\n X-Men #1\n Scott Summers\n Marvel Comics")).grid(row=4, column=1)

        def boton_cyclo():
            ventanas.BotonCyclo()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_cyclo)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=4, column=1, sticky = "s")

#-------------------Capitan America----------------------------
        tk.Label(elframe, font=8,
        text=("Capitan America\n Captain America Comics #1\n Steve Rogers\n Marvel Comics")).grid(row=0, column=3)

        def boton_capi():
            ventanas.BotonCapi()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_capi)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=0, column=3, sticky = "s")

#...................Thor-----------------------------
        tk.Label(elframe, font=8,
        text=("Thor\n Journey into Myster #83\n Thor Odinson\n Marvel Comics")).grid(row=1, column=3)

        def boton_thor():
            ventanas.BotonThor()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_thor)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=1, column=3, sticky = "s")

#-------------------Wolverine-------------------------
        tk.Label(elframe, font=8,
        text=("Wolverine\n The Incredible Hulk #180\n James Howlett\n Marvel Comics")).grid(row=2, column=3)

        def boton_wolver():
            ventanas.BotonWol()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_wolver)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=2, column=3, sticky = "s")

#....................Hawkeye...........................
        tk.Label(elframe, font=8,
        text=("Hawkeye\n Tales of Suspense #57\n Clinton Francis Barton\n Marvel Comics")).grid(row=3, column=3)

        def boton_haw():
            ventanas.BotonHaw()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_haw)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=3, column=3, sticky = "s")

#-------------------Silver Surfer--------------------------
        tk.Label(elframe, font=8,
        text=("Silver Surfer\n The Fantastic Four #48\n Norrin Radd\n Marvel Comics")).grid(row=4, column=3)

        def boton_silver():
            ventanas.BotonSilver()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_silver)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=4, column=3, sticky = "s")

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()



def dcboton():
    elframe = tk.Toplevel()
    elframe.geometry('640x600')
    elframe.title('Comics de DC')

    scrollbar = tk.Scrollbar(elframe)
    c = tk.Canvas(elframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command= c.yview)
    scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
    elframe = tk.Frame(c)
    c.pack(side='left', fill='both', expand= True)
    c.create_window(0,0, window= elframe, anchor= 'nw')
    imagefondodc = Image.open('dcfondo.png')
    imagefondodc1 = ImageTk.PhotoImage(imagefondodc)
    background_Label = tk.Label(elframe, image=imagefondodc1)
    background_Label.imagefondodc1 = imagefondodc1
    background_Label.place(x=0, y=0, height=1120, width=950)


    w = 125
    h = 189

    LabelList = []
    PhotoList = []

    heroes = util.getHeroePorPublihser('DC Comics')

    for Hero in heroes:
        path = 'dc/' + Hero['id'] + '.png'
        img = Image.open(path).resize((w,h))
        PhotoImg = ImageTk.PhotoImage(img)
        PhotoList.append(PhotoImg)
        Label = tk.Label(elframe, image = PhotoImg)
        LabelList.append(Label)

    pixs_per_row = 4
    row = col = 0

    for label in LabelList:
        label.grid(row = row, column = col)
        col += 2
        if col >= pixs_per_row:
            col = 0
            row += 1
        
#----------------Superman-------------------------
        tk.Label(elframe, font=8,
        text=("Superman\n Action Comics #1\n kal-El\n DC Comics")).grid(row=0, column=1)
        
        def boton_super():
            ventanas.BotonSuper()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_super)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=0, column=1, sticky = "s")

#---------------Linterna Verde---------------------
        tk.Label(elframe, font=8,
        text=("Green Lantern\n All-American Comics #16\n Alan Scott\n DC Comics")).grid(row=1, column=1)

        def boton_verde():
            ventanas.BotonVerde()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_verde)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=1, column=1, sticky = "s")

#--------------Wonder Woman----------------------------
        tk.Label(elframe, font=8,
        text=("Wonder Woman\n All Star Comics #8\n Princess Diana\n DC Comics")).grid(row=2, column=1)

        def boton_wonder():
            ventanas.BotonWonder()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_wonder)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=2, column=1, sticky = "s")

#--------------Robin Nightwing--------------------------
        tk.Label(elframe, font=8,
        text=("Robin/Nightwing\n Detective Comics #38\n Dick Grayson\n DC Comics")).grid(row=3, column=1)

        def boton_robin():
            ventanas.BotonRobin()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_robin)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=3, column=1, sticky = "s")

#--------------Black Canary---------------------------
        tk.Label(elframe, font=8,
        text=("Black Canary\n Flash Comics #86\n Dinah Drake\n DC Comics")).grid(row=4, column=1)

        def boton_black():
            ventanas.BotonBlack()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_black)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=4, column=1, sticky = "s")

#-------------Flash-------------------------------
        tk.Label(elframe, font=8,
        text=("Flash\n Flash Comics #1\n Barry Allen\n DC Comics")).grid(row=0, column=3)

        def botn_flash():
            ventanas.BotonFlash()

        boton_1 = tk.Button(elframe, text = "Más", command = botn_flash)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=0, column=3, sticky = "s")

#-------------Green Arrow-----------------------------
        tk.Label(elframe, font=8,
        text=("Green Arrow\n More Fun Comics #73\n Oliver Queen\n DC Comics")).grid(row=1, column=3)

        def boton_flecha():
            ventanas.BotonFlecha()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_flecha)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=1, column=3, sticky = "s")

#-------------Martian----------------------------------
        tk.Label(elframe, font=8,
        text=("Martian Manhunter\n Detective Comics #225\n Martian Manhunter\n DC Comics")).grid(row=2, column=3)

        def boton_martin():
            ventanas.BotonMartin()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_martin)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=2, column=3, sticky = "s")

#-------------Blue Beetle-------------------------------------
        tk.Label(elframe, font=8,
        text=("Blue Beetle\n Mystery Men Comics #1\n Dan Garret\n DC Comics")).grid(row=3, column=3)

        def boton_blue():
            ventanas.BotonBlue()

        boton_1 = tk.Button(elframe, text = "Más", command = boton_blue)
        boton_1.config(width=8, height=0)
        boton_1.grid(row=3 , column=3, sticky = "s")

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()


BotonMarvel = tk.Button(RaizComic, text = 'MARVEL', command = marvelbo, fg = 'RED', padx = 40, pady = 5)
BotonMarvel.place(x=100, y=80)
BotonDC = tk.Button(RaizComic, text= 'DC', command= dcboton, fg = 'BLUE', padx = 50, pady = 5)
BotonDC.place(x=380, y=80)
botonsalir = tk.Button(RaizComic, text = 'SALIR', command= salir, padx = 10, pady = 10)
botonsalir.place(x=275, y= 500)
botonbusqueda = tk.Button(RaizComic, text = 'Buscar', command = BuscarHeroe, padx = 10, pady = 5)
botonbusqueda.place(x=275, y= 165)

RaizComic.mainloop()