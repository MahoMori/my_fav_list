from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import MyfavForm
from .models import Myfav


# Create your views here.
def myfavlist(request):
    myfavs = Myfav.objects.all
    # myfavs = Myfav.objects.filter(user=request.user)
    return render(
        request,
        'myfav/myfav.html',
        {'myfavs':myfavs}
    )

def addfav(request):
    if request.method == 'GET':
        return render(request, 'myfav/addfav.html', {'form': MyfavForm()})
    else:
        try:
            form = MyfavForm(request.POST)
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