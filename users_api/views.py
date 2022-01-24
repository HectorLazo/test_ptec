from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UsuarioSerializer

from .models import Usuario

@api_view(['GET'])
def apiOverView(request):

	api_urls = {
		'Listar': '/api/usuario-list/',
		'Crear':  '/api/usuario-create/',
		'Detalle': '/api/usuario-detail/<str:pk>',
		'Actualizar': '/api/usuario-update/<str:pk>',
		'Eliminar': '/api/usuario-delete/<str:pk>',
	}

	return Response(api_urls)



@api_view(['GET'])
def usuarioList(request):

	usuarios = Usuario.objects.all()
	serializer = UsuarioSerializer(usuarios, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def usuarioDetail(request, pk):

	# if Usuario.objects.exists(pk=pk):
	# 	usuario = Usuario.objects.get(pk=pk)
	# else:

	usuarios = Usuario.objects.get(pk=pk)
	serializer = UsuarioSerializer(usuarios, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def usuarioCreate(request):

	serializer = UsuarioSerializer(data=request.data)

	if serializer.is_valid(raise_exception=True):
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def usuarioDelete(request, pk):

	# if Usuario.objects.exists(pk=pk):
	# 	usuario = Usuario.objects.get(pk=pk)
	# else:

	usuario = Usuario.objects.get(pk=pk)
	usuario.delete()
	return Response('¡Usuario eliminado correctamente!')
