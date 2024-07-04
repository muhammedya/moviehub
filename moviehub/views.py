from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from moviehub.forms import MovieForm
from moviehub.models import Movie



# from moviehub.models import Actor

# Create your views here.
# ------------------------------------
        #vritua lenv : movie
        # username: surya
        # email: surya@gmail.com
        # pasword: admin@123
# ------------------------------------

def index(request):
    movie=Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)




def detail(request, movie_id):
    movie=Movie.objects.get(id=movie_id)

    # forse delete witho confirmation.
    # if request.method=='POST':
    #     movie=Movie.objects.get(id=movie_id)
    #     movie.delete()
    #     messages.success(request, 'Movie deleted successfully !')
    #     return redirect('/')

    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        return redirect("/")
    return render(request, 'add.html')


def update(request, id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'movie':movie})

# def delete(request, id):
#     movie=Movie.objects.get(id=id)
#     if request.method=='POST':
#         movie=Movie.objects.get(id=id)
#         movie.delete()
#         messages.success(request, f'The movie "{movie.name}" deleted successfully !')
#         return redirect('/')
#     return render(request, 'delete.html', {'movie':movie})


def delete(request, id):
    # Fetch the movie object or return a 404 error if not found
    movie = get_object_or_404(Movie, id=id)
    movie_name = movie.name  # Capture the movie name before deletion

    if request.method == 'POST':
        movie.delete()
        messages.success(request, f'The movie {movie_name} was deleted successfully')
        return redirect('/')  # Redirect after deletion

    return render(request, 'delete.html', {'movie': movie})

