import data
import util
import data


op=-1
while(op!=0):
    print('<1> buscar heroe por id')
    print('<2> mostrar heroes por publisher')
    print('<3> filtrar heroes por el superhero')
    print('<0> Salir')

    op = int(input('Ingresar opción: '))

    print('')
    if op == 1:
        id = input('Ingresar id de heroe: ')
        heroe = util.getHeroePorId(id)
        
        if not heroe:
            print('Heroe', id, 'no existe')
            
        else:
            util.printHeroe(heroe)

    elif op == 2:
        publisher = input('Ingresar publisher:')
        heroes = util.getHeroePorPublihser(publisher)
        if len(heroes) > 0:
            util.printHeroes(heroes)
        else:
            print('Publisher incorrecto')

    elif op == 3:
        superHero = input('Ingresar superHero:')
        heroes = util.getHeroePorSuperHero(superHero)
        if len(heroes) > 0:
            util.printHeroes(heroes)
        else:
            print('No se encontro ninguna coincidencia')

    print('')