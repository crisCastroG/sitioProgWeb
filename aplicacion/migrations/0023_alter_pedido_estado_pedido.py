# Generated by Django 5.0.6 on 2024-07-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0022_alter_pedido_estado_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('ENVIADO', 'Enviado'), ('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], default='Pendiente', max_length=10),
        ),
    ]
