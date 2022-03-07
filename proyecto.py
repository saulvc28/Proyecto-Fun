import tkinter as tk
from PIL import ImageTk, Image

RaizComic = tk.Tk()
RaizComic.title("¡Comics!")
RaizComic.iconbitmap("Icono.ico")
RaizComic.geometry('600x600')
image2 = Image.open('marvelydc.png')
image1 = ImageTk.PhotoImage(image2)
background_Label = tk.Label(RaizComic, image=image1)
background_Label.image1 = image1
background_Label.place(x=0, y=0, height=600, width=600)

Bienvenida = tk.Label(RaizComic, text = '¡BIENVENIDOS!')
Bienvenida.place(x=150, y= 10)
Bienvenida.config(bg = 'black', fg = 'white', justify = 'right', font = ('Comic Sans', 30))


def salir():
    RaizComic.destroy()

#----------------------MARVEL.................................
def marvelbo():
    elframe = tk.Toplevel()
    elframe.geometry('790x600')
    elframe.title('Comics de Marvel')
    #w=350
    #h=460

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

    #ImagenBienvenida = tk.PhotoImage(file = 'mavellogo.png')
    #PrintBienvenida_marvel = tk.Label(elframe, image = ImagenBienvenida)
    #PrintBienvenida_marvel.grid(row=0, columnspan=2)

    ImagenBienvenida = tk.PhotoImage(file = 'marvellogo1.png')
    PrintBienvenida_marvel = tk.Label(elframe, image = ImagenBienvenida)
    PrintBienvenida_marvel.grid(row=0, column=1)
    
    ImagenBienvenida1 = tk.PhotoImage(file = 'marvellogo2.png')
    PrintBienvenida_marvel1 = tk.Label(elframe, image = ImagenBienvenida1)
    PrintBienvenida_marvel1.grid(row=0, column=2)

#------------------Spiderman-----------------------------
    ImagenSpiderman = tk.PhotoImage(file = 'marvel/marvel-spider.png')
    PrintSpiderman = tk.Label(elframe, image = ImagenSpiderman)
    PrintSpiderman.grid(row =1, column = 0)

    tk.Label(elframe, font=8,
        text=("Spiderman\n Amazing Fantasy #15\n"
            "Peter Parker\n"
            "Marvel Comics")).grid(row=1, column=1)

    def BotonSpiderman():
        spider_man = tk.Toplevel()
        spider_man.geometry('700x430')
        spider_man.title('¡Spider-Man!')
        spider_man.configure(background='yellow')

        def salir_ventana():
            spider_man.destroy()

        ImagenSpiderman1 = tk.PhotoImage(file = 'marvelfotos/spiderman2.png')
        PrintSpiderman1 = tk.Label(spider_man, image = ImagenSpiderman1)
        PrintSpiderman1.grid(row=0, column=0)

        tk.Label(spider_man, font=('Comic Sans', 18),
            text=("Spiderman\n Amazing Fantasy #15\n"
                "Peter Parker\n"
                "Marvel Comics\n" 
                "gran fuerza\n agilidad\n"
                " Un sentido arácnido\n" 
                "que le permite saber si\n" 
                "un peligro se cierne sobre él\n" 
                "antes de que suceda.\n")).place(x= 365, y= 30)
        botonsalir=tk.Button(spider_man, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 465, y =370)
        PrintSpiderman1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonSpiderman)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =300)

#-------------------Capitan america---------------------------------
    ImagenCapi = tk.PhotoImage(file = 'marvel/marvel-captain.png')
    PrintCapi = tk.Label(elframe,image = ImagenCapi)
    PrintCapi.grid(row = 2, column =0)

    tk.Label(elframe, font=8,
        text=("Capitan America\n Captain America Comics #1\n"
            "Steve Rogers\n"
            "Marvel Comics")).grid(row=2, column=1)
    
    def BotonCapi():
        capitan = tk.Toplevel()
        capitan.geometry('800x460')
        capitan.title('¡Capitan America!')
        capitan.configure(background='royal blue')

        def salir_ventana():
            capitan.destroy()

        ImagenCapi1 = tk.PhotoImage(file = 'marvelfotos/cap2.png')
        PrintCapi1 = tk.Label(capitan,image = ImagenCapi1)
        PrintCapi1.grid(row = 0, column =0)

        tk.Label(capitan, font=('Comic Sans', 18),
            text=("Capitan America\n Captain America Comics #1\n"
                "Steve Rogers\n"
                "Marvel Comics\n"
                "Gran habilidad con armas de fuego\n"
                "con el martillo Mjolnir y con su escudo\n"
                "inmune a gases y enfermedades\n"
                "Genio táctico\n"
                "acróbata experto\n")).place(x=375, y=100)
        botonsalir=tk.Button(capitan, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 530, y =390)
        PrintCapi1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonCapi)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =490)

