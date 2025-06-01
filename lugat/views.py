from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import LugatListSerializer, LugatDetailSerializer
from .models import Lugat

@swagger_auto_schema(method='GET',manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING), openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING)])
@api_view()
def lugat_list_view(request):
    query = request.GET.get('name')
    ordering = request.GET.get('ordering')

    # for frontend search bar, if the length of the query is greater than 4 it shows recomendations
    if query:queryset = Lugat.objects.filter(name__icontains=query) if len(query)>=4 else Lugat.objects.none()

    else:queryset = Lugat.objects.all()
    if ordering:queryset = queryset.order_by(ordering)
    return Response(LugatListSerializer(queryset, many=True).data) 

@swagger_auto_schema(method='POST', request_body=LugatDetailSerializer)
@api_view(['POST'])
def lugat_create_view(request):
    serializer = LugatDetailSerializer(data=request.data)
    if serializer.is_valid():serializer.save(); return Response(serializer.data)
    return Response(serializer.errors)

@api_view()
def lugat_retrieve_view(request, id):
    return Response(LugatDetailSerializer(get_object_or_404(Lugat, pk=id)).data)

@swagger_auto_schema(methods=['PUT', 'PATCH'], request_body=LugatDetailSerializer)
@api_view(['PUT', 'PATCH'])
def lugat_update_view(request, id):
    serializer = LugatDetailSerializer(get_object_or_404(Lugat, pk=id), data=request.data, partial=True)
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)
