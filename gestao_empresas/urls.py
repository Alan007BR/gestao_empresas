"""
URL configuration for gestao_empresas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from empresas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('empresas/<int:empresa_id>/', views.detalhes_empresa, name='detalhes_empresa'),
    path('empresas/cadastrar/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('empresas/editar/<int:empresa_id>/', views.editar_empresa, name='editar_empresa'),
    path('empresas/excluir/<int:empresa_id>/', views.excluir_empresa, name='excluir_empresa'),
    path('empresas/<int:empresa_id>/funcionarios/cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('empresas/<int:empresa_id>/funcionarios/editar/<int:funcionario_matricula>/', views.editar_funcionario, name='editar_funcionario'),
    path('empresas/<int:empresa_id>/funcionarios/excluir/<int:funcionario_matricula>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
]
