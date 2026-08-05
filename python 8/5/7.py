heroes = ['ironman' , 'thor' , 'hulk' , 'superman' , 'spiderman'] 
h2 = ['dr.strang' , 'cpt.america' , 'black panter' , 'ant man']

heroes.insert(0, h2[0])
print(heroes.index('thor'))
heroes.insert(heroes.index('thor'), h2[1])
print(heroes)
heroes.remove('superman')
heroes.append('ant man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] = 'wonder woman'
print(heroes)
copyheroes = [] + heroes
print(heroes)
copyheroes[0] = 'hanuman'
print(heroes)
print(copyheroes)