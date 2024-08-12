from django.conf.urls import url

from . import views
 
urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^configurarPuerto/', views.configurarPuerto, name='configurarPuerto'),
    url(r'^status/', views.status, name='status'),
    url(r'^enviarComandoCMD/', views.enviarComandoCMD, name='enviarComandoCMD'),
    url(r'^imprimirReporteX/', views.imprimirReporteX, name='imprimirReporteX'),
    url(r'^imprimirReporteZ/', views.imprimirReporteZ, name='imprimirReporteZ'),
    url(r'^getReporteX1/', views.getReporteX1, name='getReporteX1'),
    url(r'^getReporteX2/', views.getReporteX2, name='getReporteX2'),
    url(r'^getReporteX4/', views.getReporteX4, name='getReporteX4'),
    url(r'^getReporteX5/', views.getReporteX5, name='getReporteX5'),
    url(r'^getReporteX7/', views.getReporteX7, name='getReporteX7'),
    url(r'^getDatosImpresora1/', views.getDatosImpresora1, name='getDatosImpresora1'),
    url(r'^getDatosImpresora2/', views.getDatosImpresora2, name='getDatosImpresora2'),
    url(r'^getDatosImpresora3/', views.getDatosImpresora3, name='getDatosImpresora3'),
    url(r'^getDatosImpresora4/', views.getDatosImpresora4, name='getDatosImpresora4'),
    url(r'^getDatosImpresora5/', views.getDatosImpresora5, name='getDatosImpresora5'),
    url(r'^getDatosImpresora6/', views.getDatosImpresora6, name='getDatosImpresora6'),
    url(r'^getDatosImpresora7/', views.getDatosImpresora7, name='getDatosImpresora7'),
    url(r'^getDatosImpresora8E/', views.getDatosImpresora8E, name='getDatosImpresora8E'),
    url(r'^getDatosImpresora8P/', views.getDatosImpresora8P, name='getDatosImpresora8P'),
]