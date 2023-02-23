from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


from tareasApi.models import Tareas
from tareasApi.serializers import TareasSerializer


# Create your views here.


# @csrf_exempt
# def TareasAPI(request, id=0):
#     if request.method == 'GET':
#         idOp = request.GET.get('status')
#         print(idOp)
#         tareas = Tareas.objects.all()
#         tareas_serializer = TareasSerializer(tareas, many=True)
#         return JsonResponse(tareas_serializer.data, safe=False)
@csrf_exempt
def TareasAPI(request, id=0):
    if request.method == 'POST':
        hoy = datetime.now()
        hoy.strftime('%d-%m-%Y')
        tareas_data = JSONParser().parse(request)
        nombre = request.data.get('title')
        status = request.data.get('status')
        fecha = hoy
        tareas_serializer = TareasSerializer(
            data={'title': nombre, 'status': status, 'create_at': fecha})
        print(request)
        if tareas_serializer.is_valid():
            tareas_serializer.save()
        else:
            print(tareas_serializer.errors)
            return JsonResponse("Tarea agregada", safe=False)
        return JsonResponse("Error", safe=False)

    elif request.method == 'PUT':
        tareas_data = JSONParser().parse(request)
        print(tareas_data)
        tareas = Tareas.objects.get(idTarea=tareas_data['idTarea'])

        tareas_serializer = TareasSerializer(tareas, data=tareas_data)
        if tareas_serializer.is_valid():
            tareas_serializer.save()
            return JsonResponse("Tarea actualizada", safe=False)
        return JsonResponse("Error Actualizar", safe=False)


@api_view(['GET'])
def TareasAPIGET(request):

    respuesta = {}
    respuesta['estado'] = False
    tareas = Tareas.objects.values(
        'idTarea', 'title', 'created_at', 'status__opsnombre')
    if tareas:
        respuesta['estado'] = True
        respuesta['datos'] = tareas
    return Response(respuesta)


@api_view(['DELETE'])
def eliminarTareasAPI(request):
    cargaId = request.GET.get('idTarea')
    print(cargaId)
    tareas = Tareas.objects.get(idTarea=cargaId)

    tareas.delete()

    return Response(status=200)


@api_view(['GET'])
def editarAPI(request):
    cargaId = request.GET.get('idTarea')
    tareas = Tareas.objects.filter(idTarea=cargaId).values()
    return Response(tareas)


@api_view(['POST'])
def postAPI(request):
    ahora = datetime.now()
    fecha_actual = ahora.strftime('%d-%m-%Y')
    hora_actual = ahora.strftime('%H:%M:%S')
    fecha_hora_actual = f"{fecha_actual} {hora_actual}"

    nombre = request.data.get('title')
    status = request.data.get('status')
    print(fecha_hora_actual)
    tareas_serializer = TareasSerializer(
        data={'title': nombre, 'status': status, 'created_at': fecha_hora_actual})
    print(request.data)
    if tareas_serializer.is_valid():
        tareas_serializer.save()
        return JsonResponse("Tarea agregada", safe=False)
    else:
        print(tareas_serializer.errors)
        return JsonResponse("Error", safe=False)


@api_view(['PATCH'])
def putAPI(request):
    title = request.data.get('title')
    id = request.data.get('idTarea')
    status = request.data.get('status')
    fecha = datetime.now()
    fecha_actual = fecha.strftime('%d-%m-%Y')
    hora_actual = fecha.strftime('%H:%M:%S')
    fecha_hora_actual = f"{fecha_actual} {hora_actual}"

    tareas = Tareas.objects.get(idTarea=id)
    print(title, "--------------------------------")
    Tareas_serializer = TareasSerializer(

        tareas, data={'title': title, 'status': status,
                      'created_at': fecha_hora_actual}
    )
    print(Tareas_serializer)
    if Tareas_serializer.is_valid():
        Tareas_serializer.save()
        return Response("Se agrego la tarea")
    else:
        return Response("Error")
