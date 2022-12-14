#Animal
car1 = input()
car2 = input()
car3 = input()

if car1 == 'vertebrado':
    if car2 == 'ave':
        if car3 == 'carnivoro':
            print('aguia')
        elif car3 == 'onivoro':
            print('pomba')
    elif car2 == 'mamifero':
        if car3 == 'onivoro':
            print('homem')
        elif car3 == 'herbivoro':
            print('vaca')
elif car1 == 'invertebrado':
    if car2 == 'inseto':
        if car3 == 'hematofago':
            print('pulga')
        elif car3 == 'herbivoro':
            print('lagarta')
    elif car2 == 'anelideo':
        if car3 == 'hematofago':
            print('sanguessuga')
        elif car3 == 'onivoro':
            print('minhoca')
