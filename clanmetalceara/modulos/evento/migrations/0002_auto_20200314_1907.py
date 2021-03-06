# Generated by Django 3.0.3 on 2020-03-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='bairro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='cidade',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='fachada',
            field=models.ImageField(blank=True, null=True, upload_to='local-evento/'),
        ),
        migrations.AddField(
            model_name='local',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_criado',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_editado',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_realizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='flyer',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evento.Local'),
        ),
        migrations.AlterField(
            model_name='local',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
