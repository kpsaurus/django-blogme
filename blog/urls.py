from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post, name='post'),
    path('tag/<slug:slug>', views.tag, name='tag'),
    path('category/<slug:slug>', views.category, name='category'),
    path('summernote/', include('django_summernote.urls')),

]
