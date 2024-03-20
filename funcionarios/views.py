from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionarios
from .forms import FuncionariosForm

def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

def cria_funcionario(request):
    if request.method == 'POST':
        form = FuncionariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionariosForm()
    return render(request, 'funcionarios/cria_funcionario.html', {'form': form})

def edita_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    if request.method == 'POST':
        form = FuncionariosForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionariosForm(instance=funcionario)
    return render(request, 'funcionarios/edita_funcionario.html', {'form': form})


def deleta_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    funcionario.delete()
    return redirect('lista_funcionarios')

def buscar_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    busca= request.GET.get('search')
    
    if busca:
        funcionarios=funcionarios.objects.filter(nome_icontains=busca)
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})