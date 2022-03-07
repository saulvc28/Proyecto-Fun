import tkinter as tk
import proyecto2

def busqueda_man():
    busqueda_por_man = tk.Toplevel()
    busqueda_por_man.geometry('800x500')
    busqueda_por_man.title('BUSQUEDA')

    scrollbar = tk.Scrollbar(busqueda_por_man)
    c = tk.Canvas(busqueda_por_man, yscrollcommand=scrollbar.set)
    scrollbar.config(command= c.yview)
    scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
    elframe = tk.Frame(c)
    c.pack(side='left', fill='both', expand= True)
    c.create_window(0,0, window= elframe, anchor= 'nw')
    an = tk.Label(elframe, text= 'RESULTADOS DE TU BUSQUEDA:', font= ('Comic Sans', 8))
    an.grid(row=0, column=0)

    #----------------Spiderman-------------------------------------------
    ImagenSpiderman1 = tk.PhotoImage(file = 'busqueda/marvel-spider.png')
    PrintSpiderman1 = tk.Label(elframe, image = ImagenSpiderman1)
    PrintSpiderman1.grid(row=1, column=0) 

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Spiderman\n Amazing Fantasy #15\n Peter Parker\n Marvel Comics")).grid(row=1, column=1)
    
    #---------------------Iron man-------------------------------
    ImagenIron1 = tk.PhotoImage(file = 'busqueda/marvel-iron.png')
    PrintIron1 = tk.Label(elframe,image = ImagenIron1)        
    PrintIron1.grid(row = 2, column =0)

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Iron Man\n Tales of Suspense #39\n Tony Stark\n Marvel Comics")).grid(row=2, column=1)

    #---------------------Superman-------------------------------------
    ImagenSuperman1 = tk.PhotoImage(file = 'busqueda/dc-superman.png')
    PrintSuperman1 = tk.Label(elframe, image = ImagenSuperman1)
    PrintSuperman1.grid(row=3, column=0)
    
    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Superman\n Action Comics #1\n kal-El\n DC Comics")).grid(row=3, column=1)

    #-------------------Wonder woman--------------------------------------
    ImagenWonder1 = tk.PhotoImage(file = 'busqueda/dc-wonder.png')
    PrintWonder1 = tk.Label(elframe, image = ImagenWonder1)
    PrintWonder1.grid(row =4, column = 0)

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Wonder Woman\n All Star Comics #8\n Princess Diana\n DC Comics")).grid(row=4, column=1)

    #-----------------Martian Manhunter------------------------------
    ImagenMartin1 = tk.PhotoImage(file = 'busqueda/dc-martian.png')
    PrintMartin1 = tk.Label(elframe, image = ImagenMartin1)
    PrintMartin1.grid(row = 1, column = 2)

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Martian Manhunter\n Detective Comics #225\n Martian Manhunter\n DC Comics")).grid(row=1, column=3)

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()
    busqueda_por_man.mainloop()


def busqueda_green():
    busqueda_green = tk.Toplevel()
    busqueda_green.geometry('700x500')
    busqueda_green.title('BUSQUEDA')

    scrollbar = tk.Scrollbar(busqueda_green)
    c = tk.Canvas(busqueda_green, yscrollcommand=scrollbar.set)
    scrollbar.config(command= c.yview)
    scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
    elframe = tk.Frame(c)
    c.pack(side='left', fill='both', expand= True)
    c.create_window(0,0, window= elframe, anchor= 'nw')
    an = tk.Label(elframe, text= 'RESULTADOS DE TU BUSQUEDA:', font= ('Comic Sans', 8))
    an.grid(row=0, column=0)

    #------------------Linterna Verde---------------------
    ImagenVerde1 = tk.PhotoImage(file = 'busqueda/dc-green.png')
    PrintVerde1 = tk.Label(elframe, image = ImagenVerde1)
    PrintVerde1.grid(row =1, column = 0)

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Green Lantern\n All-American Comics #16\n Alan Scott\n DC Comics")).grid(row=1, column=1)

    #------------------Flacha verde-----------------------------
    ImagenFlecha1 = tk.PhotoImage(file = 'busqueda/dc-arrow.png')
    PrintFlecha1 = tk.Label(elframe, image = ImagenFlecha1)
    PrintFlecha1.grid(row =2, column = 0)

    tk.Label(elframe, font=('Comic Sans', 16),
    text=("Green Arrow\n More Fun Comics #73\n Oliver Queen\n DC Comics")).grid(row=2, column=1)

    elframe.update()
    c.config(scrollregion=c.bbox('all'))
    elframe.mainloop()
    busqueda_green.mainloop()

