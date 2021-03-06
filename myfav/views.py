from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import MyfavForm
from .models import Myfav


# Create your views here.
def myfavlist(request):
    myfavs = Myfav.objects.all()
    # myfavs = Myfav.objects.filter(user=request.user)
    return render(
        request,
        'myfav/myfav.html',
        {'myfavs':myfavs}
    )

def book(request):
    books = Myfav.objects.filter(genre__iexact='book')
    return render(
        request,
        'myfav/book.html',
        {'books':books}
    )

def animeManga(request):
    ams = Myfav.objects.filter(genre__iexact='anime/manga')
    return render(
        request,
        'myfav/anime_manga.html',
        {'ams':ams}
    )

def movie(request):
    movies = Myfav.objects.filter(genre__iexact='movie')
    return render(
        request,
        'myfav/movie.html',
        {'movies':movies}
    )

def music(request):
    musics = Myfav.objects.filter(genre__iexact='music')
    return render(
        request,
        'myfav/music.html',
        {'musics':musics}
    )

def game(request):
    games = Myfav.objects.filter(genre__iexact='game')
    return render(
        request,
        'myfav/game.html',
        {'games':games}
    )

def food(request):
    foods = Myfav.objects.filter(genre__iexact='food')
    return render(
        request,
        'myfav/food.html',
        {'foods':foods}
    )

def other(request):
    others = Myfav.objects.filter(genre__iexact='other')
    return render(
        request,
        'myfav/other.html',
        {'others':others}
    )


def addfav(request):
    if request.method == 'GET':
        return render(request, 'myfav/addfav.html', {'form': MyfavForm()})
    else:
        try:
            form = MyfavForm(request.POST, request.FILES)
            newFav = form.save()
            return redirect('myfavlist')
        except ValueError:
            return render(
                request,
                'myfav/addfav.html',
                {
                    'form': MyfavForm(),
                    'error': 'An error occured. Try again.'
                }
            )

def editmyfav(request, myfav_id):
    myfav = get_object_or_404(Myfav, pk=myfav_id)
    if request.method == 'GET':
        form = MyfavForm({'myfav': myfav})
        # form = MyfavForm(request.POST, request.FILES, instance=myfav)
        return render(
            request,
            'myfav/editmyfav.html',
            {'myfav': myfav, 'form': form}
        )
    else:
        try:
            if not request.FILES:
                request.FILES['image'] = myfav.image
            form = MyfavForm(request.POST, request.FILES, instance=myfav)
            form.save()
            return redirect('myfavlist')
        except ValueError:
            return render(
                request,
                'myfav/editmyfav.html',
                {'myfav': myfav, 'form': form, 'error': 'An error occured. Try again.'}
        )

def delete(request, myfav_id):
    myfav = get_object_or_404(Myfav, pk=myfav_id)
    if request.method == 'POST':
        myfav.delete()
        return redirect('myfavlist')