# Generated by Django 4.1.2 on 2024-06-28 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_on_tour', '0003_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
