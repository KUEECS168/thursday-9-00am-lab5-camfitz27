def funtion():
    user=0
    planets=[' ','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune',' ']
    while user != 'y':
        planet=input('Enter a planet name: ')
        planets.append(planet)
        user=input('Is the mission over? (y/n): ')
        
    neighbor=input('Which planet do you want the neighbors for?: ')
    index=planets.index(neighbor)
    print(planets[index-1])
    print(planets[index+1])

    print('Program ending...')
funtion()