#-------------------Iron man----------------------------------------
    ImagenIron = tk.PhotoImage(file = 'marvel/marvel-iron.png')
    PrintIron = tk.Label(elframe,image = ImagenIron)
    PrintIron.grid(row = 4, column =0)

    tk.Label(elframe, font=8,
        text=("Iron Man\n Tales of Suspense #39\n"
            "Tony Stark\n"
            "Marvel Comics")).grid(row=4, column=1)
    
    def BotonIron():
        iron = tk.Toplevel()
        iron.geometry('850x450')
        iron.title('¡Iron Man!')
        iron.configure(background='red4')

        def salir_ventana():
            iron.destroy()

        ImagenIron1 = tk.PhotoImage(file = 'marvelfotos/iron1.png')
        PrintIron1 = tk.Label(iron,image = ImagenIron1)
        PrintIron1.grid(row = 0, column =0)

        tk.Label(iron, font=('Comic Sans', 18),
            text=("Iron Man\n Tales of Suspense #39\n"
                "Tony Stark\n"
                "Marvel Comics\n"
                "Genio, filantropo,\n"
                "Playboy\n"
                "Repulsor de energía y misiles de proyección\n"
                "Uso de equipamiento\n"
                "Dispositivos y armamento de alta tecnología.")).place(x=350, y=80)
        botonsalir=tk.Button(iron, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 530, y =390)
        PrintIron1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonIron)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =685)

#----------------------Daredevil--------------------------------------
    ImagenDaredevil = tk.PhotoImage(file = 'marvel/marvel-daredevil.png')
    PrintDaredevil = tk.Label(elframe, image = ImagenDaredevil)
    PrintDaredevil.grid(row = 6, column = 0)

    
    tk.Label(elframe, font=8,
        text=("Daredevil\n Daredevil #1\n"
            "Matthew Michael Murdock\n"
            "Marvel Comics")).grid(row=6, column=1)
    
    def BotonDare():
        daredevil = tk.Toplevel()
        daredevil.geometry('810x485')
        daredevil.title('¡Daredevil!')
        daredevil.configure(background='indian red')

        def salir_ventana():
            daredevil.destroy()

        ImagenDaredevil1 = tk.PhotoImage(file = 'marvelfotos/daredevil1.png')
        PrintDaredevil1 = tk.Label(daredevil, image = ImagenDaredevil1)
        PrintDaredevil1.grid(row = 0, column = 0)

    
        tk.Label(daredevil, font=('Comic Sans', 18),
            text=("Daredevil\n Daredevil #1\n"
                "Matthew Michael Murdock\n"
                "Marvel Comics\n"
                "Ecolocalización radar cerebral\n"
                "que le permite ver a pesar de estar ciego\n"
                "Tirador de precisión perfecta\n"
                "Carencia del sentido del miedo\n")).place(x=360, y=100)
        botonsalir=tk.Button(daredevil, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 530, y =420)
        PrintDaredevil1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonDare)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =875)

#-----------------------Hulk------------------------------------------
    ImagenHulk = tk.PhotoImage(file = 'marvel/marvel-hulk.png')
    PrintHulk = tk.Label(elframe, image = ImagenHulk)
    PrintHulk.grid(row = 8, column = 0)

    tk.Label(elframe, font=8,
        text=("Hulk\n The Incredible Hulk #1\n"
            "Bruce Banner\n"
            "Marvel Comics")).grid(row=8, column=1)
    
    def BotonHulk():
        Hulk = tk.Toplevel()
        Hulk.geometry('800x485')
        Hulk.title('¡Hulk!')
        Hulk.configure(background='DarkOliveGreen4')

        def salir_ventana():
            Hulk.destroy()

        ImagenHulk1 = tk.PhotoImage(file = 'marvelfotos/hulk1.png')
        PrintHulk1 = tk.Label(Hulk, image = ImagenHulk1)
        PrintHulk1.grid(row = 0, column = 0)

        tk.Label(Hulk, font=('Comic Sans', 18),
            text=("Hulk\n The Incredible Hulk #1\n"
                "Bruce Banner\n"
                "Marvel Comics\n"
                "Regeneración\n"
                "Capacidad Pulmonar\n"
                "Hulk se adapta a cualquier ambiente\n"
                "Inmortalidad\n"
                " Super velocidad.\n")).place(x=380, y=100)
        botonsalir=tk.Button(Hulk, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 530, y =420)
        PrintHulk1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonHulk)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =1065)

