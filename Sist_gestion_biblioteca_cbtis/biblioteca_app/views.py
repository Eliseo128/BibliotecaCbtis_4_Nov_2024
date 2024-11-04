from django.shortcuts import render,redirect
from .models import Libro
from django.db.models import Q
# Create your views here.
def verListaLibro(request):
    lista_libro = Libro.objects.all()
    # context = {'lista_libro': lista_libro}
    # return render(request, 'listaLibro.html', context)
    return render(request, 'listaLibro.html', {'lista_libro': lista_libro})

def agregarLibro(request):
    if request.method == 'POST':
        titulo = request.POST.get('title')
        autor = request.POST.get('author')
        genero = request.POST.get('genre')
        copias = request.POST.get('copies')
        libro = Libro(titulo=titulo, autor=autor, genero=genero, copias =copias )
        libro.save()
        return redirect('verlibro', libro_id=libro.id)
    
    return render(request, 'agregarLibro.html')

def verlibro(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    # context = {'libro': libro}
    # return render(request, 'verLibro.html', context)
    return render(request, 'verLibro.html', {'libro': libro})


def borrarLibro(request):
    if request.method == 'POST':
        query = request.POST['query']
        libros = Libro.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
        if len(libros) == 1:
                libros.delete()
                return redirect('verListaLibro')
        elif len(libros) > 1:
            for libro in libros:
                libro.delete()
            return redirect('verListaLibro')
        else:
            context = {
            'title': 'Libro no encontrado',
            'message': 'Ingrese titulo de libro valido o nombre del autor.'
            }
            return render(request, 'ManejadorDeErrores.html', context)
    else:
        return render(request, 'borrarLibro.html')



def buscarLibro(request):
    if request.method == 'POST':
        query = request.POST['query']
        libros = Libro.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))

        if len(libros) == 1:
            # Redirect to the first book found (assuming you want to display the first result)
            return redirect('verlibro', libro_id=libros[0].id)
        elif len(libros) > 1:
            # Display a list of books
            context = {'libros': libros}
            return render(request, 'listaLibro.html', context)
        else:
            context = {
            'title': 'Book not found',
            'message': 'Please enter a valid book title or author name.'
            }
            return render(request, 'ManejadorDeErrores.html', context)
    else:
        return render(request, 'buscar.html')
