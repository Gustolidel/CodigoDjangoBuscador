from rest_framework import serializers
from e2app.models import Distrito,Departamento,Provincia,Institucion,TipoInstitucion
class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Distrito
        fields='__all__'
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields='__all__'
class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provincia
        fields='__all__'
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institucion
        fields='__all__'
class TipoInstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoInstitucion
        fields='__all__'