#-----------------------Thor---------------------------------
    ImagenThor = tk.PhotoImage(file = 'marvel/marvel-thor.png')
    PrintThor = tk.Label(elframe, image = ImagenThor)
    PrintThor.grid(row = 1, column = 2)

    tk.Label(elframe, font=8,
        text=("Thor\n Journey into Myster #83\n"
            "Thor Odinson\n"
            "Marvel Comics")).grid(row=1, column=3)
    
    def BotonThor():
        thor = tk.Toplevel()
        thor.geometry('700x500')
        thor.title('¡Thor !')
        thor.configure(background='RoyalBlue1')

        def salir_ventana():
            thor.destroy()

        ImagenThor1 = tk.PhotoImage(file = 'marvelfotos/thor1.png')
        PrintThor1 = tk.Label(thor, image = ImagenThor1)
        PrintThor1.grid(row = 0, column = 0)

        tk.Label(thor, font=('Comic Sans', 18),
            text=("Thor\n Journey into Myster #83\n"
                "Thor Odinson\n"
                "Marvel Comics\n"
                "dios del trueno\n"
                "Fuerza sobrehumana\n"
                "velocidad\n"
                "durabilidad\n")).place(x=415, y=120)
        botonsalir=tk.Button(thor, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 490, y =440)
        PrintThor1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonThor)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 560, y =300)

#-----------------------Wolverine---------------------------------
    ImagenWolverine = tk.PhotoImage(file = 'marvel/marvel-wolverine.png')
    PrintWolverine = tk.Label(elframe, image = ImagenWolverine)
    PrintWolverine.grid(row = 2, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Wolverine\n The Incredible Hulk #180\n"
            "James Howlett\n"
            "Marvel Comics")).grid(row=2, column=3)
    
    def BotonWol():
        wolve = tk.Toplevel()
        wolve.geometry('910x500')
        wolve.title('¡Wolverine!')
        wolve.configure(background='yellow3')

        def salir_ventana():
            wolve.destroy()

        ImagenWolverine1 = tk.PhotoImage(file = 'marvelfotos/wolve1_.png')
        PrintWolverine1 = tk.Label(wolve, image = ImagenWolverine1)
        PrintWolverine1.grid(row = 0, column = 0)

        
        tk.Label(wolve, font=('Comic Sans', 14),
            text=("Wolverine\n The Incredible Hulk #180\n"
                "James Howlett\n"
                "Marvel Comics\n"
                "Es un mutante que posee sentidos afinados a los animales\n"
                "Capacidades físicas mejoradas\n"
                "Poderosa capacidad de regeneración\n"
                "Tres garras retráctiles en cada mano.\n")).place(x=400, y=130)
        botonsalir=tk.Button(wolve, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 600, y =430)
        PrintWolverine1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonWol)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 560, y =490)

#---------------------Cyclope---------------------------------------
    ImagenCyclops = tk.PhotoImage(file = 'marvel/marvel-cyclops.png')
    PrintCyclops = tk.Label(elframe, image = ImagenCyclops)
    PrintCyclops.grid(row = 4, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Cyclops\n X-Men #1\n"
            "Scott Summers\n"
            "Marvel Comics")).grid(row=4, column=3)
    
    def BotonCyclo():
        clyclo = tk.Toplevel()
        clyclo.geometry('850x460')
        clyclo.title('¡Clyclops!')
        clyclo.configure(background='bisque3')

        def salir_ventana():
            clyclo.destroy()

        ImagenCyclops1 = tk.PhotoImage(file = 'marvelfotos/cyclops.png')
        PrintCyclops1 = tk.Label(clyclo, image = ImagenCyclops1)
        PrintCyclops1.grid(row = 0, column = 0)

        tk.Label(clyclo, font=('Comic Sans', 14),
            text=("Cyclops\n X-Men #1\n"
                "Scott Summers\n"
                "Marvel Comics\n"
                "es un mutante \n"
                "con la capacidad de proyectar potentes\n" 
                "explosiones de fuerza a través de sus ojos\n"
                "Es visualmente distintivo\n" 
                "su visor de rubí de cuarzo,\n"
                "lo que le confiere el nombre clave de Cyclops (Cíclope).\n")).place(x=360, y=100)
        botonsalir=tk.Button(clyclo, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 560, y =390)
        PrintCyclops1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonCyclo)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 560, y =685)

#----------------------Hawkeye------------------------------------
    ImagenHawkeye = tk.PhotoImage(file = 'marvel/marvel-hawkeye.png')
    PrintHawkeye = tk.Label(elframe, image = ImagenHawkeye)
    PrintHawkeye.grid(row = 6, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Hawkeye\n Tales of Suspense #57\n"
            "Clinton Francis Barton\n"
            "Marvel Comics")).grid(row=6, column=3)
    
    def BotonHaw():
        haw = tk.Toplevel()
        haw.geometry('700x380')
        haw.title('¡Hawkeye!')
        haw.configure(background='purple')

        def salir_ventana():
            haw.destroy()

        ImagenHawkeye1 = tk.PhotoImage(file = 'marvelfotos/Hawkeye.png')
        PrintHawkeye1 = tk.Label(haw, image = ImagenHawkeye1)
        PrintHawkeye1.grid(row = 0, column = 0)

        
        tk.Label(haw, font=('Comic Sans', 14),
            text=("Hawkeye\n Tales of Suspense #57\n"
                "Clinton Francis Barton\n"
                "Marvel Comics\n"
                "es un eximio arquero\n"
                "y suele utilizar muchas flechas con trucos\n"
                "ademas de las corrientes\n"
                "Puede apuntar una flecha con perfecta\n" 
                "precision desde cualquier angulo.\n")).place(x=300, y=80)
        botonsalir=tk.Button(haw, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 420, y =320)
        PrintHawkeye1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonHaw)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 560, y =875)

#---------------------Silver surfer------------------------------
    ImagenSilver = tk.PhotoImage(file = 'marvel/marvel-silver.png')
    PrintSilver = tk.Label(elframe, image = ImagenSilver)
    PrintSilver.grid(row = 8, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Silver Surfer\n The Fantastic Four #48\n"
            "Norrin Radd\n"
            "Marvel Comics")).grid(row=8, column=3)
    
    def BotonSilver():
        sil = tk.Toplevel()
        sil.geometry('700x356')
        sil.title('¡Silver Surfer!')
        sil.configure(background='gray80')

        def salir_ventana():
            sil.destroy()

        ImagenSilver1 = tk.PhotoImage(file = 'marvelfotos/Silver_Surfer.png')
        PrintSilver1 = tk.Label(sil, image = ImagenSilver1)
        PrintSilver1.grid(row = 0, column = 0)

        
        tk.Label(sil, font=('Comic Sans', 14),
            text=("Silver Surfer\n The Fantastic Four #48\n"
                "Norrin Radd\n"
                "Marvel Comics\n"
                "poderes cósmicos,gracias a que Galactus\n"
                "se los concedió,como heraldo \n"
                "Tiene la capacidad de reunir \n"
                "energía cósmica del ambiente\n"
                "para concentrarla en su cuerpo\n"
                "a voluntad o lanzarla violentamente.\n")).place(x=300, y=50)
        botonsalir=tk.Button(sil, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 440, y =300)
        PrintSilver1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonSilver)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 560, y =1065)

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()



#--------------------DC----------------------------------------
def dcboton():
    elframe = tk.Toplevel()
    elframe.geometry('780x600')
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

    ImagenBienvenidaDC = tk.PhotoImage(file = 'dc1.png')
    PrintBienvenida_dc = tk.Label(elframe, image = ImagenBienvenidaDC)
    PrintBienvenida_dc.grid(row=0, column=1)
    
    ImagenBienvenidaDC1 = tk.PhotoImage(file = 'dc2.png')
    PrintBienvenida_dc1 = tk.Label(elframe, image = ImagenBienvenidaDC1)
    PrintBienvenida_dc1.grid(row=0, column=2)

