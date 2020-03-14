# Generated by Django 3.0.3 on 2020-02-29 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_realizacao', models.DateTimeField()),
                ('flyer', models.ImageField(upload_to='')),
                ('local', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=128)),
                ('data_criado', models.DateTimeField()),
                ('data_editado', models.DateTimeField()),
                ('deletado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
                ('data_criado', models.DateTimeField()),
                ('data_editado', models.DateTimeField()),
                ('deletado', models.BooleanField()),
            ],
        ),
    ]
