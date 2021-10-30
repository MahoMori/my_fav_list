"""myfavlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfav import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.myfavlist, name='myfavlist'),

    path('myfav/book', views.book, name='book'),
    path('myfav/anime_manga', views.animeManga, name='anime_manga'),
    # path('myfav/movie', views.movie, name='movie'),
    # path('myfav/music', views.music, name='music'),
    # path('myfav/game', views.game, name='game'),
    # path('myfav/food', views.food, name='food'),
    # path('myfav/other', views.other, name='other'),

    path('add/', views.addfav, name='addfav'),
    path('myfav/<int:myfav_id>', views.editmyfav, name='editmyfav'),
    path('myfav/<int:myfav_id>/delete', views.delete, name='delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)