#----------------------Superman---------------------
    ImagenSuperman = tk.PhotoImage(file = 'dc/dc-superman.png')
    PrintSpiderman = tk.Label(elframe, image = ImagenSuperman)
    PrintSpiderman.grid(row =1, column = 0)

    tk.Label(elframe, font=8,
        text=("Superman\n Action Comics #1\n"
            "kal-El\n"
            "DC Comics")).grid(row=1, column=1)
    
    def BotonSuper():
        superman = tk.Toplevel()
        superman.geometry('700x500')
        superman.title('¡Superman!')
        superman.configure(background='black')

        def salir_ventana():
            superman.destroy()

        ImagenSuperman1 = tk.PhotoImage(file = 'dcfotos/tomsuper.png')
        PrintSuperman1 = tk.Label(superman, image = ImagenSuperman1)
        PrintSuperman1.grid(row=0, column=0)

        tk.Label(superman, font=('Comic Sans', 18),
            text=("Superman\n Action Comics #1\n"
                "kal-El\n"
                "DC Comics\n"
                "súper fuerza\n"
                "invulnerabilidad\n"
                "la capacidad de volar\n"
                "visión calorífica\n"
                "el aliento helado.\n")).place(x=410, y=100)
        botonsalir=tk.Button(superman, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 480, y =430)
        PrintSuperman1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonSuper)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =290)

#----------------Wonder woman----------------------------------
    ImagenWonder = tk.PhotoImage(file = 'dc/dc-wonder.png')
    PrintWonder = tk.Label(elframe, image = ImagenWonder)
    PrintWonder.grid(row =2, column = 0)

    tk.Label(elframe, font=8,
        text=("Wonder Woman\n All Star Comics #8\n"
            "Princess Diana\n"
            "DC Comics")).grid(row=2, column=1)
    
    def BotonWonder():
        wonder = tk.Toplevel()
        wonder.geometry('700x400')
        wonder.title('¡Wonder Woman!')
        wonder.configure(background='medium spring green')

        def salir_ventana():
            wonder.destroy()

        ImagenWonder1 = tk.PhotoImage(file = 'dcfotos/wonder.png')
        PrintWonder1 = tk.Label(wonder, image = ImagenWonder1)
        PrintWonder1.grid(row =0, column = 0)

        tk.Label(wonder, font=('Comic Sans', 14),
            text=("Wonder Woman\n All Star Comics #8\n"
                "Princess Diana\n"
                "DC Comics\n"
                "Invulnerabilidad al fuego\n"
                "Agilidad superhumana\n"
                "Teletransportación dimensional\n"
                "Durabilidad superhumana\n"
                "Comunicación con animales\n"
                "Multi-lenguaje.\n")).place(x=350, y=60)
        botonsalir=tk.Button(wonder, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 435, y =340)
        PrintWonder1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonWonder)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =480)

#--------------------Robin nightwing-----------------------
    ImagenRobin = tk.PhotoImage(file = 'dc/dc-robin.png')
    PrintRobin = tk.Label(elframe, image = ImagenRobin)
    PrintRobin.grid(row =4, column = 0)

    tk.Label(elframe, font=8,
        text=("Robin/Nightwing\n Detective Comics #38\n"
            "Dick Grayson\n"
            "DC Comics")).grid(row=4, column=1)
    
    def BotonRobin():
        robin = tk.Toplevel()
        robin.geometry('800x506')
        robin.title('¡Robin/Nightwing!')
        robin.configure(background='honeydew4')

        def salir_ventana():
            robin.destroy()

        ImagenRobin1 = tk.PhotoImage(file = 'dcfotos/robin.png')
        PrintRobin1 = tk.Label(robin, image = ImagenRobin1)
        PrintRobin1.grid(row =0, column = 0)

        tk.Label(robin, font=('Comic Sans', 18),
            text=("Robin/Nightwing\n Detective Comics #38\n"
                "Dick Grayson\n"
                "DC Comics\n"
                "es experto en las artes marciales\n"
                "crea armas simples\n")).place(x=425, y=150)
        botonsalir=tk.Button(robin, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 550, y =430)
        PrintRobin1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonRobin)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =675)

