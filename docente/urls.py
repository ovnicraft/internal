from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.docente_detail, name='docente_detail')
]
