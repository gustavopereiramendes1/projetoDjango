from django.urls import path
from django.shortcuts import render
from templates import views
#from helloworld.models import Funcionario

app_name = 'website'

urlpatterns = [
    path('', views.index(), name='index'),
]

def lista_funcionarios(request):
    funcionarios = Funcionario.objetos.all()

    contexto = {
        'funcionarios':funcionarios
    }

    return render(
        request,
        "templates/funcionarios.html",
        contexto
    )