#-----------------Flash---------------------------
    ImagenFlash = tk.PhotoImage(file = 'dc/dc-flash.png')
    PrintFlash = tk.Label(elframe, image = ImagenFlash)
    PrintFlash.grid(row =6, column = 0)

    tk.Label(elframe, font=8,
        text=("Flash\n Flash Comics #1\n"
            "Barry Allen\n"
            "DC Comics")).grid(row=6, column=1)
    
    def BotonFlash():
        flash = tk.Toplevel()
        flash.geometry('840x455')
        flash.title('¡Flash!')
        flash.configure(background='firebrick2')

        def salir_ventana():
            flash.destroy()

        ImagenFlash1 = tk.PhotoImage(file = 'dcfotos/flashba.png')
        PrintFlash1 = tk.Label(flash, image = ImagenFlash1)
        PrintFlash1.grid(row =0, column = 0)

        tk.Label(flash, font=('Comic Sans', 16),
            text=("Flash\n Flash Comics #1\n"
                "Barry Allen\n"
                "DC Comics\n"
                "pensar y reaccionar a velocidad luz\n"
                "además de tener una resistencia sobrehumana\n"
                "que les permite recorrer distancias increíbles.\n")).place(x=380, y=150)
        botonsalir=tk.Button(flash, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 555, y =390)
        PrintFlash1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonFlash)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =870)

#--------------Linterna verde--------------------------
    ImagenVerde = tk.PhotoImage(file = 'dc/dc-green.png')
    PrintVerde = tk.Label(elframe, image = ImagenVerde)
    PrintVerde.grid(row =8, column = 0)

    tk.Label(elframe, font=8,
        text=("Green Lantern\n All-American Comics #16\n"
            "Alan Scott\n"
            "DC Comics")).grid(row=8, column=1)
    
    def BotonVerde():
        verde = tk.Toplevel()
        verde.geometry('800x545')
        verde.title('¡Green Lantern!')
        verde.configure(background='forest green')

        def salir_ventana():
            verde.destroy()

        ImagenVerde1 = tk.PhotoImage(file = 'dcfotos/linver.png')
        PrintVerde1 = tk.Label(verde, image = ImagenVerde1)
        PrintVerde1.grid(row =0, column = 0)

        tk.Label(verde, font=('Comic Sans', 16),
            text=("Green Lantern\n All-American Comics #16\n"
                "Alan Scott\n"
                "DC Comics\n"
                "se caracterizan por un anillo de poder\n"
                "y la capacidad de crear manifestaciones\n"
                "de luz sólida con los susodichos anillos.\n")).place(x=390, y=180)
        botonsalir=tk.Button(verde, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 520, y =470)
        PrintVerde1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonVerde)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 150, y =1065)

#--------------Flecha verde-----------------------
    ImagenFlecha = tk.PhotoImage(file = 'dc/dc-arrow.png')
    PrintFlecha = tk.Label(elframe, image = ImagenFlecha)
    PrintFlecha.grid(row =1, column = 2)

    tk.Label(elframe, font=8,
        text=("Green Arrow\n More Fun Comics #73\n"
            "Oliver Queen\n"
            "DC Comics")).grid(row=1, column=3)
    
    def BotonFlecha():
        flecha = tk.Toplevel()
        flecha.geometry('740x505')
        flecha.title('¡Green Arrow!')
        flecha.configure(background='royal blue')

        def salir_ventana():
            flecha.destroy()

        ImagenFlecha1 = tk.PhotoImage(file = 'dcfotos/flechaoli.png')
        PrintFlecha1 = tk.Label(flecha, image = ImagenFlecha1)
        PrintFlecha1.grid(row =0, column = 0)

        tk.Label(flecha, font=('Comic Sans', 16),
            text=("Green Arrow\n More Fun Comics #73\n"
                "Oliver Queen\n"
                "DC Comics\n"
                "Posee una gran habilidad como arquero\n"
                "y tiene un amplio arsenal de flechas\n"
                "Excelente rastreador\n"
                "manejo de armas y piloto aviador.\n")).place(x=350, y=150)
        botonsalir=tk.Button(flecha, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 490, y =440)
        PrintFlecha1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonFlecha)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 550, y =290)

#-----------------Martian Manhunter------------------------
    ImagenMartin = tk.PhotoImage(file = 'dc/dc-martian.png')
    PrintMartin = tk.Label(elframe, image = ImagenMartin)
    PrintMartin.grid(row = 2, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Martian Manhunter\n Detective Comics #225\n"
            "Martian Manhunter\n"
            "DC Comics")).grid(row=2, column=3)
    
    def BotonMartin():
        martin = tk.Toplevel()
        martin.geometry('700x510')
        martin.title('¡Martian Manhunter!')
        martin.configure(background='RoyalBlue4')

        def salir_ventana():
            martin.destroy()

        ImagenMartin1 = tk.PhotoImage(file = 'dcfotos/martian.png')
        PrintMartin1 = tk.Label(martin, image = ImagenMartin1)
        PrintMartin1.grid(row = 0, column = 0)

        tk.Label(martin, font=('Comic Sans', 18),
            text=("Martian Manhunter\n Detective Comics #225\n"
                "Martian Manhunter\n"
                "DC Comics\n"
                "Superfuerza Velocidad \n"
                "Telepatía Telekinesis\n"
                "Cambio de forma\n"
                "Nueve sentidos\n")).place(x=390, y=140)
        botonsalir=tk.Button(martin, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 465, y =440)
        PrintMartin1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonMartin)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 550, y =480)

