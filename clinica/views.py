from django.shortcuts import render, redirect
from clinica.models import Paciente,Medico,Mensajes
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.
def iniciar(request):
    return render(request,"registro.html")

def iniciaradmin(request):
    return render(request,"principal_admin.html")
def homea(request):
    return render(request,"inicioadmin.html")

def home(request):
    return render(request, "principal.html")


def consultaradmin(request):
    pacientes=Paciente.objects.all()
    return render(request, "pacientesadmin.html",{
        'pacientes' : pacientes
    })

CONTRASEÑA="eternaprimavera"
def acceso(request):
    if request.method=='POST':
        contraseña=request.POST.get("contraseña")
        if contraseña==CONTRASEÑA:
            return HttpResponseRedirect('inicioa')
        else:
            messages.error(request,'Contraseña incorrecta')
    return render(request,"acceso_admin.html")






def consultar(request):
    medicos=Medico.objects.all()
    pacientes=Paciente.objects.all()
    return render(request, "pacientes.html",{
        'medicos' :medicos,
        'pacientes' : pacientes
    })
def guardar(request):
    nombre=request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_de_nacimiento= request.POST["fecha_de_nacimiento"]
    direccion=request.POST["direccion"]
    razon=request.POST["razon"]
    receta=request.POST["receta"]
    numero=request.POST["numero"]
    otros=request.POST["otros"]
    visita=request.POST["visita"]
    #lado derecho nombre del metodo, lado izquierdo es nombre del modelo
    p=Paciente(nombre=nombre,dpi=dpi,fecha_de_nacimiento=fecha_de_nacimiento,direccion=direccion,razon=razon,receta=receta,numero=numero,otros=otros,visita=visita)
    p.save()
    messages.success(request,'Paciente agregado')
    pacientes=Paciente.objects.all()
    medicos=Medico.objects.all()
    return render(request,'pacientes.html',{
        'pacientes':pacientes,
        'medicos' :medicos
    })
def guardaradmin(request):
    nombre=request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_de_nacimiento= request.POST["fecha_de_nacimiento"]
    direccion=request.POST["direccion"]
    razon=request.POST["razon"]
    receta=request.POST["receta"]
    numero=request.POST["numero"]
    otros=request.POST["otros"]
    visita=request.POST["visita"]
    #lado derecho nombre del metodo, lado izquierdo es nombre del modelo
    p=Paciente(nombre=nombre,dpi=dpi,fecha_de_nacimiento=fecha_de_nacimiento,direccion=direccion,razon=razon,receta=receta,numero=numero,otros=otros,visita=visita)
    p.save()
    messages.success(request,'Paciente agregado')
    pacientes=Paciente.objects.all()
    medicos=Medico.objects.all()
    return render(request,'pacientesadmin.html',{
        'pacientes':pacientes,
        'medicos' :medicos
    })
def eliminar(request, id):
    paciente=Paciente.objects.filter(pk=id)
    paciente.delete()
    messages.success(request,'Paciente eliminado')
    return redirect('pacientea')
def detalle(request,id):
    paciente=Paciente.objects.get(pk=id)
    return render(request,"pacienteEditar.html",{'paciente': paciente})


def editar(request):
    nombre=request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_de_nacimiento= request.POST["fecha_de_nacimiento"]
    direccion=request.POST["direccion"]
    razon=request.POST["razon"]
    receta=request.POST["receta"]
    numero=request.POST["numero"]
    otros=request.POST["otros"]
    visita=request.POST["visita"]
    id=request.POST["id"]
    Paciente.objects.filter(pk=id).update(id=id,nombre=nombre,dpi=dpi,fecha_de_nacimiento=fecha_de_nacimiento,direccion=direccion,razon=razon,receta=receta,numero=numero,otros=otros, visita=visita)
    messages.success(request,'Paciente modificado')
    return redirect('pacientea')
def historial(request):
    pacientes=Paciente.objects.all()
    return render(request, "visitas.html",{
        'pacientes' : pacientes
    })
def consultarm(request):
    medicos=Medico.objects.all()
    pacientes=Paciente.objects.all()
    return render(request, "medico.html",{
        'medicos' : medicos,
        'pacientes':pacientes
    })
def medicoguardar(request):
    nombre=request.POST["nombre"]
    numero_de_colegiado=request.POST["numero_de_colegiado"]
    especialidad=request.POST["especialidad"]
    diagnostico=request.POST["diagnostico"]
    otros=request.POST["otros"]
    m=Medico(nombre=nombre,numero_de_colegiado=numero_de_colegiado,especialidad=especialidad,diagnostico=diagnostico,otros=otros)
    m.save()
    messages.success(request, 'proceso exitoso')
    return redirect('consultarm')

def eliminarm(request, id):
    medico=Medico.objects.filter(pk=id)
    medico.delete()
    messages.success(request,'Medico eliminado')
    return redirect('consultarm')
def detallem(request,id):
    medico=Medico.objects.get(pk=id)
    return render(request,"medicoEditar.html",{'medico': medico})

def editarm(request):
    nombre=request.POST["nombre"]
    numero_de_colegiado=request.POST["numero_de_colegiado"]
    especialidad=request.POST["especialidad"]
    diagnostico=request.POST["diagnostico"]
    otros=request.POST["otros"]
    id=request.POST["id"]
    Medico.objects.filter(pk=id).update(id=id,nombre=nombre,numero_de_colegiado=numero_de_colegiado,especialidad=especialidad,diagnostico=diagnostico,otros=otros)
    messages.success(request,'Medico modificado')
    return redirect('consultarm')
def contacto(request):
    return render(request,"Contacto.html")


def mensajesc(request):
    nom_paciente=request.POST["nom_paciente"]
    numero=request.POST["numero"]
    mensaje=request.POST["mensaje"]
   
    #lado derecho nombre del metodo, lado izquierdo es nombre del modelo
    men=Mensajes(nom_paciente=nom_paciente,numero=numero,mensaje=mensaje)
    men.save()
    messages.success(request,'Mensaje enviado con éxito')
    mensajes=Mensajes.objects.all()
    return render(request,'Contacto.html',{
        'mensaje':mensajes
    })
def mensajesadmin(request):
    mensajes=Mensajes.objects.all()
    return render(request, "Contactoadmin.html",{
        'mensajes':mensajes
        
    })
def eliminarmensajes(request, id):
    mensajes=Mensajes.objects.filter(pk=id)
    mensajes.delete()
    messages.success(request,'Mensaje eliminado')
    return redirect('mensajesad')



