from django.shortcuts import render

# Create your views here.
def myfavlist(request):
    return render(request, 'myfav/myfav.html')