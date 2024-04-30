from django.shortcuts import render,redirect,get_object_or_404
from . models import Persona,Ciudad
from django.http import  HttpResponse, JsonResponse

import json
# Create your views here.


def inicio(request):
   ciudades=Ciudad.objects.all() 
   data={
       'ciudades':ciudades
   }
   return render(request,'persona/registro.html',data)
def registrar_persona(request):
    if request.method== 'POST':
        documento=request.POST.get('documento')
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        direccion=request.POST.get('direccion')
        correo=request.POST.get('correo') 
        ciudad=request.POST.get('idCiudad') 
        
        
        persona=Persona(
            documento=documento,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            correo=correo,
            ciudad=Ciudad.objects.get(idCiudad=ciudad),
            
        )
        
        persona.save()
    return redirect('inicio')
def listar_personas(request):
    personas=Persona.objects.all()
    data={
        'personas':personas,
    }
    return render(request,'persona/lista.html',data)

def eliminar_persona(request,id):
    persona=Persona.objects.get(id=id)
    persona.delete()
    return redirect("listar_personas")

def pre_editar_persona(request,id):
    persona=Persona.objects.get(id=id)
    ciudades=Ciudad.objects.all()
    data={
        "persona":persona,
        "ciudades":ciudades
    }
    return render(request,"persona/editar.html",data)

def actualizar_persona(request,id):
    if request.method=="POST":
        persona=Persona.objects.get(id=id)
        persona.documento=request.POST.get('documento')
        persona.nombre=request.POST.get('nombre')
        persona.apellido=request.POST.get('apellido')
        persona.direccion=request.POST.get('direccion')
        persona.correo=request.POST.get('correo')
        persona.ciudad=Ciudad.objects.get(idCiudad=request.POST.get('idCiudad'))
        
        persona.save()
    return redirect("listar_personas")
def listar_ciudades():
    ciudades=Ciudad.objects.all()
    data={
        'ciudades':ciudades,
    }
    return data
def login(request):
     if request.method== 'POST':
        documento=request.POST.get('documento')
        clave=request.POST.get('clave')
        
        usuario=Persona.objects.filter(documento=documento,clave=clave).first()
        if usuario is not None:
            return render(request,"persona/registro.html")
        else:
            return redirect("inicio")
