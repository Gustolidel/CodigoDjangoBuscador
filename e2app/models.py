from django.db import models
class Departamento(models.Model):
    nombDepa = models.CharField(max_length=50)
    def __str__(self):
        return self.nombDepa
class Provincia(models.Model):
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    nombProvi = models.CharField(max_length=50)
    def __str__(self):
        return self.nombProvi
class Distrito(models.Model):
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    codProvi = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)
    nombDistrito = models.CharField(max_length=50)
    def __str__(self):
        return self.nombDistrito
class TipoInstitucion(models.Model):
    nombreTipo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombreTipo
class Institucion(models.Model):
    nombreInsti = models.CharField(max_length=50)
    sigla = models.CharField(max_length=50)
    representante = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    ruc = models.CharField(max_length=50)
    situacion = models.CharField(max_length=50)
    codTipo = models.ForeignKey(TipoInstitucion, null=True, on_delete=models.CASCADE)
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    codProvi = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)
    codDistri = models.ForeignKey(Distrito, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreInsti