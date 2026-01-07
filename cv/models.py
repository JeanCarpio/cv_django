from django.db import models

class DatosPersonales(models.Model):
    idperfil = models.AutoField(primary_key=True)
    descripcionperfil = models.CharField(max_length=50)
    perfilactivo = models.BooleanField(default=True)

    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()

    numerocedula = models.CharField(max_length=10, unique=True)

    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6)

    telefonoconvencional = models.CharField(max_length=15)
    telefonofijo = models.CharField(max_length=15)

    direcciontrabajo = models.CharField(max_length=50)
    direcciondomiciliaria = models.CharField(max_length=50)

    sitioweb = models.CharField(max_length=60)

    # 📸 Foto del CV
    foto_perfil = models.ImageField(
        upload_to='fotos_perfil/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

class ExperienciaLaboral(models.Model):
    idexperiencialaboral = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='experiencias'
    )

    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)

    emailempresa = models.EmailField(max_length=100)
    sitiowebempresa = models.CharField(max_length=100)

    nombrecontactoempresarial = models.CharField(max_length=100)
    telefonocontactoempresarial = models.CharField(max_length=60)

    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField(null=True, blank=True)

    descripcionfunciones = models.CharField(max_length=100)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    rutacertificado = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.cargodesempenado
    

class Reconocimiento(models.Model):
    idreconocimiento = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='reconocimientos'
    )

    TIPO_CHOICES = [
        ('Académico', 'Académico'),
        ('Público', 'Público'),
        ('Privado', 'Privado'),
    ]

    tiporeconocimiento = models.CharField(
        max_length=100,
        choices=TIPO_CHOICES
    )

    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)

    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    rutacertificado = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.tiporeconocimiento


class CursoRealizado(models.Model):
    idcursorealizado = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='cursos'
    )

    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField()

    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)

    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)

    emailempresapatrocinadora = models.EmailField(max_length=60)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    rutacertificado = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombrecurso


class ProductoAcademico(models.Model):
    idproductoacademico = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='productos_academicos'
    )

    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    def __str__(self):
        return self.nombrerecurso


class ProductoLaboral(models.Model):
    idproductoslaborales = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='productos_laborales'
    )

    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.CharField(max_length=100)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreproducto


class VentaGarage(models.Model):
    idventagarage = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name='ventas_garage'
    )

    ESTADO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
    ]

    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(
        max_length=40,
        choices=ESTADO_CHOICES
    )

    descripcion = models.CharField(max_length=100)
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)

    activarparaqueseveaenfront = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreproducto
