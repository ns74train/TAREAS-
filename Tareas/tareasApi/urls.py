from django.urls import path
from tareasApi import views
from django.conf import settings
from django.conf import urls

urlpatterns = [

    path('tarea-registro', views.TareasAPI),
    path('tarea-get', views.TareasAPIGET),
    path('tarea-registro/<id>', views.TareasAPI),
    path('tarea-eliminar', views.eliminarTareasAPI),
    path('tarea-editar', views.editarAPI),
    path('tarea-post', views.postAPI),
    path('tarea-put', views.putAPI),


]
