from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("configurarPuerto/", views.configurarPuerto, name="configurarPuerto"),
    path("status/", views.status, name="status"),
    path("enviarComandoCMD/", views.enviarComandoCMD, name="enviarComandoCMD"),
    path("enviarComandoCMD2/", views.enviarComandoCMDGET, name="enviarComandoCMDGET"),
    path("enviarComandoCMD3/", views.enviarComandoCMDPOST, name="enviarComandoCMDPOST"),
    path("imprimirReporteX/", views.imprimirReporteX, name="imprimirReporteX"),
    path("imprimirReporteZ/", views.imprimirReporteZ, name="imprimirReporteZ"),
    path("getReporteX1/", views.getReporteX1, name="getReporteX1"),
    path("getReporteX2/", views.getReporteX2, name="getReporteX2"),
    path("getReporteX4/", views.getReporteX4, name="getReporteX4"),
    path("getReporteX5/", views.getReporteX5, name="getReporteX5"),
    path("getReporteX7/", views.getReporteX7, name="getReporteX7"),
    path("getZReport/", views.getZReport, name="getZReport"),
    path("getDatosImpresora1/", views.getDatosImpresora1, name="getDatosImpresora1"),
    path("getDatosImpresora2/", views.getDatosImpresora2, name="getDatosImpresora2"),
    path("getDatosImpresora3/", views.getDatosImpresora3, name="getDatosImpresora3"),
    path("getDatosImpresora4/", views.getDatosImpresora4, name="getDatosImpresora4"),
    path("getDatosImpresora5/", views.getDatosImpresora5, name="getDatosImpresora5"),
    path("getDatosImpresora6/", views.getDatosImpresora6, name="getDatosImpresora6"),
    path("getDatosImpresora7/", views.getDatosImpresora7, name="getDatosImpresora7"),
    path("getDatosImpresora8E/", views.getDatosImpresora8E, name="getDatosImpresora8E"),
    path("getDatosImpresora8P/", views.getDatosImpresora8P, name="getDatosImpresora8P"),
]