def BotonSpiderman():
    spider_man = tk.Toplevel()
    spider_man.geometry('750x500')
    spider_man.title('¡Spider-Man!')

    ImagenSpiderman1 = tk.PhotoImage(file = 'marvelfotos/spiderman2-.png')
    PrintSpiderman1 = tk.Label(spider_man, image = ImagenSpiderman1)
    PrintSpiderman1.grid(row=0, column=0)

    tk.Label(spider_man, font=('Comic Sans', 18),
    text=("Spiderman\n Amazing Fantasy #15\n Peter Parker\n Marvel Comics\n Gran fuerza\n agilidad\n Un sentido arácnido\n que le permite saber si\n un peligro se cierne sobre él\n antes de que suceda.\n")).place(x= 415, y= 100)

    PrintSpiderman1.mainloop()

def BotonIron():
    iron = tk.Toplevel()
    iron.geometry('850x500')
    iron.title('¡Iron Man!')

    ImagenIron1 = tk.PhotoImage(file = 'marvelfotos/iron1-.png')
    PrintIron1 = tk.Label(iron,image = ImagenIron1)
    PrintIron1.grid(row = 0, column =0)

    tk.Label(iron, font=('Comic Sans', 16),
    text=("Iron Man\n Tales of Suspense #39\n Tony Stark\n Marvel Comics\n Genio, filantropo,\n Playboy\n Repulsor de energía y misiles de proyección\n Uso de equipamiento\n Dispositivos y armamento de alta tecnología.")).place(x=410, y=135)

    PrintIron1.mainloop()

def BotonHulk():
    Hulk = tk.Toplevel()
    Hulk.geometry('830x500')
    Hulk.title('¡Hulk!')

    ImagenHulk1 = tk.PhotoImage(file = 'marvelfotos/hulk1-.png')
    PrintHulk1 = tk.Label(Hulk, image = ImagenHulk1)
    PrintHulk1.grid(row = 0, column = 0)

    tk.Label(Hulk, font=('Comic Sans', 18),
    text=("Hulk\n The Incredible Hulk #1\n Bruce Banner\n Marvel Comics\n Regeneración\n Capacidad Pulmonar\n Hulk se adapta a cualquier ambiente\n Inmortalidad\n Super velocidad.\n")).place(x=410, y=100)

    PrintHulk1.mainloop()

def BotonCyclo():
    clyclo = tk.Toplevel()
    clyclo.geometry('850x460')
    clyclo.title('¡Clyclops!')

    ImagenCyclops1 = tk.PhotoImage(file = 'marvelfotos/cyclops.png')
    PrintCyclops1 = tk.Label(clyclo, image = ImagenCyclops1)
    PrintCyclops1.grid(row = 0, column = 0)

    tk.Label(clyclo, font=('Comic Sans', 14),
    text=("Cyclops\n X-Men #1\n Scott Summers\n Marvel Comics\n Es un mutante \n con la capacidad de proyectar potentes\n explosiones de fuerza a través de sus ojos\n Es visualmente distintivo\n su visor de rubí de cuarzo,\n lo que le confiere el nombre clave de Cyclops (Cíclope).\n")).place(x=360, y=100)

    PrintCyclops1.mainloop()

def BotonCapi():
    capitan = tk.Toplevel()
    capitan.geometry('850x500')
    capitan.title('¡Capitan America!')

    ImagenCapi1 = tk.PhotoImage(file = 'marvelfotos/cap2-.png')
    PrintCapi1 = tk.Label(capitan,image = ImagenCapi1)
    PrintCapi1.grid(row = 0, column =0)

    tk.Label(capitan, font=('Comic Sans', 18),
    text=("Capitan America\n Captain America Comics #1\n Steve Rogers\n Marvel Comics\n Gran habilidad con armas de fuego\n con el martillo Mjolnir y con su escudo\n inmune a gases y enfermedades\n Genio táctico\n acróbata experto\n")).place(x=410, y=120)

    PrintCapi1.mainloop()    

def BotonThor():
    thor = tk.Toplevel()
    thor.geometry('750x500')
    thor.title('¡Thor !')

    ImagenThor1 = tk.PhotoImage(file = 'marvelfotos/thor1-.png')
    PrintThor1 = tk.Label(thor, image = ImagenThor1)
    PrintThor1.grid(row = 0, column = 0)

    tk.Label(thor, font=('Comic Sans', 18),
    text=("Thor\n Journey into Myster #83\n Thor Odinson\n Marvel Comicsdios del trueno\n Fuerza sobrehumana\n Velocidad\n Durabilidad\n")).place(x=410, y=150)

    PrintThor1.mainloop()    

