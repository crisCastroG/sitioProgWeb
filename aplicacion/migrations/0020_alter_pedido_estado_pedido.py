# Generated by Django 5.0.6 on 2024-07-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0019_productocarro_codigo_carro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('PENDIENTE', 'Pendiente'), ('ENVIADO', 'Enviado')], default='Pendiente', max_length=10),
        ),
    ]
