import os
import django,csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_syst_admin_biblioteca.settings')
django.setup()



from biblioteca_app.models import Libro

with open("listalibro.txt") as csvfile:
    for line in csvfile:
        nombre,autor,genero,copias="","","",""
        if(line[0]=='"'):
            nombre = line.split(',')[0] + line.split(',')[1]
            autor = line.split(',')[2] + line.split(',')[3]
            genero = line.split(',')[4] 
            copias = line.split(',')[5]
            
        else:
            nombre = line.split(',')[0]
            autor = line.split(',')[1] + line.split(',')[2]
            genero = line.split(',')[3]
            copias = line.split(',')[4]

        if copias.isnumeric():  
            libro = Libro.objects.create(titulo=nombre,autor=autor,genero=genero,copias=copias)
            libro.save()
            print(f"Libro Agregado - {nombre}")
        
        
            