def BotonWol():
    wolve = tk.Toplevel()
    wolve.geometry('915x500')
    wolve.title('¡Wolverine!')

    ImagenWolverine1 = tk.PhotoImage(file = 'marvelfotos/wolve1-.png')
    PrintWolverine1 = tk.Label(wolve, image = ImagenWolverine1)
    PrintWolverine1.grid(row = 0, column = 0)

    tk.Label(wolve, font=('Comic Sans', 14),
    text=("Wolverine\n The Incredible Hulk #180\n James Howlett\n Marvel Comics\n Es un mutante que posee sentidos afinados a los animales\n Capacidades físicas mejoradas\n Poderosa capacidad de regeneración\n Tres garras retráctiles en cada mano.\n")).place(x=405, y=155)

    PrintWolverine1.mainloop()    

def BotonHaw():
    haw = tk.Toplevel()
    haw.geometry('765x500')
    haw.title('¡Hawkeye!')

    ImagenHawkeye1 = tk.PhotoImage(file = 'marvelfotos/Hawkeye-.png')
    PrintHawkeye1 = tk.Label(haw, image = ImagenHawkeye1)
    PrintHawkeye1.grid(row = 0, column = 0)

    tk.Label(haw, font=('Comic Sans', 14),
    text=("Hawkeye\n Tales of Suspense #57\n Clinton Francis Barton\n Marvel Comics\n Es un arquero experto\n y suele utilizar muchas flechas con trucos\n ademas de las corrientes\n Puede apuntar una flecha con perfecta\n precision desde cualquier angulo.\n")).place(x=405, y=150)

    PrintHawkeye1.mainloop()

def BotonSilver():
    sil = tk.Toplevel()
    sil.geometry('775x500')
    sil.title('¡Silver Surfer!')

    ImagenSilver1 = tk.PhotoImage(file = 'marvelfotos/Silver_Surfer-.png')
    PrintSilver1 = tk.Label(sil, image = ImagenSilver1)
    PrintSilver1.grid(row = 0, column = 0)

    tk.Label(sil, font=('Comic Sans', 14),
    text=("Silver Surfer\n The Fantastic Four #48\n Norrin Radd\n Marvel Comics\n poderes cósmicos,gracias a que Galactus\n se los concedió,como heraldo \n Tiene la capacidad de reunir \n energía cósmica del ambiente\n para concentrarla en su cuerpo\n a voluntad o lanzarla violentamente.\n")).place(x=405, y=140)

    PrintSilver1.mainloop()

def BotonDare():
    daredevil = tk.Toplevel()
    daredevil.geometry('860x500')
    daredevil.title('¡Daredevil!')

    ImagenDaredevil1 = tk.PhotoImage(file = 'marvelfotos/daredevil1-.png')
    PrintDaredevil1 = tk.Label(daredevil, image = ImagenDaredevil1)
    PrintDaredevil1.grid(row = 0, column = 0)

    tk.Label(daredevil, font=('Comic Sans', 18),
    text=("Daredevil\n Daredevil #1\n Matthew Michael Murdock\n Marvel Comics\n Ecolocalización radar cerebral\n que le permite ver a pesar de estar ciego\n Tirador de precisión perfecta\n Carencia del sentido del miedo\n")).place(x=405, y=130)

    PrintDaredevil1.mainloop()

def BotonSuper():
    superman = tk.Toplevel()
    superman.geometry('700x500')
    superman.title('¡Superman!')

    ImagenSuperman1 = tk.PhotoImage(file = 'dcfotos/tomsuper.png')
    PrintSuperman1 = tk.Label(superman, image = ImagenSuperman1)
    PrintSuperman1.grid(row=0, column=0)

    tk.Label(superman, font=('Comic Sans', 18),
    text=("Superman\n Action Comics #1\n kal-El\n DC Comics\n súper fuerza\n invulnerabilidad\n la capacidad de volar\n visión calorífica\n el aliento helado.\n")).place(x=395, y=100)

    PrintSuperman1.mainloop()

def BotonVerde():
    verde = tk.Toplevel()
    verde.geometry('800x545')
    verde.title('¡Green Lantern!')

    ImagenVerde1 = tk.PhotoImage(file = 'dcfotos/linver.png')
    PrintVerde1 = tk.Label(verde, image = ImagenVerde1)
    PrintVerde1.grid(row =0, column = 0)

    tk.Label(verde, font=('Comic Sans', 16),
    text=("Green Lantern\n All-American Comics #16\n Alan Scott\n DC Comics\n Se caracterizan por un anillo de poder\n Y la capacidad de crear manifestaciones\n de luz sólida con los susodichos anillos.\n")).place(x=390, y=180)

    PrintVerde1.mainloop()

