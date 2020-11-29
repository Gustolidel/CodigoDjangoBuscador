# Generated by Django 3.1.3 on 2020-11-28 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombDepa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombDistrito', models.CharField(max_length=50)),
                ('codDepa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='TipoInstitucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombProvi', models.CharField(max_length=50)),
                ('codDepa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInsti', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=50)),
                ('representante', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('ruc', models.CharField(max_length=50)),
                ('situacion', models.CharField(max_length=50)),
                ('codDepa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.departamento')),
                ('codDistri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.distrito')),
                ('codProvi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.provincia')),
                ('codTipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.tipoinstitucion')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='codProvi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e2app.provincia'),
        ),
    ]