# Generated by Django 5.0.6 on 2024-07-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0017_alter_pedido_estado_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('ENVIADO', 'Enviado'), ('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], default='Pendiente', max_length=10),
        ),
    ]
