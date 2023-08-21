from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Empresa, Funcionario

@login_required(login_url='')
def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/lista_empresas.html', {'empresas': empresas})

@login_required(login_url='')
def detalhes_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    funcionarios = Funcionario.objects.filter(empresa=empresa)
    return render(request, 'empresas/detalhes_empresa.html', {'empresa': empresa, 'funcionarios': funcionarios})

@login_required(login_url='')
def cadastrar_empresa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        contato = request.POST['contato']
        empresa = Empresa(nome=nome, endereco=endereco, contato=contato)
        empresa.save()
        return redirect('lista_empresas')
    return render(request, 'empresas/cadastrar_empresa.html')

@login_required(login_url='')
def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        empresa.nome = request.POST['nome']
        empresa.endereco = request.POST['endereco']
        empresa.contato = request.POST['contato']
        empresa.save()
        return redirect('lista_empresas')
    return render(request, 'empresas/editar_empresa.html', {'empresa': empresa})

@login_required(login_url='')
def excluir_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        empresa.delete()
        return redirect('lista_empresas')
    return render(request, 'empresas/excluir_empresa.html', {'empresa': empresa})

@login_required(login_url='')
def cadastrar_funcionario(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        nome = request.POST['nome']
        cargo = request.POST['cargo']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        email = request.POST['email']
        telefone = request.POST['telefone']
       
        matricula = Funcionario.proximo_matricula_funcionario(empresa)
        funcionario = Funcionario(empresa=empresa, nome=nome, cargo=cargo, endereco=endereco, cidade=cidade, email=email, telefone=telefone, matricula=matricula)
        funcionario.save()
        return redirect('detalhes_empresa', empresa_id=empresa.id)
    return render(request, 'empresas/cadastrar_funcionario.html', {'empresa': empresa})

@login_required(login_url='')
def editar_funcionario(request, empresa_id, funcionario_matricula):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    funcionario = get_object_or_404(Funcionario, empresa=empresa, matricula=funcionario_matricula)
    if request.method == 'POST':
        funcionario.matricula = request.POST['matricula']
        funcionario.nome = request.POST['nome']
        funcionario.cargo = request.POST['cargo']
        funcionario.endereco = request.POST['endereco']
        funcionario.cidade = request.POST['cidade']
        funcionario.email = request.POST['email']
        funcionario.telefone = request.POST['telefone']
        funcionario.save()  # Salva as alterações no banco de dados
        return redirect('detalhes_empresa', empresa_id=empresa.id)
    return render(request, 'empresas/editar_funcionario.html', {'empresa': empresa, 'funcionario': funcionario})

@login_required(login_url='')
def excluir_funcionario(request, empresa_id, funcionario_matricula):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    funcionario = get_object_or_404(Funcionario, empresa=empresa, matricula=funcionario_matricula)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('detalhes_empresa', empresa_id=empresa.id)
    return render(request, 'empresas/excluir_funcionario.html', {'empresa': empresa, 'funcionario': funcionario})