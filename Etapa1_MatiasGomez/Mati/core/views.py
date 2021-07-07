from django.shortcuts import render,redirect
from .forms import ColaboradoresForm
from .models import Colaboradores
# Create your views here.
def Inicio (request): 
    return render (request,'Sesión.html')

def Catalogo (request): 
    return render (request,'modificar.html')

def Acercade (request): 
    return render (request,'mostrarpedido.html')

def formulario(request):
    return render(request, 'formulario.html')
def actualizar(request):
    return render (request, 'core/modificar.html')

def form_colaboradores(request):
    if request.method =='POST':
        clb=ColaboradoresForm(request.POST)
        if clb.is_valid():
            clb.save()
            return redirect('formulario')
    else:
        clb=ColaboradoresForm()
    return render(request, 'core/Sesión.html', {'clb': clb})

def VerColaboradores(request):
    clbb = Colaboradores.objects.all()
    return render(request, 'core/mostrarpedido.html', context={'clbb':clbb})

def modColaborador(request,id):
    mod = Colaboradores.objects.get(rut=id)

    datos ={
           'form': ColaboradoresForm(instance=mod)
    }
    if request.method == 'POST': 
        modd = ColaboradoresForm(data=request.POST, instance = mod)
        if modd.is_valid: 
            modd.save()          
            return redirect('mostrarpedido') 
    return render(request, 'core/modificar.html', datos)

def delColaborador(request,id):
    dele = Colaboradores.objects.get(rut=id)
    dele.delete()
    return redirect('mostrarpedido')