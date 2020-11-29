from django.shortcuts import render
from rest_framework import generics,filters
from e2app.models import Distrito,Departamento,TipoInstitucion,Provincia,Institucion
from e2app.serializers import DepartamentoSerializer,DistritoSerializer,ProvinciaSerializer\
    ,TipoInstitucionSerializer,InstitucionSerializer
class DepartamentoAPIView(generics.ListCreateAPIView):
    search_fields=['nombDepa']
    filter_backends = (filters.SearchFilter,)
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
class DistritoAPIView(generics.ListCreateAPIView):
    search_fields=['nombDistrito']
    filter_backends = (filters.SearchFilter,)
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
class ProvinciaAPIView(generics.ListCreateAPIView):
    search_fields=['nombProvi']
    filter_backends = (filters.SearchFilter,)
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
class TipoInstitucionAPIView(generics.ListCreateAPIView):
    search_fields=['nombreTipo','id']
    filter_backends = (filters.SearchFilter,)
    queryset = TipoInstitucion.objects.all()
    serializer_class = TipoInstitucionSerializer
class InstitucionAPIView(generics.ListCreateAPIView):
    search_fields=['nombreInsti']
    filter_backends = (filters.SearchFilter,)
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
class InstitucionRUCAPIView(generics.ListCreateAPIView):
    search_fields=['ruc']
    filter_backends = (filters.SearchFilter,)
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
class InstitucionTipoAPIView(generics.ListCreateAPIView):
    search_fields=['codTipo__nombreTipo']
    filter_backends = (filters.SearchFilter,)
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
