from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('cvs/', views.lista_cv, name='lista_cv'),
    path('cv/<int:idperfil>/', views.detalle_cv, name='detalle_cv'),
    path('cv/<int:id>/pdf/', views.cv_pdf, name='cv_pdf'),
]
