
from django.contrib import admin
from django.urls import path
from clinica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.iniciar,name='iniciar'),
    path('inicio', views.home, name='inicio'),
    path('inicioadmin', views.iniciaradmin, name='inicioadmin'),
    path('acceso/inicioa', views.homea, name='inicioa'),
    path('paciente', views.consultar, name='consultar'),
    path('pacientea', views.consultaradmin, name='pacientea'),
    path('pacientes/guardar', views.guardar, name='guardar'),
    path('pacientesa/guardar', views.guardaradmin, name='guardara'),
    path('pacientes/historial', views.historial, name='historial'),
    path('pacientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('pacientes/detalle/<int:id>', views.detalle, name='detalle'),
    path('pacientes/editar', views.editar, name='editar'),
    path('medico',views.consultarm,name='consultarm' ),
    path('medicos/guardar',views.medicoguardar,name='guardarm'),
    path('medicos/eliminar/<int:id>', views.eliminarm, name='eliminarm'),
    path('medicos/detalle/<int:id>', views.detallem, name='detallem'),
    path('medicos/editar', views.editarm, name='editarm'),
    path('contacto',views.contacto, name='contacto'),
    path('contacto/guardar',views.mensajesc, name='mensajes'),
    path('contacto/men',views.mensajesadmin, name='mensajesad'),
    path('mensajes/eliminar/<int:id>', views.eliminarmensajes, name='eliminarmen'),
    path('acceso/admin',views.acceso, name='acceso_admin')
]
