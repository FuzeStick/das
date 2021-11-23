import os
os.system('docker images')
print('введите id образа')
id=input()
print('Название на латинице для образа')
name=input()
os.system(f'docker commit  {id} {name}')