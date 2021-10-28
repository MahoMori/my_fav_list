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
        form = MyfavForm(request.POST, request.FILES, instance=myfav)
        return render(
            request,
            'myfav/editmyfav.html',
            {'myfav': myfav, 'form': form}
        )
    else:
        try:
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