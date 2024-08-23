set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('per' in set_countries)

#Agregar a conjunto
set_countries.add('per')
print(set_countries)

#Actualizar conjunto
set_countries.update({'bra', 'arg'})
print(set_countries)

#Remover elementos de conjunto
set_countries.remove('bra')
print(set_countries)

#Elimina sin lanzar error
set_countries.discard('bra')
print(set_countries)

#Limpiar el conjunto
set_countries.clear()
print(len(set_countries))