def BotonWonder():
    wonder = tk.Toplevel()
    wonder.geometry('700x400')
    wonder.title('¡Wonder Woman!')

    ImagenWonder1 = tk.PhotoImage(file = 'dcfotos/wonder.png')
    PrintWonder1 = tk.Label(wonder, image = ImagenWonder1)
    PrintWonder1.grid(row =0, column = 0)

    tk.Label(wonder, font=('Comic Sans', 14),
    text=("Wonder Woman\n All Star Comics #8\n Princess Diana\n DC Comics\n Invulnerabilidad al fuego\n Agilidad superhumana\n Teletransportación dimensional\n Durabilidad superhumana\n Comunicación con animales\n Multi-lenguaje.\n")).place(x=350, y=60)

    PrintWonder1.mainloop()

def BotonRobin():
    robin = tk.Toplevel()
    robin.geometry('800x506')
    robin.title('¡Robin/Nightwing!')

    ImagenRobin1 = tk.PhotoImage(file = 'dcfotos/robin.png')
    PrintRobin1 = tk.Label(robin, image = ImagenRobin1)
    PrintRobin1.grid(row =0, column = 0)

    tk.Label(robin, font=('Comic Sans', 18),
    text=("Robin/Nightwing\n Detective Comics #38\n Dick Grayson\n DC Comics\n Es experto en las artes marciales\n Crea armas simples\n")).place(x=425, y=150)

    PrintRobin1.mainloop()

def BotonBlack():
    black = tk.Toplevel()
    black.geometry('1050x550')
    black.title('¡Black Canary!')

    ImagenBlack1 = tk.PhotoImage(file = 'dcfotos/blackca.png')
    PrintBlack1 = tk.Label(black, image = ImagenBlack1)
    PrintBlack1.grid(row = 0, column = 0)

    tk.Label(black, font=('Comic Sans', 16),
    text=("Black Canary\n Flash Comics #86\n Dinah Drake\n DC Comics\n Su superpoder más conocido es el grito del canario\n Un chillido ultrasónico que le permite aturdir a sus enemigos\n E incluso destruir objetos\n")).place(x=480, y=180)

    PrintBlack1.mainloop()

def BotonFlash():
    flash = tk.Toplevel()
    flash.geometry('840x455')
    flash.title('¡Flash!')

    ImagenFlash1 = tk.PhotoImage(file = 'dcfotos/flashba.png')
    PrintFlash1 = tk.Label(flash, image = ImagenFlash1)
    PrintFlash1.grid(row =0, column = 0)

    tk.Label(flash, font=('Comic Sans', 16),
    text=("Flash\n Flash Comics #1\n Barry Allen\n DC Comics\n pensar y reaccionar a velocidad luz\n además de tener una resistencia sobrehumana\n que les permite recorrer distancias increíbles.\n")).place(x=380, y=150)

    PrintFlash1.mainloop()

def BotonFlecha():
    flecha = tk.Toplevel()
    flecha.geometry('740x505')
    flecha.title('¡Green Arrow!')

    ImagenFlecha1 = tk.PhotoImage(file = 'dcfotos/flechaoli.png')
    PrintFlecha1 = tk.Label(flecha, image = ImagenFlecha1)
    PrintFlecha1.grid(row =0, column = 0)

    tk.Label(flecha, font=('Comic Sans', 16),
    text=("Green Arrow\n More Fun Comics #73\n Oliver Queen\n DC Comics\n Posee una gran habilidad como arquero\n Y tiene un amplio arsenal de flechas\n Excelente rastreador\n Manejo de armas y piloto aviador.\n")).place(x=350, y=150)

    PrintFlecha1.mainloop()

def BotonMartin():
    martin = tk.Toplevel()
    martin.geometry('700x510')
    martin.title('¡Martian Manhunter!')

    ImagenMartin1 = tk.PhotoImage(file = 'dcfotos/martian.png')
    PrintMartin1 = tk.Label(martin, image = ImagenMartin1)
    PrintMartin1.grid(row = 0, column = 0)

    tk.Label(martin, font=('Comic Sans', 18),
    text=("Martian Manhunter\n Detective Comics #225\n Martian Manhunter\n DC Comics\n Superfuerza Velocidad \n Telepatía Telekinesis\n Cambio de forma\n Nueve sentidos\n")).place(x=390, y=140)

    PrintMartin1.mainloop()

def BotonBlue():
    blue = tk.Toplevel()
    blue.geometry('700x505')
    blue.title('¡Blue Beetle!')

    ImagenBlue1 = tk.PhotoImage(file = 'dcfotos/bluebe.png')
    PrintBlue1 = tk.Label(blue, image = ImagenBlue1)
    PrintBlue1.grid(row = 0, column = 0)

    tk.Label(blue, font=('Comic Sans', 18),
    text=("Blue Beetle\n Mystery Men Comics #1\n Dan Garret\n DC Comics\n Capacidad de volar\n Superfuerza y luminosidad\n")).place(x=370, y=160)

    PrintBlue1.mainloop()