#-------------Blue Beetle------------------------
    ImagenBlue = tk.PhotoImage(file = 'dc/dc-blue.png')
    PrintBlue = tk.Label(elframe, image = ImagenBlue)
    PrintBlue.grid(row = 4, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Blue Beetle\n Mystery Men Comics #1\n"
            "Dan Garret\n"
            "DC Comics")).grid(row=4, column=3)
    
    def BotonBlue():
        blue = tk.Toplevel()
        blue.geometry('700x505')
        blue.title('¡Blue Beetle!')
        blue.configure(background='SteelBlue4')

        def salir_ventana():
            blue.destroy()

        ImagenBlue1 = tk.PhotoImage(file = 'dcfotos/bluebe.png')
        PrintBlue1 = tk.Label(blue, image = ImagenBlue1)
        PrintBlue1.grid(row = 0, column = 0)

        
        tk.Label(blue, font=('Comic Sans', 18),
            text=("Blue Beetle\n Mystery Men Comics #1\n"
                "Dan Garret\n"
                "DC Comics\n"
                "capacidad de volar\n"
                "superfuerza y luminosidad\n")).place(x=370, y=160)
        botonsalir=tk.Button(blue, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)
        botonsalir.place(x = 465, y =430)
        PrintBlue1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonBlue)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 550, y =675)

#----------------Black Canary------------------
    ImagenBlack = tk.PhotoImage(file = 'dc/dc-black.png')
    PrintBlack = tk.Label(elframe, image = ImagenBlack)
    PrintBlack.grid(row = 6, column = 2)

    
    tk.Label(elframe, font=8,
        text=("Black Canary\n Flash Comics #86\n"
            "Dinah Drake\n"
            "DC Comics")).grid(row=6, column=3)
    
    def BotonBlack():
        black = tk.Toplevel()
        black.geometry('1050x550')
        black.title('¡Black Canary!')
        black.configure(background='orchid2')

        def salir_ventana():
            black.destroy()

        ImagenBlack1 = tk.PhotoImage(file = 'dcfotos/blackca.png')
        PrintBlack1 = tk.Label(black, image = ImagenBlack1)
        PrintBlack1.grid(row = 0, column = 0)

        
        tk.Label(black, font=('Comic Sans', 16),
            text=("Black Canary\n Flash Comics #86\n"
                "Dinah Drake\n"
                "DC Comics\n"
                "Su superpoder más conocido es el grito del canario\n"
                "Un chillido ultrasónico que le permite aturdir a sus enemigos\n"
                "E incluso destruir objetos\n")).place(x=480, y=180)
        botonsalir=tk.Button(black, text = "RETROCEDER", command = salir_ventana,fg = 'red', padx = 10, pady = 10)     
        botonsalir.config(width=12, height=0)
        botonsalir.place(x = 720, y =480)
        PrintBlack1.mainloop()

    boton_1 = tk.Button(elframe, text = "Más", command = BotonBlack)
    boton_1.config(width=8, height=0)
    boton_1.place(x = 550, y =870)

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()


#--------------BOTONES-----------
BotonMarvel = tk.Button(RaizComic, text = 'MARVEL', command = marvelbo, fg = 'RED', padx = 40, pady = 5)
BotonMarvel.place(x=100, y=80)
botonsalir = tk.Button(RaizComic, text = 'SALIR', command= salir, padx = 10, pady = 10)
botonsalir.place(x=275, y= 500)
BotonDC = tk.Button(RaizComic, text= 'DC', command= dcboton, fg = 'BLUE', padx = 50, pady = 5)
BotonDC.place(x=380, y=80)
#botonbuscar = tk.Button(RaizComic, text= 'BUSCAR', padx = 10, pady = 5)
#botonbuscar.place(x=275,y=80)


RaizComic.mainloop()