# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from utilidades.impresora import (
    testF, 
    configurarPueto, 
    statusImpresora,
    enviarComando,
    ReporteXPrint,
    ReporteZPrint,
    datosReporteX1, 
    datosReporteX2, 
    datosReporteX4, 
    datosReporteX5, 
    datosReporteX7, 
    datosImpresora1,
    datosImpresora2,
    datosImpresora3,
    datosImpresora4,
    datosImpresora5,
    datosImpresora6,
    datosImpresora7,
    datosImpresora8E,
    datosImpresora8P,
    )
from django.core.cache import cache
from models import Puerto

# Create your views here.

def index(request):
    status=testF()
    return HttpResponse("Hello word")

def configurarPuerto(request):
    DB_PORT=Puerto.objects.last()
    print('Ultimo puerto:' + DB_PORT.nombre)
    PORT = cache.get_or_set('PORT', '')
    try:
        PORT = configurarPueto()
        cache.set('PORT', PORT)
        Puerto.objects.create(
            nombre=PORT
        )
        
        return JsonResponse({
            "message":"puerto configurado: "+ PORT,
            "status":True,
            "port":PORT
            })
    except Exception as e:
        print(e)
        return JsonResponse({
            "message":"Error al configurar el puerto",
            "error":True
        })

def status(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            resp=statusImpresora(PORT)
            return JsonResponse({
                    "resp":resp,
                    "status":True,
                    "error":False
                    })
        else:
           raise Exception('el puerto no esta configurado')
    except Exception as e:
        print(e)
        return JsonResponse({
                "message":"Error al configurar el puerto",
                "error":True
            })

    
@api_view(['GET'])
def enviarComandoCMD(req):
    comando= req.query_params.get('comando')
    print(comando)
    
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    if PORT == DB_PORT.nombre and isinstance(PORT,str):
        resp=enviarComando(PORT, comando)
        return HttpResponse("Reporte Impreso")
    else:
        return HttpResponse("error al imprimir") 

def imprimirReporteX(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            ReporteXPrint(PORT)
            return JsonResponse({
                        "resp":'reporte Impreso',
                        "error":False
                        })
        else:
           raise Exception('el puerto no esta configurado')
    except Exception as e:
        print(e)
        return JsonResponse({
                "message":"Error al configurar el puerto",
                "error":True
            })
    
def imprimirReporteZ(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    if PORT == DB_PORT.nombre and isinstance(PORT,str):
        ReporteZPrint(PORT)
        return HttpResponse("Reporte Impreso Z")
    else:
        return HttpResponse("error al imprimir")
    
def getReporteX1(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX1(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X1", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX2(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX2(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X2", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
    
def getReporteX4(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX4(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X4", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX5(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX5(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X5", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX7(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX7(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X7", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
        
def getDatosImpresora1(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora1(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 1", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 

def getDatosImpresora2(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora2(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 2", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
def getDatosImpresora3(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora3(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 3", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
def getDatosImpresora4(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora4(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 4", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
def getDatosImpresora5(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora5(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 5", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
def getDatosImpresora6(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora6(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 6", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
      
def getDatosImpresora7(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora7(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora 7", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True})
     
def getDatosImpresora8E(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora8E(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora encabezado", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
def getDatosImpresora8P(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosImpresora8P(PORT)
            return JsonResponse({
                    "mensaje":"Datos de la impresora pie", 
                    "datos":datos.__dict__,
                    "status":True}) 
        else:
            return JsonResponse({"error":True}) 
    except Exception as e:
        return JsonResponse({"error":True}) 
