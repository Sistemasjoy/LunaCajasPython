# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import threading
import json
import time
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
    datosReporteZ,
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

command_lock = threading.Lock()


def disponible():
    if command_lock.locked():
        print("Printer busy")
        return JsonResponse({"error": "Printer busy"}, status=503)


def index(request):
    status = testF()
    print(status)
    return HttpResponse("Hello word")


def configurarPuerto(request):
    disponible()
    try:
        DB_PORT = Puerto.objects.last()
        print("Ultimo puerto:" + DB_PORT.nombre)
        OLD_PORT =DB_PORT.nombre
        resp = statusImpresora(OLD_PORT)
        if 'Sin error' in resp:
            print(resp, "el puerto sigue activo")
            PORT = OLD_PORT
        else:
            # PORT = cache.get_or_set("PORT", "")
            PORT = configurarPueto()
            Puerto.objects.create(nombre=str(PORT))
        
        cache.set("PORT", str(PORT))

        return JsonResponse(
            {"message": "puerto configurado: " + PORT, "status": True, "port": PORT}
        )
    except Exception as e:
        print(e)
        return JsonResponse({"message": "Error al configurar el puerto", "error": True})


def status(req):
    disponible()
    try:
        PORT = cache.get("PORT")
        DB_PORT = Puerto.objects.last()
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            print("verificando status")
            resp = statusImpresora(PORT)
            return JsonResponse({"resp": resp, "status": True, "error": False})
        else:
            raise Exception("el puerto no esta configurado")
    except Exception as e:
        print(e)
        return JsonResponse({"message": "Error al configurar el puerto", "error": True})


@api_view(["POST"])
def enviarComandoCMD(request):
    disponible()
    try:
        params = request.data.get("params")
        comando = params["com"]
        tipo = params["tipo"]
        PORT = cache.get("PORT")
        DB_PORT = Puerto.objects.last()
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            with command_lock:
                if tipo == "factura":
                    imprimirFactura(comando, PORT)
                # resp=enviarComando(PORT, comando)
                print("esperado....")
                time.sleep(6)
                print("listo")
                return JsonResponse(
                    {"resp": "pendiente", "status": True, "error": False}
                )
        else:
            return JsonResponse(
                {
                    "resp": "El puerto no esta configurado",
                    "status": False,
                    "error": True,
                }
            )
    except Exception as e:
        return JsonResponse(
            {"resp": str(e), "error": True, "status": False}, status=500
        )


@api_view(["GET"])
def enviarComandoCMDGET(request):
    disponible()
    comando = request.query_params.get("comando")
    print(comando)
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    if PORT == DB_PORT.nombre and isinstance(PORT, str):
        resp = enviarComando(PORT, comando)

        return JsonResponse({"resp": resp, "status": True, "error": False})
    else:
        return JsonResponse(
            {"resp": "El puerto no esta configurado", "status": False, "error": True}
        )


@api_view(["POST"])
def enviarComandoCMDPOST(request):
    disponible()
    comando = request.data.get("comando")
    print(comando)
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    if PORT == DB_PORT.nombre and isinstance(PORT, str):
        resp = enviarComando(PORT, comando)

        return JsonResponse({"resp": resp, "status": True, "error": False})
    else:
        return JsonResponse(
            {"resp": "El puerto no esta configurado", "status": False, "error": True}
        )


def imprimirFactura(com, PORT):
    data = json.loads(com)
    print(data)
    print(type(data))
    for line in data:
        print(str(line))
        resp = enviarComando(PORT, line)
    return None


def imprimirReporteX(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            ReporteXPrint(PORT)
            return JsonResponse({"resp": "reporte Impreso", "error": False})
        else:
            raise Exception("el puerto no esta configurado")
    except Exception as e:
        print(e)
        return JsonResponse({"message": "Error al configurar el puerto", "error": True})


def imprimirReporteZ(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            ReporteZPrint(PORT)
            return JsonResponse({"resp": "reporte Impreso", "error": False})
        else:
            raise Exception("el puerto no esta configurado")
    except Exception as e:
        print(e)
        return JsonResponse({"message": "Error al configurar el puerto", "error": True})


def getReporteX1(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteX1(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte X1", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getReporteX2(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteX2(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte X2", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getReporteX4(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()

    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteX4(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte X4", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getReporteX5(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()

    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteX5(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte X5", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getReporteX7(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()

    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteX7(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte X7", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getZReport(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()

    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosReporteZ(PORT)
            return JsonResponse(
                {"mensaje": "Datos del reporte z", "datos": datos.__dict__}
            )
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta")


def getDatosImpresora1(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora1(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 1",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora2(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora2(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 2",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora3(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora3(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 3",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora4(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora4(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 4",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora5(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora5(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 5",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora6(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora6(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 6",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora7(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora7(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora 7",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora8E(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora8E(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora encabezado",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})


def getDatosImpresora8P(req):
    disponible()
    PORT = cache.get("PORT")
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT, str):
            datos = datosImpresora8P(PORT)
            return JsonResponse(
                {
                    "mensaje": "Datos de la impresora pie",
                    "datos": datos.__dict__,
                    "status": True,
                }
            )
        else:
            return JsonResponse({"error": True})
    except Exception as e:
        return JsonResponse({"error": True})
